import numpy as np


class DcmUtil:

    @staticmethod
    def psnr(img1, img2, pix_max):
        mse = np.mean((img1 - img2) ** 2)
        if mse == 0:
            return 100
        return 10 * np.log10(pix_max * pix_max / mse)

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
