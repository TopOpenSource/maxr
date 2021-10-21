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


def copPatientPath(excel, sheet_name, path, patientId):
    # 患者目录
    patientPath = path + "\\" + patientId

    excel.create_sheet(sheet_name)

    patientCTPath = patientPath + "\\CT"
    patientCBCTPath = patientPath + "\\CBCT"
    patientSCTPath = patientPath + "\\SCT"

    # 插入excel头
    excel.insert_line_date(sheet_name
                           , 1
                           , ('序号', 'mae_CBCT', 'mae_SCT', 'mse_CBCT', 'mse_SCT', 'rmse_CBCT', 'rmse_SCT', 'psnr_CBCT',
                              'psnr_SCT'))

    files_CT = os.listdir(patientCTPath)
    files_CBCT = os.listdir(patientCBCTPath)
    files_SCT = os.listdir(patientSCTPath)

    print(files_CT)

excel = ExcelUtil()
copPatientPath(excel, "0134606885310576", "D:\\test_data", "0134606885310576")
# excel.save("D://d.xls")
