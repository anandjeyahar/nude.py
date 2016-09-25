# Straight from http://blog.iconfinder.com/detecting-duplicate-images-using-python/
def perceptual_hash(image, hash_size = (9,9)):
    from skimage.color import rgb2gray
    from skimage.transform import resize
    # Grayscale and shrink the image in one step.
    #image = image.convert('L').resize(
    #    (hash_size[0], hash_size[1]),
    #    Image.ANTIALIAS,
    #)
    image1 = resize(image, (hash_size[0], hash_size[1]))
    import pdb; pdb.set_trace()  # XXX BREAKPOINT

    pixels = list(image1.getdata())

    # Compare adjacent pixels.
    difference = []
    for row in xrange(hash_size[1]):
        for col in xrange(hash_size[0]):
            pixel_left = image1.getpixel((col, row))
            pixel_right = image1.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)

    # Convert the binary array to a hexadecimal string.
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2**(index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return ''.join(hex_string)
