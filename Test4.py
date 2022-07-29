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

    for i in range(0, 10):
        image_CBCT = DcmUtil.get_pixels_hu(slices_CBCT[i])
        image_CT = DcmUtil.get_pixels_hu(slices_CT[i])
        image_SCT = DcmUtil.get_pixels_hu(slices_SCT[i])

        # 计算
        index, r_CBCT, r_SCT = DcmUtil.reduce_img(i, image_CBCT, image_CT, image_SCT)


        plt.imshow(r_CBCT, interpolation='nearest', cmap='bwr', origin='lower',vmin=-2000, vmax=2000)
        plt.colorbar(shrink=.92)  # 设置一个颜色指引条

        plt.xticks(())
        plt.yticks(())

        plt.show()



rootPath = "D:\\test_data"

for file in os.listdir(rootPath):
    copPatientPath(rootPath, file)