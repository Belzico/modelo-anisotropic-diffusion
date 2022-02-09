from AnisoDiffusion.coefficent import segm_coef

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

def ad_step_time_slic(image, edgeimage, param):
    t, db, bf, num_seg, h, sigam, edge = param
    
    for i in range(t):

        dN = derivate('n', image)
        cN = segm_coef(dN, db, bf, num_seg)

        dW = derivate('w', image)
        cW = segm_coef(dW, db, bf, num_seg)

        dS = derivate('s', image)
        cS = segm_coef(dS, db, bf, num_seg)

        dE = derivate('e', image)
        cE = segm_coef(dE, db, bf, num_seg)

        image = image + ((cN*dN + cW*dW + cS*dS + cE*dE)*h)
    
    return image        