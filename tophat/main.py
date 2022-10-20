import asyncio
import datetime

import deepgram
import voicemsg

import constants
import image_generator
import settings

image_gen = image_generator.StabilityAPIGen(
    settings.STABILITY_KEY)

dg_client = deepgram.Deepgram(settings.DEEPGRAM_KEY)


def run():
    print(f"Running TopHat v{constants.VERSION}")
    print(settings.STABILITY_KEY)

    vm = voicemsg.VoiceMsg(
        filepath=settings.AUDIO_RECORDINGS_DIR,
        debug=True)
    vm.calibrate(show_demo_text=True)  # Calibrates the silence threshold

    print("TopHat initialized")

    while True:
        print("Listening for voice message")

        message_id: str = str(datetime.datetime.now())
        message_filename = "{}.wav".format(message_id)
        vm.record(message_filename)

        print("\nMessage successfully recorded!")

        message_filepath = f"{settings.AUDIO_RECORDINGS_DIR}/{message_filename}"
        with open(message_filepath, 'rb') as audio_recording_f:
            source = {'buffer': audio_recording_f, 'mimetype': 'audio/wav'}

            response = asyncio.run(
                dg_client.transcription.prerecorded(
                    source,
                    {'punctuate': True}
                )
            )

        try:
            parsed_text_from_speech = \
                response.get('results', {}).get('channels', {}).pop().get('alternatives').pop().get('transcript')
        except IndexError:
            print("Couldn't get text recognition result")
            continue

        print(parsed_text_from_speech)

        image_gen.generate(
            prompt=parsed_text_from_speech,
            width=settings.IMAGE_RESOLUTION[0],
            height=settings.IMAGE_RESOLUTION[1],
            steps=settings.IMAGE_GENERATION_STEPS,
        )
