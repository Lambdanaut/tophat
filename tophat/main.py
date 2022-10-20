import datetime

import voicemsg

import constants
import image_generator
import settings


image_gen = image_generator.StabilityAPIGen(
    settings.STABILITY_KEY)


def run():
    print(f"Running TopHat v{constants.VERSION}")
    print(settings.STABILITY_KEY)

    # image_gen.generate(
    #     width=settings.IMAGE_RESOLUTION[0],
    #     height=settings.IMAGE_RESOLUTION[1],
    #     steps=settings.IMAGE_GENERATION_STEPS,
    # )

    vm = voicemsg.VoiceMsg(
        filepath=constants.audio_recordings_filepath,
        debug=True)
    vm.calibrate(show_demo_text=True)  # Calibrates the silence threshold

    print("TopHat initialized")

    message_id: str = str(datetime.datetime.now())
    message_filename = "{}.wav".format(message_id)
    vm.record(message_filename)

    print("\nMessage successfully recorded!")