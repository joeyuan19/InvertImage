from PIL import Image
import numpy as np


def pixelate(img,pixel_size=5):
    X,Y = img.size
    data = np.array(img)
    for x in range(X):
        for y in range(Y):
            for j in range(3):
                data[y][x][j] = 255 - data[y][x][j]
    img = Image.fromarray(data)
    return img 

if __name__ == '__main__':
    import sys
    from optparse import OptionParser
    parser = OptionParser()
    opts,args = parser.parse_args()
    if len(args) <= 0:
        print("No image provided")
        sys.exit(1)
    img = Image.open(args[0])
    img = pixelate(img)
    img.save('out.png')
