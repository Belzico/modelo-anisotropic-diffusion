from Diffusion.coefficent import *
from PyQt5.QtWidgets import QTreeWidgetItem
from Diffusion.images import edge_image, save_image

def derivate(direction, image):
    res = image.copy()
    if direction == 'n':
        res[:, :-1] -= image[:, 1:]
    elif direction == 'w':
        res[:-1, :] -= image[1:, :]
    elif direction == 's':
        res[:, 1:] -= image[:, :-1]
    elif direction == 'e':
        res[1:, :] -= image[:-1, :]
    return res

def ad_step_time_slic(image, name, param, self):
    t, db, bf, num_seg, sigam, coeff, edge = param
    
    for i in range(t):
        self.statBar.showMessage(f'Processing image: "{name} for t={i+1}"', 0)

        dN = derivate('n', image)
        cN = segm_coef(dN, db, bf, num_seg, coeff)

        dW = derivate('w', image)
        cW = segm_coef(dW, db, bf, num_seg, coeff)

        dS = derivate('s', image)
        cS = segm_coef(dS, db, bf, num_seg, coeff)

        dE = derivate('e', image)
        cE = segm_coef(dE, db, bf, num_seg, coeff)

        image = image + ((cN*dN + cW*dW + cS*dS + cE*dE)*0.25)
        
        image_diff_edge = edge_image(image, param[-1])
        
        new_name = f'{name}_{i+1}'
        self.imageParent[new_name] = name
        save_image(image_diff_edge, f'{new_name}_diff')
        save_image(image_diff_edge, f'{new_name}_edge_diff')
        self.imageList[new_name] = QTreeWidgetItem(self.imageList[name], [new_name])

def segm_coef(dir, db, bf, num_seg, coef_type):
    if coef_type == 'Perona and Malik I':
        return segm_coef_1(dir, db, bf, num_seg)
    elif coef_type == 'Perona and Malik II':
        return segm_coef_2(dir, db, bf, num_seg)
    elif coef_type == 'Weickert':
        segm = segm_coef_3(dir, db, bf, num_seg)
        if segm is not None: return segm
        else: return None
    else:
        return segm_coef_4(dir, db, bf, num_seg)