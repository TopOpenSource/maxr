import numpy
import numpy as np


img1 = np.zeros((5, 6), dtype='int32')
img1[2][1] = 1
img1[3][1] = 1
img1[0][2] = 1
img1[2][4] = 1


img2 = np.zeros((5, 6), dtype='int32')
img2[2][1] = 2
img2[3][1] = 2
img2[0][2] = 2
img2[2][4] = 2


image = np.argwhere(img1 ==0)
print(image)
zeros=len(image)
for i in image:
    img1[i[0]][i[1]]=0
print(img1)

print(img1.size)

print(numpy.sum((img1 - img2) ** 2)/(img1.size-len(image)))
print( np.mean((img1 - img2) ** 2))
