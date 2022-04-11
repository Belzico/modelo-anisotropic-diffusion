import cv2
import numpy as np

from PIL import Image
from skimage.feature import canny
from matplotlib.pyplot import gray, imsave
from skimage.filters.edges import scharr, sobel

def get_name(path):
    return path.split('/')[-1][:-4]

def read_image(path):
    img = np.array(Image.open(path).convert('L'), dtype='float64')
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
    elif edge_type == 'Laplace':
        laplace = cv2.Laplacian(image, cv2.CV_64F)
        edge = np.uint8(np.absolute(laplace))
    else:
        edge = canny(image, 0)

    gray()
    return edge