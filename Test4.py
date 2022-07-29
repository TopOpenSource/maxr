import os

from utils.DcmUtil3 import DcmUtil
import matplotlib.pyplot as plt

def copPatientPath(path, patientId):
    # 患者目录
    patientPath = path + "\\" + patientId


    patientCTPath = patientPath + "\\CT"
    patientCBCTPath = patientPath + "\\CBCT"
    patientSCTPath = patientPath + "\\SCT"


    # 按照方向排序切片

    slices_CT = DcmUtil.sortSlices(patientCTPath)
    slices_CBCT = DcmUtil.sortSlices(patientCBCTPath)
    slices_SCT = DcmUtil.sortSlices(patientSCTPath)

    for i in range(0,len(slices_CT)):

        image_CBCT = DcmUtil.get_pixels_hu(slices_CBCT[i])
        image_CT = DcmUtil.get_pixels_hu(slices_CT[i])
        image_SCT = DcmUtil.get_pixels_hu(slices_SCT[i])

        # 计算
        index, r_CBCT, r_SCT = DcmUtil.reduce_img(i, image_CBCT, image_CT, image_SCT)

        saveImage(r_CBCT,patientCBCTPath+"_reduct\\"+str(i)+".png")
        saveImage(r_SCT, patientSCTPath + "_reduct\\" + str(i) + ".png")


def saveImage(data,savePath):
    plt.imshow(data, interpolation='nearest', cmap='bwr', origin='lower', vmin=-2000, vmax=2000)

    plt.colorbar(shrink=.92)

    plt.xticks(())
    plt.yticks(())
    plt.savefig(savePath)
    plt.close("all")


rootPath = "D:\\test_data"

for file in os.listdir(rootPath):
    copPatientPath(rootPath, file)