#!/home/ocean/anaconda3/bin/python3
#Written by Ocean Wong, last updated 2019-03-19 15:57:53, 
#For calculating the number of collisions required to slow down a neutron to thermal speed using Monte Carlo method.

from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
from numpy.random import uniform as uni

NumSim=300000 #Decide the number of trials to run.
A=2	#Atomic mass
alpha = ((A-1)/(A+1))**2
MeV=1E6
eV=1

def Thermalize(): #function to calculate number of collisions required to thermalize.
	NumCol=0
	E_n = 2*MeV#Starting energy
	ThermalEnergy = 1*eV#thermal threshold, below which we "kill" the particle
	while (E_n > ThermalEnergy):
		NumCol+=1
		E_loss_factor=uni(alpha,1)
		E_n=E_n*E_loss_factor
	return NumCol

ColToTherm=[]#Store the results as a 1D array so that a histogram can be plotted later.
for n in range(NumSim):
	NumCol = Thermalize()
	ColToTherm.append(NumCol)
print(np.mean(ColToTherm))
plt.hist(ColToTherm,bins=max(ColToTherm)-min(ColToTherm)+1)
plt.show()