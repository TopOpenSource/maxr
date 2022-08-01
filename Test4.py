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
    #
    for i in range(0, len(slices_CT)):

        image_CBCT = DcmUtil.get_pixels_hu(slices_CBCT[i])
        image_CT = DcmUtil.get_pixels_hu(slices_CT[i])
        image_SCT = DcmUtil.get_pixels_hu(slices_SCT[i])

        # 计算
        index, r_CBCT, r_SCT = DcmUtil.reduce_img(i, image_CBCT, image_CT, image_SCT)

        cbct_reduce = patientCBCTPath + "_reduct"
        sct_reduce = patientSCTPath + "_reduct"

        # 判断文件夹是否存在,创建文件夹
        if (not os.path.exists(cbct_reduce)):
            os.makedirs(cbct_reduce)

        if (not os.path.exists(sct_reduce)):
            os.makedirs(sct_reduce)

        # 保存图片
        saveImage("CBCT", DcmUtil.rot180(r_CBCT), cbct_reduce + "\\" + str(i) + ".png")
        saveImage("SCT", DcmUtil.rot180(r_SCT), sct_reduce + "\\" + str(i) + ".png")


def saveImage(title, data, savePath):
    plt.suptitle(title, fontsize=16)

    plt.imshow(data, interpolation='nearest', cmap='bwr', origin='lower', vmin=-2000, vmax=2000)

    plt.colorbar(shrink=.92)

    plt.xticks(())
    plt.yticks(())
    #plt.show()
    plt.savefig(savePath)
    plt.close("all")


rootPath = "D:\\test_data"

for file in os.listdir(rootPath):
    copPatientPath(rootPath, file)
