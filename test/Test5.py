import numpy
import numpy as np

img1 = np.zeros((5, 6), dtype='int32')
img1[2][1] = 1
img1[3][1] = 1
img1[0][2] = 1
img1[2][4] = 1

img2 = np.zeros((5, 6), dtype='int32')
img2[0][0] = 1

img3 = np.zeros((5, 6), dtype='int32')
img2[0][1] = 1

com = np.maximum(img1, img2,img3)
#print(com)

#print(img1)
notNul = np.argwhere(img1 > 0)
#print(notNul)
#print(notNul.min(axis=0))
#print(notNul.max(axis=0))

#print(com[0:2,0:2])

def clear_border(image1, image2, image3):
    '''
    1: 三张图片合并，每个坐标取最大值
    2: 过滤 >-500的坐标
    3：获取 最小坐标   最大坐标
    4：截取 最小坐标-最大坐标之间的值
    '''
    image = np.maximum(image1, image2, image3)

    image = np.argwhere(image > -500)


    min_grid = image.min(axis=0)
    max_grid = image.max(axis=0)


    return image1[min_grid[0]:max_grid[0] + 1, min_grid[1]:max_grid[1] + 1]\
        ,image2[min_grid[0]:max_grid[0] + 1, min_grid[1]:max_grid[1] + 1]\
        ,image3[min_grid[0]:max_grid[0] + 1, min_grid[1]:max_grid[1] + 1]

image1=numpy.full((512, 512),-1000, dtype='int32')
image1[2][2]=501
image1[4][2]=501

image2=numpy.full((512, 512),-1000, dtype='int32')
image2[1][1]=501
image2[2][3]=501

image3=numpy.full((512, 512),-1000, dtype='int32')
image3[2][1]=501
image3[4][3]=501


i1,i2,i3=clear_border(image1,image2,image3)
#print(i3)
#print(i3.shape)