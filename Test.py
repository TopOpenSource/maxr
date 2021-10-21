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
def copPatientPath(excel,sheet_name,path,patientId):

    # 患者目录
    patientPath = path+"\\"+patientId

    excel.create_sheet(sheet_name)

    patientCTPath = patientPath + "\\CT"
    patientCBCTPath = patientPath + "\\CBCT"
    patientSCTPath = patientPath + "\\SCT"

    # 插入excel头
    excel.insert_line_date(sheet_name, 1, ('序号', 'mae_CBCT', 'mae_SCT', 'mse_CBCT', 'mse_SCT', 'rmse_CBCT', 'rmse_SCT', 'psnr_CBCT', 'psnr_SCT'))

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
            # 计算
            vols = DcmUtil.comp(index, image_CBCT, image_CT, image_SCT, 255)
            # 插入excel
            excel.insert_line_date(sheet_name, index + 2, vols)

excel = ExcelUtil()
copPatientPath(excel,"0134606885310576","D:\\test_data","0134606885310576")
excel.save("D://d.xls")