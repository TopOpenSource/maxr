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

#DcmUtil.comp_test(img2,img1)



img3 = np.zeros((2, 2), dtype='int32')
img4 = np.zeros((2, 2), dtype='int32')

img3[0][0] = 1
img3[0][1] = 3
img3[1][0] = 3
img3[1][1] = 1

img4[0][0] = 2
img4[0][1] = 2
img4[1][0] = 2
img4[1][1] = 2

print(DcmUtil.reduce(img4,img3))