import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy import pi
import math
from const import *




def Lagg(cgg,ma):

    wagg = (4*math.pi*(alph**2)*(ma**3))*((cgg)**2)/(L**2)

    ghza = (mh**2-mz**2+ma**2)/(2*ma*mh)
    La = np.sqrt((ghza**2)-1)*(1/wagg)

    return La





plt.plot(ma,Lagg(0.0029,ma), label = '$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]=0.0029')
plt.plot(ma,Lagg(0.005,ma), label = '$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]=0.005')
plt.plot(ma,Lagg(0.01,ma), label = '$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]=0.01')
plt.plot(ma,Lagg(0.02,ma), label = '$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]=0.02')
plt.plot(ma,Lagg(0.030,ma), label = '$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]=0.03')




plt.xlabel('$m_a$[GeV]')
plt.ylabel('d[cm]')
plt.title('Decay length')
#plt.xscale("log")
#plt.yscale("log")
plt.legend()
plt.show()