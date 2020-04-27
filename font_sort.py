from typing import Tuple

from PIL import Image, ImageFont, ImageDraw
import string

def density_of_letter(im: Image, size: Tuple[int]) -> float:
    x, y = size
    black_pixel_count = 0
    for i in range(x):
        for j in range(y):
            pixel = im.getpixel((i, j))
            if pixel == 0:
                black_pixel_count += 1

    return black_pixel_count / (x * y)


class FontSort:

    def __init__(self, font_filename: str):
        self.font_filename = font_filename
        self.font_dict = {}

    def find_densities(self):
        font = ImageFont.truetype(self.font_filename, 35, encoding="unic")
        size = (50, 50)

        for letter in string.ascii_lowercase:
            canvas_letter = Image.new('L', size, "white")
            draw_letter = ImageDraw.Draw(canvas_letter)
            draw_letter.text((0, 0), letter, 'black', font)
            dens = density_of_letter(canvas_letter, size)
            self.font_dict[letter] = dens

    def get_font_dict(self):
        return self.font_dict
