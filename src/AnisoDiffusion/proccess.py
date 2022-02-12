from PyQt5.QtWidgets import QTreeWidgetItem

from skimage.filters import gaussian
from AnisoDiffusion.difussion import ad_step_time_slic
from AnisoDiffusion.images import get_name, read_image, save_image, edge_image

def proccess_image(param, path, self):
    
    name = get_name(path)
    self.LoadImage(name)
    
    i = 0
    while name in self.imageList:
        i += 1
        name = f'{name}({i})'
    
    self.imageParent[name] = name
    self.imageList[name] = QTreeWidgetItem(self.treeWidget, [name])

    image = read_image(path)
    image_edge = edge_image(image, param[-1])
    
    save_image(image, name)
    save_image(image_edge, f'{name}_edge')
    
    imageGauss = gaussian(image, sigma=param[-3])
    ad_step_time_slic(imageGauss, name, param, self)

    self.statBar.showMessage(f'', 0)