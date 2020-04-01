from PIL import Image
from PIL import ImageFont, ImageDraw

# sample text and font
unicode_text = u"A"
font = ImageFont.truetype("Open_Sans/OpenSans-Regular.ttf", 28, encoding="unic")

# get the line size
text_width, text_height = font.getsize(unicode_text)

# create a blank canvas with extra space between lines
canvas = Image.new('RGB', (text_width, text_height+1), "white")

# draw the text onto the text canvas, and use black as the text color
draw = ImageDraw.Draw(canvas)
draw.text((0, 0), unicode_text, 'black', font)

# save the blank canvas to a file
canvas.save("images/test.png", "PNG")
# canvas.show()