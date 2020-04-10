from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img2 = img.convert('L')
# crooked = filtered_img2.rotate(90)
# crooked.save("grey.png", 'png')
# crooked.show()

img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')

print(img.size)
