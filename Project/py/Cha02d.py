import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator

from brlma import Brl
from Brczh import Brczh
from const import *
from loadcsv import *



czh_l = np.linspace(0.2,0.4,100)


X, Y = np.meshgrid(ma, czh_l)
Z = Brczh(X,Y)/Brl(X)

#3d plot
#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

#Contour plot
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z,[1,3],alpha = 0.5)


#ax.clabel(CS, inline=True, fontsize=10)

ax.set_xlabel('$m_a$[GeV]')
ax.set_ylabel('$C_{Zh}$/\u039B[$TeV^{-1}$]')
ax.text(4.5,0.325,'a \u2192 \u03B3\u03B3',fontsize = 12)
ax.text(6,0.38,'ATLAS, $139fb^{-1}$ ',fontsize = 12)
#ax.set_zlabel('BR(h \u2192 Za) \u00D7 BR(a \u2192 \u03B3\u03B3)/Lim(ma)')
#ax.set_title('')

plt.show()
