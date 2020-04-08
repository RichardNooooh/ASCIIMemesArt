from typing import Tuple

from PIL import Image, ImageFont, ImageDraw, ImageMath
import string


# from https://stackoverflow.com/questions/24085996/how-i-can-load-a-font-file-with-pil-imagefont-truetype-without-specifying-the-ab


# sample text and font
# unicode_text = u"t"
# font = ImageFont.truetype("Open_Sans/OpenSans-Regular.ttf", 28, encoding="unic")

# get the line size
# text_width, text_height = font.getsize(unicode_text)

# create a blank canvas with extra space between lines
# canvas = Image.new('RGB', (text_width, text_height+1), "white")

# draw the text onto the text canvas, and use black as the text color
# draw = ImageDraw.Draw(canvas)
# draw.text((0, 0), unicode_text, 'black', font)

# save the blank canvas to a file
# canvas.save("images/test.png", "PNG")
# canvas.show()

# each pixel should be either completely black or white, so I just need to count the black pixels
def density_of_letter(im: Image, size: Tuple[int]) -> float:
    x, y = size
    black_pixel_count = 0
    for i in range(x):
        for j in range(y):
            pixel = im.getpixel((i, j))
            if 0 in pixel:
                black_pixel_count += 1

    return black_pixel_count / (x * y)


font = ImageFont.truetype("Open_Sans/OpenSans-Regular.ttf", 35, encoding="unic")
size = (50, 50)

for letter in string.ascii_lowercase:
    # text_width, text_height = font.getsize(letter)
    canvas_letter = Image.new('RGB', size, "white")
    draw_letter = ImageDraw.Draw(canvas_letter)
    draw_letter.text((0, 0), letter, 'black', font)
    dens = density_of_letter(canvas_letter, size)
    print(letter + " : " + str(dens))

canvas_letter.show()