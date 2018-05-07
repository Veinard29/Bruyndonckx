from PIL import Image


im = Image.open('Mercedes.jpg')
print(im.size)
sizes = im.size
sizeX = sizes[0]
sizeY = sizes[1]
elem_size = 8
for i in range(sizeX // elem_size):
    for j in range(sizeY // elem_size):
        box = (i * elem_size, j * elem_size, (i+1) * elem_size, (j+1) * elem_size)
        region = im.crop(box)
        outfile = 'Blocks8x8/{}-{}.jpeg'.format(i, j)
        region.save(outfile, "JPEG")





