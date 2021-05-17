import numpy as np
import matplotlib.pyplot as plt
import math

ma1 = [0.7,1.0,2.0,4.0,6.0,9.0]
exp = [0.0705354,0.091249,0.119474,0.0608263,0.0524145,0.0495964]
y1 = [0.0502474,0.0649824,0.0851612,0.043293,0.0372992,0.035303]
y2 = [0.100348,0.129832,0.16988,0.0863901,0.0744695,0.070515]
y3 = [0.0372296,0.0481412,0.0631222,0.0320974,0.0276499,0.0261568]
y4 = [0.139091,0.180079,0.235142,0.11964,0.103165,0.0977239]


ma = np.linspace(0.7,9,100)     #GeV

def B(ma,czh_l):
    mh = 125     #GeV
    
    mz = 91     #GeV
    v = 246     #GeV
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
    
    plt.plot(ma, b,'--', label = 'C/\u039B ={}$TeV^{}$'.format(czh_l,-1))



B(ma,0.5)
B(ma,0.1)
B(ma,0.2)
plt.plot(ma1,exp, '.--',label = 'expected upper limit')
plt.fill_between(ma1, y3,y4,color = '#00ff00',alpha= 1, label = '2\u03C3')
plt.fill_between(ma1, y1,y2,color = '#ffff00',alpha= 1, label = '1\u03C3')
plt.xlabel('$m_a$[GeV]')
plt.ylabel('BR(h \u2192 Za) \u00D7 BR(a \u2192 \u03B3\u03B3)')
plt.title('$C_{Zh}=C_{ah}$')
plt.legend()
plt.show()

