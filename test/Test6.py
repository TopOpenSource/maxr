import numpy
import numpy as np

img1 = np.zeros((3, 4), dtype='int32')
img1[0][0] = 1
img1[0][3] = 1
img1[1][2] = 1
img1[1][3] = -501
img1[2][2] = 1
img1[2][3] = -501

img2 = np.zeros((3, 4), dtype='int32')
img2[0][0] = 2
img2[0][3] = 1
img2[1][2] = 2
img2[1][3] = -501
img2[2][2] = 1
img1[2][3] = -501


from utils.DcmUtil3 import *

DcmUtil.comp_test(img2,img1)
