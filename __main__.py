import math

from PIL import Image

im = Image.open("images/weeb.jpg")
pixel = im.load()

width, height = im.size

output_string = ""

for x in range(width):
    for y in range(height):
        r, g, b = pixel[y, x]
        brightness = math.sqrt(0.299 * r **2 + 0.587 * g ** 2 + 0.114 * b ** 2)
        asciiMap = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
        ind = brightness * 70 // 256
        output_string += asciiMap[int(ind)]

    output_string += "\n"

print(output_string)

