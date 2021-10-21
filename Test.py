import os
import pydicom
from utils.DcmUtil import DcmUtil
from utils.ExcelUtil import ExcelUtil

# DcmUtil.test()

'''
1 设置患者目录

2.遍历CT的目录文件 
  2-1 获取 CT的像素值
  2-2 获取 CBCT对应的像素值
  2-3 获取 SCT对应的像素值

'''

# 患者目录
patientPath = "D:\\test_data\\0134606885310576"

excel = ExcelUtil()
sheet_name = '0134606885310576'
excel.create_sheet(sheet_name)

patientCTPath = patientPath + "\\CT"
patientCBCTPath = patientPath + "\\CBCT"
patientSCTPath = patientPath + "\\SCT"

for root, dirs, files in os.walk(patientCTPath):

    for index, file in enumerate(files):
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

        index=index+1
        excel.insert_data(sheet_name, index, 1, index)

        excel.insert_data(sheet_name, index, 2, mae_CBCT)
        excel.insert_data(sheet_name, index, 3, mae_SCT)

        excel.insert_data(sheet_name, index, 4, mse_CBCT)
        excel.insert_data(sheet_name, index, 5, mse_SCT)

        excel.insert_data(sheet_name, index, 6, rmse_CBCT)
        excel.insert_data(sheet_name, index, 7, rmse_SCT)

        excel.insert_data(sheet_name, index, 8, psnr_CBCT)
        excel.insert_data(sheet_name, index, 9, psnr_SCT)

excel.save("D://a.xls")