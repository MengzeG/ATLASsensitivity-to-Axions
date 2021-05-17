import numpy as np
import math

from const import *


def fagg(cgg,ma):

    wagg = (4*math.pi*(alph**2)*(ma**3))*((cgg)**2)/(L**2)

    ghza = (mh**2-mz**2+ma**2)/(2*ma*mh)
    La = np.sqrt((ghza**2)-1)*(1/wagg)

    d = (La/cm1)

    eff = 1-e**(-100/(d))

    return eff