import io
import os
import uuid
import warnings

from IPython.display import display
from PIL import Image
import stability_sdk.client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

import constants
import settings


def run():
    # Connect to stability API
    stability_api = stability_sdk.client.StabilityInference(
        key=settings.STABILITY_KEY,
        verbose=True,
    )

    print(f"Running TopHat v{constants.VERSION}")
    print(settings.STABILITY_KEY)

    # the object returned is a python ge
    #         prompt="Obama on the moon on a unicorn juggling bassoons, 4k",
    #         width=settings.IMAGE_RESOLUTION[0],
    #         height=settings.IMAGE_RESOLUTION[1],
    #         # seed=567,  # if provided, specifying a random seed makes results deterministic
    #     )
    #
    #     # iterating over the generator produces the api response
    #     for resp in answers:
    #         for artifact in resp.artifacts:
    #             if artifact.finish_reason == generation.FILTER:
    #                 warnings.warn(
    #                     "Your request activated the API's safety filters and could not be processed."
    #                     "Please modify the prompt and try again.")
    #             if artifact.type == generation.ARTIFACT_IMAGE:
    #                 img = Image.open(io.BytesIO(artifact.binary))
    #                 display(img)
    #                 filename = f'{str(uuid.uuid4())}.png'
    #                 save_path = os.path.join(
    #                     settings.GENERATED_IMG_DIR,
    #                     filename,
    #                 )
    #                 img.save(save_path)nerator
    answers = stability_api.generate(