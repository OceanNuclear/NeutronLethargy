#!/home/ocean/anaconda3/bin/python3
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
from numpy.random import uniform as uni

NumSim=300000
A=2
alpha = ((A-1)/(A+1))**2
MeV=1E6
eV=1

def Thermalize():
	NumCol=0
	E_n = 2*MeV
	ThermalEnergy = 1*eV
	while (E_n > ThermalEnergy):
		NumCol+=1
		E_loss_factor=uni(alpha,1)
		E_n=E_n*E_loss_factor
	return NumCol

ColToTherm=[]
for n in range(NumSim):
	NumCol = Thermalize()
	ColToTherm.append(NumCol)
print(np.mean(ColToTherm))
plt.hist(ColToTherm,bins=max(ColToTherm)-min(ColToTherm)+1)
plt.show()