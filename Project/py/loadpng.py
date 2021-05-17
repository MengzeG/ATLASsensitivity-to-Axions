import matplotlib.pyplot as plt
from scipy import misc
import scipy
import numpy as np
from  numpy import *
import matplotlib.image as mpimg
import atlas_mpl_style as ampl
from matplotlib import ticker, cm
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import scipy
from scipy import interpolate
import sys
import math
import imageio as io
import matplotlib


# -*- coding: utf-8 -*-

filename0 = "\Bkg.png"

path = r"C:\Users\john-\Desktop\ATLAS-sensitivity-to-Axions\project\py\csv"


im = plt.imread(path+filename0)

plt.imshow(im)


plt.show()