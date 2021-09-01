import math;
import matplotlib.pyplot as plt


# Specifications Provided
Wing_Span=5.18;
Wing_Area=3.51;
W_To=435.5*9.81;
W_by_S=(W_To/Wing_Area);
Fuel_Capcity=210;
C_Do=0.02;
K=0.062;
V_cruise=369*(5/18);
v_Stall=89*(5/18);
V_max=373*(5/18);
Thrust_single_engine=900;
no_engines=1;
#Atmospheric Conditions
Density=1.225;

#Thrust required and Thrust Available Vs Velocity

Velocity=[i for i in range(1,201)]

def thrust(Velocity):
    C_L=(2*W_To)/(Density*Velocity*Velocity*Wing_Area);
    Thrust_Required=(C_Do+K*C_L**2)*(0.5*Density*Velocity*Velocity*Wing_Area);
    Power_Required=Thrust_Required*Velocity; 
    return(Thrust_Required,Power_Required)

Thrust_Available=[0.735*134*1000/i for i in Velocity]
Thrust_Required=[thrust(i)[0] for i in Velocity]

# plotting Graph Velocity VS Thrust Required
plt.plot(Velocity, Thrust_Required)
plt.xlabel('Velocity - axis')
plt.ylabel('Thrust_Required - axis')
plt.title('Velocity VS Thrust Required')
plt.show()

# plotting Graph Velocity VS Thrust_Available
plt.plot(Velocity, Thrust_Available)
plt.xlabel('Velocity - axis')
plt.ylabel('Thrust_Available - axis')
plt.title('Velocity VS Thrust_Available')
plt.show()

T_BY_W=(900/W_To) 

#print(T_BY_W) #0.21066158270047083

num=(T_BY_W*W_by_S)+(W_by_S*(math.sqrt(T_BY_W**2-4*C_Do*K)));
den=(Density*C_Do);
V_Max_Analytical=math.sqrt((num)/(den))


#print(V_Max_Analytical) #142.58073975336006
ROC= [Velocity[i]*(Thrust_Available[i]-Thrust_Required[i])/(W_To) for i in range(len(Velocity))]
# print(ROC) #[-122.99642331158861, -61.18229476442195, -40.4373119328513, -29.959766495536375,..........]

# plotting Graph Velocity VS ROC
plt.plot(Velocity, ROC)
plt.xlabel('Velocity - axis')
plt.ylabel('ROC - axis')
plt.title('Velocity VS ROC')
plt.show()

# Hodograph

angle = [i*0.5 for i in range(1,51)]
V_hor = [V_cruise*math.cos(i) for i in angle]
V_ver = [V_cruise*math.sin(i) for i in angle]

# plotting Graph V_hor VS V_ver
# plt.plot(V_hor, V_ver)
# plt.xlabel('V_hor - axis')
# plt.ylabel('V_ver - axis')
# plt.title('V_hor VS V_ver')
# plt.show()

# COMPARISON OF MAX CLIMB ANGLE FROM HODOGRAPH AND ANALYTICAL FORMULATION
Climb_angle_max=math.degrees(math.asinh(T_BY_W-math.sqrt(4*C_Do*K)))
#print(Climb_angle_max) #8.008729710395235


a=(2/Density);
b=math.sqrt((K)/(C_Do));
c=W_by_S;
Velocity_Theta_maxx=math.sqrt((a*b*c*math.cos(math.radians(Climb_angle_max))))
#print(Velocity_Theta_maxx) #58.86188114104379

#How to determine the maximum rate of climb
ROC_max=Velocity_Theta_maxx*math.sin(math.radians(Climb_angle_max))

#print(ROC_max)# 8.200871477566722

#Glide Performance

L_by_D_Max=math.sqrt(1/(4*C_Do*K));
theta_min=math.degrees(math.atan(1/(L_by_D_Max)))
#print(theta_min) #4.028533465486285

h=3048
Range_max_glide=h/math.degrees(math.tan(theta_min))
#print(Range_max_glide) #43.35916458464309e+04


 
