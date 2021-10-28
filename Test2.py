import numpy as np
import pydicom

from utils.DcmUtil import DcmUtil

#image_SCT = pydicom.dcmread("D:\\test_data\\0134606885310576\\CT\\0.dcm")

image_SCT=DcmUtil.get_pixels_hu(pydicom.dcmread("D:\\test_data\\0134606885310576\\CT\\55.dcm"))

#查看矩阵形状
print(image_SCT.shape)

#矩阵中的最小值
min_index_CBCT =np.unravel_index(np.argmin(image_SCT, axis=None), image_SCT.shape)
#最小值的坐标位置
print(min_index_CBCT)
#矩阵中的最小值
print(image_SCT[min_index_CBCT])

#矩阵中的最大值
max_index_CBCT =np.unravel_index(np.argmax(image_SCT, axis=None), image_SCT.shape)
#最大值的坐标位置
print(max_index_CBCT)
#矩阵中的最大值
print(image_SCT[max_index_CBCT])

#查询具体数据
'''
for i in range(0, 511):
    for j in range(0, 511):
        print(str(image_SCT[i][j])+",",end="")
    print("")
'''

