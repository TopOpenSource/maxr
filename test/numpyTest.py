from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from utils.DcmUtil3 import DcmUtil

img = Image.open("D://a.jpeg")
arr = np.asarray(img)
plt.imshow(arr)
plt.show()


arr=DcmUtil.rot180(arr)
plt.imshow(arr)
plt.show()


