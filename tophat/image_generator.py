import abc
import datetime
import io
import os
import uuid
import warnings

from IPython.display import display
from PIL import Image
import pygame
import stability_sdk.client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

import constants
import settings


class ImageGen(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def generate(self, prompt):
        pass

    @staticmethod
    def get_save_path(using_uuid=False):
        if using_uuid:
            # Use UUID as filename
            filename = f'{str(uuid.uuid4())}.png'
        else:
            # Use datetime as filename
            filename = f'{str(datetime.datetime.now())}.png'

        # Generate full path
        save_path = os.path.join(
            settings.GENERATED_IMG_DIR,
            filename,
        )

        return save_path


class StabilityAPIGen(ImageGen):
    def __init__(
            self,
            api_key: str,
            width: int,
            height: int,
            steps: int,
            use_sdl_display: bool = False
    ):
        # Connect to stability API
        self.stability_api = stability_sdk.client.StabilityInference(
            key=api_key,
            verbose=True,
        )

        self.width = width
        self.height = height
        self.steps = steps

        if constants.DEBUG_MODE:
            self.width = constants.DEBUG_MODE_IMAGE_RESOLUTION[0]
            self.height = constants.DEBUG_MODE_IMAGE_RESOLUTION[1]
            self.steps = constants.DEBUG_MODE_IMAGE_GENERATION_STEPS

        self.use_sdl_display = use_sdl_display
        if use_sdl_display:

            if settings.FULLSCREEN_MODE:
                screen_mode = pygame.FULLSCREEN
            else:
                screen_mode = pygame.SHOWN
            # Setup Pygame
            pygame.init()
            self.sdl_screen = pygame.display.set_mode(
                (self.width, self.height),
                screen_mode,
            )
            pygame.display.set_caption('Image Generation SDL Display')

            self.sdl_screen.fill((0, 0, 0))
            pygame.display.flip()

    def generate(self, prompt):
        save_path = None

        # the object returned is a python generator
        answers = self.stability_api.generate(
            prompt=prompt,
            width=self.width,
            height=self.height,
            steps=self.steps,
            # seed=567,  # if provided, specifying a random seed makes results deterministic
        )

        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    warnings.warn(
                        "Your request activated the API's safety filters and could not be processed."
                        "Please modify the prompt and try again.")
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    display(img)
                    save_path = self.get_save_path()
                    img.save(save_path)

                    print(f"Saved new file to `{save_path}`")

                    # Show the new image
                    if self.use_sdl_display:

                        pygame_img = pygame.image.load(save_path)
                        self.sdl_screen.fill((0, 0, 0))
                        self.sdl_screen.blit(pygame_img, (0, 0))

                        pygame.display.flip()

                    break

        return save_path
