import os

import numpy as np
import pydicom


class DcmUtil:

    @staticmethod
    def psnr(img1, img2, zeros):
        mse = np.sum((img1 - img2) ** 2) / (img1.size - zeros)
        if(mse<0):
            pass
        # mse = np.mean((img1 - img2) ** 2)
        if mse == 0:
            return 100
        return 10 * np.log10(255.0 * 255.0 / mse)

    @staticmethod
    def mse(img1, img2, zeros):

        mse = np.sum((img1 - img2) ** 2) / (img1.size - zeros)

        return mse

    @staticmethod
    def rmse(img1, img2, zeros):
        mse = np.sum((img1 - img2) ** 2) / (img1.size - zeros)
       # print(mse)
        return np.sqrt(mse)

    @staticmethod
    def mae(img1, img2, zeros):
        mae = np.sum(np.abs(img1 - img2)) / (img1.size - zeros)
        #mae = np.mean(np.abs(img1 - img2))
        return mae

    @staticmethod
    def comp(index, image_CBCT, image_CT, image_SCT, pix_max):
        # 判断 shape是否相同
        if image_CT.shape == image_CBCT.shape and image_CT.shape == image_SCT.shape:
            image_CT1,image_CBCT,zero1=DcmUtil.clear_blank(image_CT,image_CBCT)
            image_CT2, image_SCT, zero2 = DcmUtil.clear_blank(image_CT, image_SCT)

            mae_CBCT = DcmUtil.mae(image_CT1, image_CBCT,zero1)
            mae_SCT = DcmUtil.mae(image_CT2, image_SCT,zero2)

            mse_CBCT = DcmUtil.mse(image_CT1, image_CBCT,zero1)
            mse_SCT = DcmUtil.mse(image_CT2, image_SCT,zero2)

            rmse_CBCT = DcmUtil.rmse(image_CT1, image_CBCT,zero1)
            rmse_SCT = DcmUtil.rmse(image_CT2, image_SCT,zero2)

            psnr_CBCT = DcmUtil.psnr(image_CT1, image_CBCT,zero1)
            psnr_SCT = DcmUtil.psnr(image_CT2, image_SCT,zero2)

            return (index, mae_CBCT, mae_SCT, mse_CBCT, mse_SCT, rmse_CBCT, rmse_SCT, psnr_CBCT, psnr_SCT)
            #return (index, "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1")
        else:
            return (index, "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1")

    # 切片的灰度值
    @staticmethod
    def get_pixels_hu(slice):
        image = slice.pixel_array.astype(np.int64)
        image[image == -2000] = 0

        intercept = slice.RescaleIntercept
        slope = slice.RescaleSlope

        if slope != 1:
            image = slope * image.astype(np.int64)
            image = image.astype(np.int64)

        image += np.int64(intercept)

        return image

    # 清理图片的黑边
    @staticmethod
    def clear_blank(image1_, image2_):
        image1=image1_.copy()
        image2=image2_.copy()
        '''
        1: 三张图片合并，每个坐标取最大值
        2: 获取 < 500的坐标
        3：将 image1 image2 对应的设置为0
        4：返回 image1 image2  和 < 500的个数
        '''
        image = np.maximum(image1, image2)
        image = np.argwhere(image < -500)

        for i in image:
            image1[i[0]][i[1]] = 0
            image2[i[0]][i[1]] = 0
        return image1, image2, len(image)

    # 切片排序
    @staticmethod
    def sortSlices(path):
        slices = [pydicom.read_file(path + '/' + s) for s in os.listdir(path)]
        slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
        return slices
