from PIL import Image
from numpy import save
from pylab import array, gray, imsave
from skimage.feature import canny
from skimage.filters.edges import scharr, sobel
from skimage.filters import gaussian

from AnisoDiffusion.difussion import ad_step_time_slic

def get_name(path):
    return path.split('/')[-1][:-4]

def read_image(path):
    img = array(Image.open(path).convert('L'), dtype='float64')
    gray()
    return img

def save_image(image, name, path='./.temp'):
    gray()
    imsave(f'{path}/{name}.jpg', image)

def proccess_image(param, path):
    
    name = get_name(path)

    image = read_image(path)
    image_edge = edge_image(image, param[-1])
    imageGauss = gaussian(image, sigma=param[-2])
    image_diff = ad_step_time_slic(imageGauss, image_edge, param)
    image_edge = edge_image(image_diff, param[-1])

    save_image(image, name)
    save_image(image_edge, f'{name}_edge')
    save_image(image_diff, f'{name}_diff')

    return name

def edge_image(image, edge_type):
    if edge_type == 'Scharr':
        edge = abs(scharr(image))
    elif edge_type == 'Canny':
        edge = abs(sobel(image))
    else:
        edge = canny(image, 0)

    gray()
    return edge