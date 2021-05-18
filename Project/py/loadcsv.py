import numpy as np

# -*- coding: utf-8 -*-
#path to filename py
path = r"C:\Users\john-\Desktop\ATLASsensitivity-to-Axions\project\py"

filename = "\ATLASlimit"
filename1 = "\Beamdump"
filename2 = "\CAST-SUMICO"
filename3 = "\CDF"
filename4 = "\cosmology"
filename5 = "\g-2mu"
filename6 = "\HB stars"
filename7 = "\cgg"
filename8 = "\invgamma"
filename9 = "\LEP"
filename10 = "\LHC"
filename11 = "\LHC2"
filename12 = "\SN1987a"
filename13 = "\cgg3cm"
filename14 = "\cgg30cm"
filename15 = "\cgg50cm"
filename16 = "\cgg100cm"

ma1, exp = np.loadtxt(path+"\csv"+filename+'.csv', delimiter = ',', unpack=True)
x1,y1 = np.loadtxt(path+"\csv"+filename1+'.csv', delimiter = ',', unpack=True)
x2,y2 = np.loadtxt(path+"\csv"+filename2+'.csv', delimiter = ',', unpack=True)
x3,y3 = np.loadtxt(path+"\csv"+filename3+'.csv', delimiter = ',', unpack=True)
x4,y4 = np.loadtxt(path+"\csv"+filename4+'.csv', delimiter = ',', unpack=True)
x5,y5 = np.loadtxt(path+"\csv"+filename5+'.csv', delimiter = ',', unpack=True)
x6,y6 = np.loadtxt(path+"\csv"+filename6+'.csv', delimiter = ',', unpack=True)
x7,y7 = np.loadtxt(path+"\csv"+filename7+'.csv', delimiter = ',', unpack=True)
x8,y8 = np.loadtxt(path+"\csv"+filename8+'.csv', delimiter = ',', unpack=True)
x9,y9 = np.loadtxt(path+"\csv"+filename9+'.csv', delimiter = ',', unpack=True)
x10,y10 = np.loadtxt(path+"\csv"+filename10+'.csv', delimiter = ',', unpack=True)
x11,y11 = np.loadtxt(path+"\csv"+filename11+'.csv', delimiter = ',', unpack=True)
x12,y12 = np.loadtxt(path+"\csv"+filename12+'.csv', delimiter = ',', unpack=True)
x13,y13 = np.loadtxt(path+"\csv"+filename13+'.csv', delimiter = ',', unpack=True)
x14,y14 = np.loadtxt(path+"\csv"+filename14+'.csv', delimiter = ',', unpack=True)
x15,y15 = np.loadtxt(path+"\csv"+filename15+'.csv', delimiter = ',', unpack=True)
x16,y16 = np.loadtxt(path+"\csv"+filename16+'.csv', delimiter = ',', unpack=True)
