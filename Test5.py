import os

import pandas as  pd
from utils.DcmUtil3 import DcmUtil
from utils.ExcelUtil import ExcelUtil


def genExcel(patientPath,paramName):
    #创建excel
    writer = pd.ExcelWriter(patientPath+"\\"+paramName+".xlsx",engine='openpyxl')
    #按照方向排序切片
    slices = DcmUtil.sortSlices(patientPath+"\\"+paramName)
    #遍历切片len(slices)
    for i in range(0,len(slices)):
       sheet_name=str(i)
       image_CT = DcmUtil.get_pixels_hu(slices[i])
       pd_data = pd.DataFrame(image_CT)
       #保存矩阵
       pd_data.to_excel(writer, sheet_name, index=False)

    writer.save()
    pass


def genReduce(patientPath, leftParamName,rightParamName):
    # 创建excel
    writer = pd.ExcelWriter(patientPath + "\\" + leftParamName+"_"+rightParamName+ ".xlsx", engine='openpyxl')
    # 按照方向排序切片
    slices_left = DcmUtil.sortSlices(patientPath + "\\" + leftParamName)
    slices_right = DcmUtil.sortSlices(patientPath + "\\" + rightParamName)
    # 遍历切片 len(slices_left)
    for i in range(0,len(slices_left)):
        sheet_name = str(i)
        image_left = DcmUtil.get_pixels_hu(slices_left[i])
        image_right = DcmUtil.get_pixels_hu(slices_right[i])

        pd_data = pd.DataFrame(DcmUtil.reduce(image_left,image_right))
        pd_data.to_excel(writer, sheet_name, index=False)

    writer.save()
    pass

def execPatient(rootPath,patientId):
    patientPath=rootPath + "\\" + patientId
    #生成CT
    genExcel(patientPath,"CT")
    #生成CBCT
    genExcel(patientPath, "CBCT")
    #生成SCT
    genExcel(patientPath, "SCT")
    #生成CBCT-CT
    genReduce(patientPath,"CBCT","CT")
    #生成SCT-CT
    genReduce(patientPath,"SCT","CT")
    pass

rootPath = "D:\\test_data"
#遍历病人
for file in os.listdir(rootPath):
    execPatient(rootPath,file)



