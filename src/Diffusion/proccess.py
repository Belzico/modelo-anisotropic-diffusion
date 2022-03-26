from skimage.filters import gaussian
from Diffusion.difussion import ad_step_time_slic
from Diffusion.images import save_image, edge_image

def proccess_image(image, param, self):
    self.countProcc += 1
    edge = edge_image(image, param[-1])
    save_image(edge, f'{self.name}_edge')
    
    imageGauss = gaussian(image, sigma=param[-3])
    ad_step_time_slic(imageGauss, self.name, param, self)
    self.countProcc -= 1