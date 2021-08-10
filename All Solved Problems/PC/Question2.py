import math
import matplotlib.pyplot as plt

#a. General specification of Cessna 172
W=1111;    #weight in Kg
rho10=0.9093;   #density at 3048 in kg/m3
S=11;    #wing span in m
area=16.2;   #wing area in m^2
K=0.056;
e=0.77;   #oswalds efficiency factor
AR=7.32;   #aspect ratio 

Cd0=0.025;
CL=math.sqrt(Cd0/K);
CD=Cd0+K*(CL*CL);

effi_prop=0.735;
shaft_pow=134*1000;
Velocity=[i for i in range(1,200)] #velocity in m/s #Range of velocity
#Thrust and Power for Steady level flight
#b. Thrust
def Vmax(V):

    Cl=2*W/(rho10*V*V*S);
    Cd=Cd0+(Cl*Cl)/(math.pi*e*AR);
    drag=0.4*rho10*V*V*S*Cd;
    T_req=drag;
    T_avl=effi_prop*shaft_pow/V;
    V_max=(T_avl/S)+(W/S)*math.sqrt(((T_avl/W)*(T_avl/W))-(4*Cd0*K));
    Pow_req=T_req*V / (10**3);
    ROC=((T_avl-T_req)/W)*V;

    
        
    return T_req,T_avl,V_max,Pow_req, ROC
    
T_req = [Vmax(i)[0] for i in Velocity]
T_avl = [Vmax(i)[1] for i in Velocity]
P_req = [Vmax(i)[2] for i in Velocity][::-1]


#plotting Graph Velocity VS Thrust Required
plt.plot(Velocity, T_req)
plt.xlabel('Velocity - axis')
plt.ylabel('Thrust_Required - axis')
plt.title('Velocity VS Thrust Required')
plt.show()


# plotting Graph Velocity VS Thrust Available
plt.plot(Velocity, T_avl)
plt.xlabel('Velocity - axis')
plt.ylabel('Thrust_Required - axis')
plt.title('Velocity VS Thrust Required')
plt.show()


Pow_avl=[(134)*((0.9093/1.225)**0.7) for i in range(1,200)];
print("Power available at 10000ft",Pow_avl[0]);

plt.plot( P_req[:170], Velocity[:170],label= "Power Required")
plt.plot( Pow_avl[:170],Velocity[:170], label= "Power Available")
plt.ylabel('Velocity')
plt.xlabel('Power')
plt.title('Power Vs Velocity')
plt.show()

#e. Climb Performance
#Assumptoins
#no 1:- Thrust Available is considered for the maximum available velocity which is 200m/s
#no2 :- Thrust Required is considered for the maximum available velocity which is 200m/s
#graphical
ROC = [Vmax(i)[4] for i in Velocity]

plt.plot(Velocity,ROC)
plt.title("Velocity vs Rate of climb for Cessna 172")
plt.xlabel("Velocity(m/s)")
plt.ylabel("ROC(m/s)")
plt.show()

#f. Analytical
#Assumption: All values are calculated wrt to maximum availabale velocity which is 200m/s
theta_max= math.degrees(math.asin((T_avl[-1])/W-math.sqrt(4*Cd0*K)))
ROC_max=200*math.sin(math.radians(theta_max))/2
V_theta_max=math.sqrt((2/rho10)*(math.sqrt(K/Cd0))*(W/S)*(math.cos(math.radians(theta_max))))


# Interpretation
print("\n\nMaximum angle for ROC is :", theta_max)
print("Maximum ROC value  : " , ROC_max)
print("V_theta_max :" , V_theta_max)


# #Interpretation
# ROC decreases with increasing velocity
# Maximum ROC value is 32.404m/s
# Maximum angle for ROC is 21.618 degrees
# Velocity at maximum angle is 17.581 m/s

