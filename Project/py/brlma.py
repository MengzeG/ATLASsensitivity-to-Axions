from scipy import interpolate
from loadcsv import *


def Brl(ma):
    f = interpolate.interp1d(ma1,exp)
    xf = ma
    yf = f(xf)
    return yf