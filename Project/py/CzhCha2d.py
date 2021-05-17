import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
from scipy import interpolate
import math

ma1 = [0.7,1.0,2.0,4.0,6.0,9.0]
exp = [0.0705354,0.091249,0.119474,0.0608263,0.0524145,0.0495964]
y1 = [0.0502474,0.0649824,0.0851612,0.043293,0.0372992,0.035303]
y2 = [0.100348,0.129832,0.16988,0.0863901,0.0744695,0.070515]
y3 = [0.0372296,0.0481412,0.0631222,0.0320974,0.0276499,0.0261568]
y4 = [0.139091,0.180079,0.235142,0.11964,0.103165,0.0977239]


def Br(czh_l,ma):
    mh = 125     #GeV
    #ma = np.linspace(0.0001,10,6)     #GeV
    mz = 91     #GeV
    v = 246     #GeV

    #czh_l = np.linspace(0.0002,0.0004,6)

    cah_l2 = czh_l

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


def lim(ma):
    f = interpolate.interp1d(ma1,exp)
    yf = f(ma)

    return yf


ma = np.linspace(0.7,9,100)
czh_l = np.linspace(0.25,0.4,100)
#czh_l = 0.25

#X, Y = np.meshgrid(ma, czh_l)
#Z = Br(Y,X)/lim(X)

plt.plot(ma,Br(0.8,ma))
plt.plot(ma,Br(0.85,ma))
plt.plot(ma,Br(0.9,ma))
plt.plot(ma,Br(1,ma))
plt.plot(ma1,exp)
#3d plot
#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

#Contour plot
#fig, ax = plt.subplots()
#CS = ax.contour(X, Y, Z,[1,3],alpha = 0.5)
#CS = ax.contour(X, Y, Z,alpha = 0.5)

#ax.clabel(CS, inline=True, fontsize=10)

#ax.set_xlabel('$m_a$[GeV]')
#ax.set_ylabel('$C_{Zh}$/\u039B$[TeV^{-1}]$')
#ax.text(4.5,0.325,'a \u2192 \u03B3\u03B3',fontsize = 12)
#ax.set_zlabel('BR(h \u2192 Za) \u00D7 BR(a \u2192 \u03B3\u03B3)/Lim(ma)')
#ax.set_title('')

plt.show()

