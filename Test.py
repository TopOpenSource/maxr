import os

import pydicom
import matplotlib.pyplot as plt
from utils.DcmUtil import DcmUtil

DcmUtil.test()

'''
1 设置患者目录

2.遍历CT的目录文件 
  2-1 获取 CT的像素值
  2-2 获取 CBCT对应的像素值
  2-3 获取 SCT对应的像素值

'''

#患者目录
patientPath = "D:\\test_data\\test_data\\0134606885310576"


patientCTPath = patientPath + "\\CT"
patientCBCTPath = patientPath + "\\CBCT"
patientSCTPath = patientPath + "\\SCT"


for root, dirs, files in os.walk(patientCTPath):

    for file in files:
        #获取文件名
        fileName = file.split(".dcm")[0]
        #根据文件名获取 CBCT CT SCT对应的文件
        fileCBCT = patientCBCTPath + "\\I" + fileName
        fileCT = patientCTPath + "\\" + fileName + ".dcm"
        fileSCT = patientSCTPath + "\\" + fileName + ".dcm"

        imageCBCT = pydicom.dcmread(fileCBCT).pixel_array
        imageCT = pydicom.dcmread(fileCT).pixel_array
        imageSCT = pydicom.dcmread(fileSCT).pixel_array


'''
dcm = pydicom.dcmread("D:\\test_data\\test_data\\0134606885310576\\CT\\1.dcm")
img_arr = dcm.pixel_array

dcm1 = pydicom.dcmread("D:\\test_data\\test_data\\0134606885310576\\CBCT\\I0")
img_arr1=dcm1.pixel_array
'''
