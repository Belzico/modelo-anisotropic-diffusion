import collections

from cmath import sqrt
from Diffusion.kmmc import kmmc2
from pylab import zeros, exp, sqrt
from skimage.segmentation import slic

def in_range(x, y, img):
    return -1 < x < img.shape[0] and -1 < y < img.shape[1]

def segm_coef_1(img, db=0.1, bf=0.05, num_seg=15):
    labels = slic(img, num_seg, multichannel=False, start_label=1)
    matrix_coef = zeros(img.shape)
    process = zeros(img.shape, dtype=bool)
    extGlobals = kmmc2(img, onlyKm=True)
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            if not process[x, y]:
                superpixel = bfs_cluster(img, process, labels, (x, y), labels[x, y])
                k = kmmc2(img, db, bf, superpixel=superpixel, extGlobal=extGlobals)
                for i in range(len(superpixel)):
                    pos = superpixel[i]
                    matrix_coef[pos] = 1 / (1 + (img[pos]/(k))**2) if k != 0 else 0
    return matrix_coef

def segm_coef_2(img, db=0.1, bf=0.05, num_seg=15):
    labels = slic(img, num_seg, multichannel=False, start_label=1)
    matrix_coef = zeros(img.shape)
    process = zeros(img.shape, dtype=bool)
    extGlobals = kmmc2(img, onlyKm=True)
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            if not process[x, y]:
                superpixel = bfs_cluster(img, process, labels, (x, y), labels[x, y])
                k = kmmc2(img, db, bf, superpixel=superpixel, extGlobal=extGlobals)
                for i in range(len(superpixel)):
                    pos = superpixel[i]
                    matrix_coef[pos] = -((img[pos] / k))**2 if k != 0 else 0
    matrix_coef = exp(matrix_coef)    
    return matrix_coef

def segm_coef_3(img, db=0.1, bf=0.05, num_seg=15):
    labels = slic(img, num_seg, multichannel=False, start_label=1)
    matrix_coef = zeros(img.shape)
    process = zeros(img.shape, dtype=bool)
    extGlobals = kmmc2(img, onlyKm=True)
    if len(extGlobals) != 2: return None
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            if not process[x, y]:
                superpixel = bfs_cluster(img, process, labels, (x, y), labels[x, y])
                k = kmmc2(img, db, bf, superpixel=superpixel, extGlobal=extGlobals)
                k2 = sqrt(2*k)
                for i in range(len(superpixel)):
                    pos = superpixel[i]
                    if img[pos] <= 0: matrix_coef[pos] = 1
                    else:
                        matrix_coef[pos] =1- exp(-2.33/(img[pos]/k)**2) if k != 0 else 0
    return matrix_coef

def segm_coef_4(img, db=0.1, bf=0.05, num_seg=15):
    labels = slic(img, num_seg, multichannel=False, start_label=1)
    matrix_coef = zeros(img.shape)
    process = zeros(img.shape, dtype=bool)
    extGlobals = kmmc2(img, onlyKm=True)
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            if not process[x, y]:
                superpixel = bfs_cluster(img, process, labels, (x, y), labels[x, y])
                k = kmmc2(img, db, bf, superpixel=superpixel, extGlobal=extGlobals)
                for i in range(len(superpixel)):
                    pos = superpixel[i]
                    matrix_coef[pos] = 1/(sqrt(1+(img[pos]/k)**2)) if k != 0 else 0   
    return matrix_coef

dirX = [0, 1, 0, -1]
dirY = [-1, 0, 1, 0]

def bfs_cluster(img, process, labels, pos, num_lbl):
    superpixel = []
    queue = collections.deque()
    queue.append(pos)
    process[pos] = True
    while len(queue) != 0:
        current = queue.popleft()
        for i in range(0, 4):
            adyX = current[0] + dirX[i]
            adyY = current[1] + dirY[i]
            if in_range(adyX, adyY, img) and not process[adyX, adyY] and labels[adyX, adyY] == num_lbl:
                queue.append((adyX, adyY))
                process[adyX, adyY] = True
        superpixel.append(current)

    return superpixel