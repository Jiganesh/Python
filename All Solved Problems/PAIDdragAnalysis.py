# @Author RUTURAJ SHEWALE

import matplotlib.pyplot
import numpy 
import math

# Ambient Properties
Ph   = 101325               # Ambient Pressure in N/sq.m 8 rhoh = 1.225                
rhoh = 1.225                 # Ambient Density in kg/cu.m
Th   = 288.15               # Ambient Temperature in K=
Muh  = 1.7894*10**-5        # Dynamic Viscosity of Air in Ns/sq.m


# Wing Specifications
W_To    = 600*9.8           # Maximum Takeoff Weight in N
S_Wing  = 11                # Wing Area in  Sq.m 
b_Wing  = 9                 # Wing Span in m
AR_Wing = 7.36              # Aspect Ratio of Wing
TR_Wing = 0.70              # Taper Ratio of Wing
MC_Wing = 1.23              # Mean Aerodynamic Chord of Wing in m
tc_Wing = 0.15              # Thickness - Chord Ratio of Wing

# Fuselage Specifications 

L_Fuse    = 7               # Length of the Fuselage
SWet_Fuse = 20              # Wetted Surface Area of Fuselage
MaxA_Fuse = 0.8             # Maximum Cross Section Area of Fuselage
D_Fuse    = 1.009           # Equivalent Diameter of Fuselage
LtoD_Fuse = 6.936           # Length-Diameter Ratio of Fuselage

def Cdo(V):
    # Zero Lift Drag Coefficient of Fuselage
    Re_Fuse = (rhoh*L_Fuse*V)/(Muh)

    Cf_Fuse = 0.00258+(0.00102*math.exp(-6.28*10**-9*Re_Fuse))+(0.00295*math.exp(-2.01*10**-9*Re_Fuse))/2
    RW_Fuse = 1
    CD0_Fuse = (RW_Fuse*Cf_Fuse*(1+(60/(LtoD_Fuse**3))+(0.0025*LtoD_Fuse))*(SWet_Fuse/S_Wing))


    # Zero Lift Drag Coefficient of Wing
    Re_Wing = (rhoh*MC_Wing*V)/(Muh) 
    Cf_Wing = 0.00258+(0.00102*math.exp(-6.28*10**-9*Re_Fuse))+(0.00295*math.exp(-2.01*10**-9*Re_Fuse))/2  
    RF_Wing = 1
    CD0_Wing= (RF_Wing*Cf_Wing*(1+(tc_Wing)+ (100*tc_Wing**4))*((2*S_Wing)/S_Wing))*20
    
    # Zero Lift Drag Coefficient of Aircraft
    CD0 = CD0_Fuse + CD0_Wing
    return CD0 /10          

def Cdi(V):
    eps = 0.85                                      # Oswald's Wing Efficiency Factor
    K = 1/(3.147*eps*AR_Wing)                       # Lift Induced Drag Coefficient Factor
    CL = (2*W_To)/(rhoh*S_Wing*V**2)                # Coefficient of Lift of Aircraft
    CDi = K*CL**2                                   # Lift Induced Drag Coefficient
    return CDi

# Zero lift Drag Coefficient of Aircraft for 100 m/s 
Cdo_100 = Cdo(100)
# lift induced Drag Coefficient of Aircraft for 100 m/s 
Cdi_100 = Cdi(100)

print("Calculation of Zero Lift Drag Coefficient for the Aircraft and Lift Induced Drag Coefficient\n")
print("The Zero Lift Drag Coefficient for the Aircraft At 100m/s Velocity is:",Cdo_100)
print("The Lift Induced Drag Coefficient for the Aircraft At 100m/s Velocity is:",Cdi_100)

V = numpy.arange(50,200,5)
Cdo_var = numpy.array([ ])
Cdi_var = numpy.array([ ])
for i in V:
    Cdo_var = numpy.append(Cdo_var,Cdo(i))
    Cdi_var = numpy.append(Cdi_var,Cdi(i))
 
matplotlib.pyplot.figure(figsize = (15,10))
matplotlib.pyplot.plot(V,Cdo_var,'m-',label="Cdo-Aircraft")
matplotlib.pyplot.plot(V,Cdi_var,'b-',label="Cdi-Aircraft")
matplotlib.pyplot.title("Variation of Cdo & Cdi with Velocity",fontsize=15)
matplotlib.pyplot.minorticks_on()
matplotlib.pyplot.grid(which='minor')
matplotlib.pyplot.xlabel("Velocity [ m/s ]",fontsize=15)
matplotlib.pyplot.ylabel("Drag Coefficient",fontsize=15)
matplotlib.pyplot.legend(fontsize=15)
matplotlib.pyplot.grid(linewidth=2)
matplotlib.pyplot.show()


#Determination of Velocity for Minimum Thrust Required
#Analytical
eps=0.85
k=1/(3.147*eps*AR_Wing) 
V_mintr=numpy.sqrt((2/rhoh)*(numpy.sqrt(k/0.025)*(W_To/S_Wing)))
print("\n\nCalculation of Velocity for Minimum Thrust Required:\n")
print("Velocity for minimum Thrust required is:", V_mintr,"m/s")


# Graphically
V = numpy.arange(0,200,1)

Cdo_d = numpy.array([ ])
Cdi_d = numpy.array([ ]) 
for i in V:
    Cdo_d = numpy.append(Cdo_d,Cdo(i))  
    Cdi_d = numpy.append(Cdi_d,Cdi(i))
Drag_ZeroLift = (0.5*rhoh*S_Wing*Cdo_d*V**2)                
Drag_LiftInduced = (0.5*rhoh*S_Wing*Cdi_d*V**2)         
Drag = (0.5*rhoh*S_Wing*Cdo_d*V**2)  + (0.5*rhoh*S_Wing*Cdi_d*V**2)     
matplotlib.pyplot.figure(figsize=(15,10))
matplotlib.pyplot.plot(V,Drag, label="Thrust Required")
matplotlib.pyplot.axis([0,200,0, 6000])
matplotlib.pyplot.title("Variation of Thrust required with Velocity",fontsize=15)
matplotlib.pyplot.xlabel("Velocity",fontsize=15)
matplotlib.pyplot.ylabel("Thrust Required",fontsize=15)
matplotlib.pyplot.minorticks_on()
matplotlib.pyplot.grid(which='minor') 
matplotlib.pyplot.grid(linewidth=2)
matplotlib.pyplot.legend(fontsize=13)
matplotlib.pyplot.show()
