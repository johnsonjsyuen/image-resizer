import math
from pathlib import Path
import shutil

from PIL import Image


def resize_image(input_path: str, output_path: str, max_height: int, max_width: int):
    original_image = Image.open(input_path)
    print(f"Original size : {original_image.size}")

    width = original_image.size[0]
    height = original_image.size[1]
    aspect_ratio = width / height

    resized_ratio = (math.floor(max_height * aspect_ratio), max_height)

    print(f"Aspect Ratio {aspect_ratio}, resized ratio {resized_ratio}")

    resized = original_image.resize(resized_ratio)
    resized.save(output_path)


def reduce_image_size(input_path: str, output_path: str, max_size_bytes: int):
    # If under max size, copying is the end
    shutil.copyfile(input_path, output_path)

    output_file_path = Path(output_path)
    current_size = output_file_path.stat().st_size

    # Otherwise keep reducing the quality until the max size is under the size limit
    current_quality = 99
    while current_size >= max_size_bytes:
        input_image = Image.open(input_path)
        input_image.save(output_path, optimize=True, quality=current_quality)
        current_quality -= 1
        current_size = output_file_path.stat().st_size
        print(f"Image size now: {current_size} at quality {current_quality}")


if __name__ == '__main__':
    INPUT_PATH = 'ute.jpg'
    OUPUT_PATH = 'processed.jpeg'
    resize_image(input_path=INPUT_PATH, output_path='resized.jpeg', max_height=699, max_width=699)
    reduce_image_size(input_path='resized.jpeg', output_path=OUPUT_PATH, max_size_bytes=99 * 1024)
