from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import mymodule as mm

image = Image.open('exemple/test.png')
imageArray = np.array(image)
mm.threshold(imageArray)

plt.imshow(imageArray)
plt.show()