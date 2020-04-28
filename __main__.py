import math
from font_sort import FontSort

from PIL import Image

im = Image.open("images/weeb.jpg")
pixel = im.load()

width, height = im.size

output_string = ""

mapping_string = " .'`^\",:;Il!i~+_-?1|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ft = FontSort("Open_Sans/OpenSans-Regular.ttf", mapping_string)
asciiMap = ft.get_reversed_font_dict()

for y in range(height):
    for x in range(width):
        pixel_tuple = pixel[x, y]
        if len(pixel_tuple) > 3:
            r, g, b, a = pixel_tuple
            r *= a / 255
            g *= a / 255
            b *= a / 255
        else:
            r, g, b = pixel_tuple

        brightness = math.sqrt(0.299 * r ** 2 + 0.587 * g ** 2 + 0.114 * b ** 2)
        ind = brightness * len(mapping_string) // 256
        output_string += asciiMap[int(ind)][0]

    output_string += "\n"

print(output_string)

