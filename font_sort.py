from PIL import Image
from PIL import ImageFont, ImageDraw
from PIL import ImageMath

font = ImageFont.truetype("Open_Sans/OpenSans-Regular.ttf")
mask = font.getmask('a')
# draw = ImageDraw.Draw()

size = 50, 50
blank = Image.new('L', size, 256)  # not sure what value is needed for pure white
blank.save("images/test.png")

#
# s = 0
# ImageMath.eval("sum += int(a), 'L'", sum = s, a = mask)

# print(mask)
# mask.save("images/a.jpg")
