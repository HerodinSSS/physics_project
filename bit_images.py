from PIL import Image, ImageDraw, ImageFont

img = Image.open("image/path")
# img.show() # Show the images that you have chosen
WIDTH, HEIGHT = 10000, 10000 #image size

# Set the font and size for the bits
font = ImageFont.truetype("font", 20)
cell_width, cell_height = 20, 20

# Resizing the image 
img = img.resize((int(WIDTH / cell_width), int(HEIGHT / cell_height)), Image.Resampling.NEAREST)
new_width, new_height = img.size
img = img.load()

# Reading the image colors
new_img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
d = ImageDraw.Draw(new_img)


# Creating images
for i in range(new_height):
    for j in range(new_width):
        r, g, b = img[j, i]
#         r, g, b, a = img[j, i] # use this line if you have an image with alpha value
        k = int((r + g + b) / 3)
        if k < 128:
            text = "1"
        else:
            text = "0"
        d.text((j * cell_width, i * cell_height), text=text, font=font, fill=(0, g, 0))

new_img.show()
##new_img.save("Keanu_0_1.png")-