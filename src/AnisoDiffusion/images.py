from PIL import Image
from numpy import save
from pylab import array, gray, imsave
from skimage.feature import canny
from skimage.filters.edges import scharr, sobel

def get_name(path):
    return path.split('/')[-1][:-4]

def read_image(path):
    img = array(Image.open(path).convert('L'), dtype='float64')
    gray()
    return img

def save_image(image, name, path='./.temp'):
    gray()
    imsave(f'{path}/{name}.jpg', image)

def edge_image(image, edge_type):
    if edge_type == 'Scharr':
        edge = abs(scharr(image))
    elif edge_type == 'Canny':
        edge = abs(sobel(image))
    else:
        edge = canny(image, 0)

    gray()
    return edge