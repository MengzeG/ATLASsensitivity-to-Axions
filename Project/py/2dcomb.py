import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

from brlma import Brl
from fcgg import fagg
from Brczh import Brczh
from const import *
from loadcsv import *


plt.fill_between(x1, y1, 1.5e4, alpha = 0.5)
plt.fill_between(x4, y4, 0.209095, alpha = 0.5)
plt.fill_between(x6, y6, 1.5e4, alpha = 1)
plt.fill_between(x2, y2, 1.5e4, alpha = 1)
plt.fill_between(x11, y11,2.88162, alpha = 1, color = '#87CEFA')
plt.fill_between(x12, y12, 1.5e4, alpha = 1)
plt.fill_between(x10, y10, 1.5e4, alpha = 0.5, color = '#87CEFA')
plt.fill_between(x3, y3, 1.5e4, alpha = 0.5)
plt.fill_between(x9, y9, 1.5e4, alpha = 1)
plt.fill_between(x5, y5, 1.5e4, alpha = 0.5)
plt.fill_between(x8, y8, 1.5e4, alpha = 1)

plt.text(0.00368546,0.209095,'Beam Dump',horizontalalignment='center',fontsize = 9)
plt.text(5.11802e-08,0.32,'CAST+SUMICO',horizontalalignment='center',fontsize = 9)
plt.text(260.408,860.308,'CDF',horizontalalignment='center',fontsize = 9, rotation = 90)
plt.text(0.000123852,3.65724e-08,'Cosmology',horizontalalignment='center',fontsize = 9)
plt.text(8.46081e-08,1.92476,'$(g-2)_{\u00B5}$',horizontalalignment='center',fontsize = 9)
plt.text(1.21121e-05,0.0151722,'HB stars',horizontalalignment='center',fontsize = 9)
plt.text(2.58357,21.23239,'ATLAS, $139fb^{-1}$',horizontalalignment='center',fontsize = 7, rotation = 90)
plt.text(9.6326e-05,44.39,'\u03D2 \u2192 inv.+\u03B3',horizontalalignment='center',fontsize = 9)
plt.text(35,599.115,'LEP',horizontalalignment='center',fontsize = 9)
plt.text(1250.98,140.908,'LHC',horizontalalignment='center',fontsize = 9, rotation = 90)
plt.text(0.000204744,3.94189,'LHC',horizontalalignment='center',fontsize = 9)
plt.text(6.06797e-06,9.5727e-05,'SN1987a',horizontalalignment='center',fontsize = 9)


cgg = np.linspace(3e-3,15505,100)

X, Y = np.meshgrid(ma, cgg )
Z = Brczh(X, Y)-(Brl(X)/fagg(Y, X))



#3d plot
#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

#Contour plot
#fig, ax = plt.subplots()

#plt.contourf(X, Y, Z, [0,100], alpha = 0.7)
#plt.contourf(X, Y, Z, [Brczh(0.7, 0.72)-(Brl(0.7)/fagg(3e-3, 0.7)),100], alpha = 0.7)
#plt.contourf(X, Y, Z, [Brczh(0.7, 1)-(Brl(0.7)/fagg(3e-3, 0.7)),100], alpha = 0.7)

plt.contourf(X, Y, Z, [0
                    ,Brczh(0.7, 0.72)-(Brl(0.7)/fagg(3e-3, 0.7))
                    ,Brczh(0.7, 1)-(Brl(0.7)/fagg(3e-3, 0.7)),100], alpha = 0.7)


plt.xscale("log")
plt.yscale("log")


plt.xlabel('$m_a$[GeV]')
plt.ylabel('$C_{\u03B3\u03B3}$/\u039B[$TeV^{-1}$]')
#plt.legend(loc = 'upper left', fontsize = 7)
plt.show()

print(Brczh(0.7, 0.72)-(Brl(0.7)/fagg(3e-3, 0.7)))
print(Brczh(0.7, 1)-(Brl(0.7)/fagg(3e-3, 0.7)))