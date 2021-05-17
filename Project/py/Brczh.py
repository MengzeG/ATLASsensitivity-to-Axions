import numpy as np
import math

from const import *
from loadcsv import *

def Brczh(ma,czh_l):

    cah_l2 = 0

    x = (mz/mh)**2
    y = (ma/mh)**2
    l = ((1-x-y)**2)-4*x*y     #lambda

    w_sm = 4.088*10**(-3)     #GeV
    w_hza = ((czh_l/1000)**2)*((mh**3)/(16*math.pi))*(l)**(3/2)     #GeV
    w_haa = ((cah_l2/1000)**2)*((v**2)*mh/(32*math.pi))*((1-2*(ma/mh)**2)**2)*np.sqrt(1-4*(ma/mh)**2)     #GeV

    Brhza = w_hza/(w_sm+w_hza+w_haa)
    Bragg = 1

    b = Brhza*Bragg
    return b

