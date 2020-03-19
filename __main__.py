from PIL import Image

im = Image.open("images/weeb.jpg")
pixel = im.load()

width, height = im.size

for x in range(width):
    for y in range(height):
        print(str(pixel[x, y]) + " ", end="")
    print()
