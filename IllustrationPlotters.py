#!/home/ocean/anaconda3/bin/python3
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt

alpha=0.4
height = 0.5

x=np.linspace(alpha,1)
#Create the square distribution
fig,ax = plt.subplots()
x_rect=np.concatenate([[0,alpha],x,[1]])
y=height*(x-x+1)#hack to make y=alpha with the same shape of x, quickly.
y_rect=np.concatenate([[0,0],y,[0]])

Figure = "Fig3"

if Figure=="Fig1":
	#Create other distributions
	y2=np.log(1/x)

	#Make plot
	ax.plot(x_rect,y_rect,label="P(E)")
	ax.plot(x,y2,label=r"$\Delta$ u(E)")

	#Set x axes
	ax.set_xticks([alpha,1])
	ax.set_xticklabels([r"$\alpha E_i$",r"$E_i$"])
	ax.set_xlabel(r"Final energy after collision $E_f$")
	ax.set_xlim(0,1.002)

if Figure=="Fig2":
	x2 = np.linspace(0,-np.log(alpha))
	y2 = x2
	#make prob dist look nicer
	x2rect=np.concatenate([[0],x2,[-np.log(alpha),1]])
	y2rect=np.concatenate([[0],0.4*np.e**(-x2),[0,0]])
	ax.plot(x2rect,y2rect,label=r"$P(\Delta u)=\frac{dE}{d(\Delta u)}P(E)$")
	ax.plot(x2,y2,label="$ \Delta u$")
	ax.set_xlabel(r"$\Delta u$")
	ax.set_xticks([0,np.log(1/alpha)])
	ax.set_xticklabels(["0",r"-ln($\alpha$)"])
	ax.set_xlim(-0.008,1)

if Figure=="Fig3":
	xlong=np.linspace(0.2,1,100)
	ylong=np.log(1/xlong)
	ax.plot(x_rect,y_rect,label="P(E)")
	ax.plot(xlong,ylong,label=r"$\Delta$ u(E)")

	midpt=(alpha+1)/2
	if "Dotted line":
		xdot=[midpt]
		ydot=[height]
		xdot.append(midpt)
		ydot.append(np.log(1/midpt))
		xdot.append(0)
		ydot.append(np.log(1/midpt))
	ax.plot(xdot,ydot, linestyle="--")
	ax.set_xlim(0,1.002)
	ax.set_xlabel(r"Final energy after collision $E_f$")
	ax.set_xlabel(r"Final energy after collision $E_f$")
	ax.set_xticks([alpha,1])
	ax.set_xticklabels([r"$\alpha E_i$",r"$E_i$"])

#set y axes, legend, and save.
ax.set_ylim(bottom=0)
ax.set_yticks([])
ax.legend()
fig.set_size_inches(4,3)
plt.savefig(Figure+".png",bbox_inches="tight")#Necessary for saving the thing properly
print("Saved "+Figure+".png")
