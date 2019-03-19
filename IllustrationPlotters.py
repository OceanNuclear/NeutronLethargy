#!/home/ocean/anaconda3/bin/python3
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt

alpha=0.4

x=np.linspace(alpha,1)
x_rect=np.concatenate([[alpha],x,[1]])

y=alpha*(x-x+1)
y_rect=np.concatenate([[0],y,[0]])
y2=np.log(1/x)

plt.plot(x_rect,y_rect,label="P(E)")
plt.plot(x,y2,label=r"$\Delta$ u(E)")
plt.xlim(0,1)
plt.legend()
#plt.title("")

plt.show()
