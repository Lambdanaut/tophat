import os

real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)


# API Key to use to connect to Stability API for image generation
STABILITY_KEY = os.environ.get('STABILITY_KEY')

# API Key to use to connect to DEEPGram for voice transcription
DEEPGRAM_KEY = os.environ.get('DEEPGRAM_KEY')

# Where to save generated images
GENERATED_IMG_DIR = os.environ.get(
    'GENERATED_IMG_DIR',
    f'{dir_path}/../cache/generated-images')

# Where to save generated images
AUDIO_RECORDINGS_DIR = os.environ.get(
    'AUDIO_RECORDINGS_DIR',
    f'{dir_path}/../cache/audio-recordings')

# Image Resolution can be provided like `2160x1080` in the env variable
IMAGE_RESOLUTION = os.environ.get('IMAGE_RESOLUTION')
if IMAGE_RESOLUTION is not None:
    IMAGE_RESOLUTION = IMAGE_RESOLUTION.split('x')
else:
    # Default Resolution
    IMAGE_RESOLUTION = 1088, 512

# Steps to produce the sample. More steps=higher res, and potentially more $
IMAGE_GENERATION_STEPS = os.environ.get('IMAGE_GENERATION_STEPS', 50)
