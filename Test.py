import os

import numpy as np
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


def copPatientPath(excel, sheet_name, path, patientId):
    # 患者目录
    patientPath = path + "\\" + patientId
    excel.create_sheet(sheet_name)

    patientCTPath = patientPath + "\\CT"
    patientCBCTPath = patientPath + "\\CBCT"
    patientSCTPath = patientPath + "\\SCT"

    # 插入excel头
    excel.insert_line_date(sheet_name, 1, (
    '序号', 'mae_CBCT', 'mae_SCT', 'mse_CBCT', 'mse_SCT', 'rmse_CBCT', 'rmse_SCT', 'psnr_CBCT', 'psnr_SCT'))

    # 按照文件名排序
    for _, _, files_CT in os.walk(patientCTPath):
        files_CT.sort(key=lambda x: int(x[:-4]))
    for _, _, files_CBCT in os.walk(patientCBCTPath):
        files_CBCT.sort(key=lambda x: int(x[1:]))
    for _, _, files_SCT in os.walk(patientSCTPath):
        files_SCT.sort(key=lambda x: int(x[:-4]))

    for i in range(0, len(files_CT)):
        fileCBCT = patientCBCTPath + "\\" + files_CBCT[i]
        fileCT = patientCTPath + "\\" + files_CT[i]
        fileSCT = patientSCTPath + "\\" + files_SCT[i]

        image_CBCT = pydicom.dcmread(fileCBCT).pixel_array
        image_CT = pydicom.dcmread(fileCT).pixel_array
        image_SCT = pydicom.dcmread(fileSCT).pixel_array

        max_index_CBCT =np.unravel_index(np.argmin(image_CBCT, axis=None), image_CBCT.shape)
        print(image_CBCT[max_index_CBCT])

        max_index_CT = np.unravel_index(np.argmin(image_CT, axis=None), image_CT.shape)
        print(image_CT[max_index_CT])

        max_index_SCT = np.unravel_index(np.argmin(image_SCT, axis=None), image_SCT.shape)
        print(image_SCT[max_index_SCT])


        # 计算
        vols = DcmUtil.comp(i, image_CBCT, image_CT, image_SCT, 255)
        # 插入excel
        excel.insert_line_date(sheet_name, i + 2, vols)


excel = ExcelUtil()
rootPath = "D:\\test_data"

for file in os.listdir(rootPath):
    copPatientPath(excel, file, rootPath, file)

excel.save("D://c.xls")
