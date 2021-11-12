import numpy as np


def mse(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    return mse

img1 = np.zeros((512, 512), dtype='int32')
img1[511][511]=2
#img1[510][510]=-1000



img2 = np.zeros((512, 512), dtype='int32')
img2[511][511]=100
#img2[510][510]=-1000
print(mse(img1,img2))