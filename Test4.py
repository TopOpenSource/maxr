import numpy as np

a = np.zeros((512, 512), dtype='int16')

a[511][511] = -754

print(a ** 2)
