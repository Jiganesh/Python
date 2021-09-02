import math
import matplotlib.pyplot as plt
import numpy as np
# This code written for climb performance at 11 km
# Lockheed Martin Raptor F-35
MTOW= 31700*9.81; # Maximum Take off Weight
S_Wing= 43; # Wing Area
b_wing= 11; # Wing Span
V_criuse= 200; # cruise velocity in m/s
cd = 0.02
TbyW = 0.609
WbyS = 28316.11
T_av0= 120000; # Thrust avilable without afterburner
Cd0 = 0.010; # Coefficient Zero Lift Drag
e = 0.995; # Wing efficiency
AR=(b_wing**2)/(S_Wing); # Aspect Ratio
k=1/(math.pi*e*AR);
rho_0=1.225; # Density at Sea Level
rho_11=0.364; # Density at 11 km
# Plot for rate of climb vs velocity
Velocity=[i for i in range(1,500)]
def ROC_cal(V):

    C_L= math.sqrt(Cd0/k);
    CD=Cd0+(k*C_L*C_L);
    D=0.5*rho_11*V**2*S_Wing*CD;
    T_req=D;
    T_av11=(T_av0*(rho_11/rho_0));
    ROC=((T_av11*V)-(T_req*V))/MTOW;
    return ROC
T_av=(T_av0*(rho_11/rho_0));
roc = lambda V : V*(TbyW - 0.5*rho_0*V**2/(WbyS)*cd - 2*WbyS*k/rho_0/V**2)
V = np.arange(100,600,10)    
ROC = np.array([roc(i) for i in V])

plt.plot(V,ROC)
plt.xlabel('Velocity in m/s')
plt.ylabel('ROC in m/s')
plt.title('Figure 1 : Variation of ROC with Velocity')
plt.show()


# Climb angle maximum
a=T_av/MTOW; #T/W
A=math.sqrt(4*Cd0*k);
thetamax= math.degrees(math.sin(math.degrees(a-A)))-6
# velocity at maximum climb angle
b=2/rho_0;
c=math.sqrt(k/Cd0/1.8);
d=(MTOW*(math.acos(math.radians(thetamax))))/S_Wing;
V_thetamax=math.sqrt(b*c*d)
# Code for hodograph
angle=[i*0.5 for i in range(1,51)]

def hodo(angle):
    Vv= V_criuse*(math.sin(math.radians(angle)));
    Vh= V_criuse*(math.cos(math.radians(angle)));
    
    return Vv , Vh

Vv =[hodo(i)[0] for i in angle]
Vh =[hodo(i)[1] for i in angle]


plt.plot(Vh,Vv)
plt.title('HODOGRAPH')
plt.xlabel('Horizontal Component of velocity')
plt.ylabel('Vertical Component of velocity')
plt.show()
# Analytical Value for maximum rate of Climb
ROC_max=V_thetamax*(math.sin(math.radians(thetamax)))

print("theta_max = ",thetamax)
print("V_thetamax = ",V_thetamax)
print('ROC_max =',ROC_max)
