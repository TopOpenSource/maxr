import os
import numpy as np
import pydicom
import matplotlib.pyplot as plt
from utils.DcmUtil import DcmUtil

# DcmUtil.test()

'''
1 设置患者目录

2.遍历CT的目录文件 
  2-1 获取 CT的像素值
  2-2 获取 CBCT对应的像素值
  2-3 获取 SCT对应的像素值

'''

# 患者目录
patientPath = "D:\\test_data\\test_data\\0134606885310576"

patientCTPath = patientPath + "\\CT"
patientCBCTPath = patientPath + "\\CBCT"
patientSCTPath = patientPath + "\\SCT"

for root, dirs, files in os.walk(patientCTPath):
    for file in files:
        # 获取文件名
        fileName = file.split(".dcm")[0]
        # 根据文件名获取 CBCT CT SCT对应的文件
        fileCBCT = patientCBCTPath + "\\I" + fileName
        fileCT = patientCTPath + "\\" + fileName + ".dcm"
        fileSCT = patientSCTPath + "\\" + fileName + ".dcm"

        image_CBCT = pydicom.dcmread(fileCBCT).pixel_array
        image_CT = pydicom.dcmread(fileCT).pixel_array
        image_SCT = pydicom.dcmread(fileSCT).pixel_array

        mae_CBCT = DcmUtil.mae(image_CT, image_CBCT)
        mae_SCT = DcmUtil.mae(image_CT, image_SCT)

        mse_CBCT = DcmUtil.mse(image_CT, image_CBCT)
        mse_SCT = DcmUtil.mse(image_CT, image_SCT)

        rmse_CBCT = DcmUtil.rmse(image_CT, image_CBCT)
        rmse_SCT = DcmUtil.rmse(image_CT, image_SCT)

        psnr_CBCT = DcmUtil.psnr(image_CT, image_CBCT, 512)
        psnr_SCT = DcmUtil.psnr(image_CT, image_SCT, 512)

