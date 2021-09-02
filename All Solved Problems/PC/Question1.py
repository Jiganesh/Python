import matplotlib.pyplot as plt
import numpy as np

Weight = 311477    #Weight in N
rho = 1.225    
e = 0.995
A = 43
S = 11
AR = (S**2/A)
K = 1/np.pi/e/AR
cd = 0.02
TbyW = 0.609
WbyS = 28316.11

roc = lambda V : V*(TbyW - 0.5*rho*V**2/(WbyS)*cd - 2*WbyS*K/rho/V**2)
V = np.arange(100,600,10)    
ROC = np.array([roc(i) for i in V])

plt.plot(V,ROC)
plt.xlabel('Velocity in m/s')
plt.ylabel('ROC in m/s')
plt.title('Figure 1 : Variation of ROC with Velocity')
plt.show()