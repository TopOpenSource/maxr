import os

import numpy as np
import pydicom

class DcmUtil:

    @staticmethod
    def psnr(img1, img2, pix_max):
        mse = np.mean((img1 - img2) ** 2)
        if mse == 0:
            return 100
        return 10 * np.log10(255.0 * 255.0 / mse)

    @staticmethod
    def mse(img1, img2):
        mse = np.mean((img1 - img2) ** 2)
        return mse

    @staticmethod
    def rmse(img1, img2):
        mse = np.mean((img1 - img2) ** 2)
        return np.sqrt(mse)

    @staticmethod
    def mae(img1, img2):
        mae = np.mean(np.abs(img1 - img2))
        return mae

    @staticmethod
    def comp(index, image_CBCT, image_CT, image_SCT, pix_max):
        # 判断 shape是否相同
        if image_CT.shape == image_CBCT.shape and image_CT.shape == image_SCT.shape:
            mae_CBCT = DcmUtil.mae(image_CT, image_CBCT)
            mae_SCT = DcmUtil.mae(image_CT, image_SCT)

            mse_CBCT = DcmUtil.mse(image_CT, image_CBCT)
            mse_SCT = DcmUtil.mse(image_CT, image_SCT)

            rmse_CBCT = DcmUtil.rmse(image_CT, image_CBCT)
            rmse_SCT = DcmUtil.rmse(image_CT, image_SCT)

            psnr_CBCT = DcmUtil.psnr(image_CT, image_CBCT, pix_max)
            psnr_SCT = DcmUtil.psnr(image_CT, image_SCT, pix_max)

            return (index, mae_CBCT, mae_SCT, mse_CBCT, mse_SCT, rmse_CBCT, rmse_SCT, psnr_CBCT, psnr_SCT)
        else:
            return (index, "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1")

    @staticmethod
    def get_pixels_hu(slice):
        image = slice.pixel_array.astype(np.int16)
        image[image == -2000] = 0

        intercept = slice.RescaleIntercept
        slope = slice.RescaleSlope

        if slope != 1:
            image = slope * image.astype(np.float64)
            image = image.astype(np.int16)

        image += np.int16(intercept)

        return image

    @staticmethod
    def sortSlices(path):
        slices = [pydicom.read_file(path + '/' + s) for s in os.listdir(path)]
        slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
        return slices