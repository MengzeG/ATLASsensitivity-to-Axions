import numpy as np
import matplotlib.pyplot as plt

from brlma import Brl
from fcgg import fagg
from const import *


cgg = np.linspace(0,3e-10,100)


X, Y = np.meshgrid(ma, cgg)
#Z = Lagg(Y,X)
Z = Brl(X)/fagg(Y, X)

#3d plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

#Contour plot
#fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 500, alpha = 0.5)


ax.clabel(CS, colors = 'k')
ax.set_xlabel('$m_a$[GeV]')
ax.set_ylabel('$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]')

#plt.plot(ma, Lagg(0.0029,ma), label = '$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]=0.0029')
#plt.plot(ma, Lagg(0.005,ma), label = '$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]=0.005')
#plt.plot(ma, Lagg(0.01,ma), label = '$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]=0.01')
#plt.plot(ma, Lagg(0.02,ma), label = '$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]=0.02')
#plt.plot(ma, Lagg(0.030,ma), label = '$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]=0.03')

#plt.xscale("log")
#plt.yscale("log")

plt.show()




