import os

real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)


STABILITY_KEY = os.environ.get('STABILITY_KEY')
GENERATED_IMG_DIR = os.environ.get(
    'GENERATED_IMG_DIR',
    f'{dir_path}/../generated')

# Image Resolution can be provided like `2160x1080` in the env variable
IMAGE_RESOLUTION = os.environ.get('IMAGE_RESOLUTION')
if IMAGE_RESOLUTION is not None:
    IMAGE_RESOLUTION = IMAGE_RESOLUTION.split('x')
else:
    # Default Resolution
    IMAGE_RESOLUTION = 1088, 512
