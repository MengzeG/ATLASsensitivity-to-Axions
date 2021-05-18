import matplotlib.pyplot as plt
from  numpy import *

from loadcsv import *

filename0 = "\Bkg.png"
im = plt.imread(path+"\csv"+filename0)

plt.imshow(im)
plt.show()