import numpy as np


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
    def comp(index,image_CBCT, image_CT, image_SCT, pix_max):
        mae_CBCT = DcmUtil.mae(image_CT, image_CBCT)
        mae_SCT = DcmUtil.mae(image_CT, image_SCT)

        mse_CBCT = DcmUtil.mse(image_CT, image_CBCT)
        mse_SCT = DcmUtil.mse(image_CT, image_SCT)

        rmse_CBCT = DcmUtil.rmse(image_CT, image_CBCT)
        rmse_SCT = DcmUtil.rmse(image_CT, image_SCT)

        psnr_CBCT = DcmUtil.psnr(image_CT, image_CBCT, pix_max)
        psnr_SCT = DcmUtil.psnr(image_CT, image_SCT, pix_max)

        return (index,mae_CBCT, mae_SCT, mse_CBCT, mse_SCT, rmse_CBCT, rmse_SCT, psnr_CBCT, psnr_SCT)
