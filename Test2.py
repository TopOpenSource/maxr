import os

import numpy as np
import pydicom
from utils.DcmUtil2 import DcmUtil
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

    # 按照方向排序切片
    slices_CT = DcmUtil.sortSlices(patientCTPath)
    slices_CBCT = DcmUtil.sortSlices(patientCBCTPath)
    slices_SCT = DcmUtil.sortSlices(patientSCTPath)

    for i in range(0, len(slices_CT)):
        image_CBCT = DcmUtil.get_pixels_hu(slices_CBCT[i])
        image_CT = DcmUtil.get_pixels_hu(slices_CT[i])
        image_SCT = DcmUtil.get_pixels_hu(slices_SCT[i])

        # 计算
        vols = DcmUtil.comp(i, image_CBCT, image_CT, image_SCT, 255)
        # 插入excel
        excel.insert_line_date(sheet_name, i + 2, vols)


excel = ExcelUtil()
rootPath = "D:\\test_data"

for file in os.listdir(rootPath):
    copPatientPath(excel, file, rootPath, file)

excel.save("D://c.xls")

