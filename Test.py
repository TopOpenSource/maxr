
import pydicom
import matplotlib.pyplot as plt
from utils.DcmUtil import DcmUtil

DcmUtil.test()

#pydicom.read_file
dcm = pydicom.dcmread("D:\\test_data\\test_data\\0134606885310576\\CT\\1.dcm")
img_arr = dcm.pixel_array
