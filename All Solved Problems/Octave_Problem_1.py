import matplotlib.pyplot as plt
import math
Area = 1.2* 2 # m^2
L_glass = 3 # mm
K_glass = 0.78 # W/(m-C)
T_infinity_1 ,T_infinity_2 = 24,-5 # C
h_1,h_2  = 10, 25 # W/m^2-C
K_air = 0.026 # W/(m-C)

def Q_dot_result(L_air):
    R_conv_1 = 1/(h_1*Area)
    R_glass =(L_glass*0.001)/(K_glass*Area)
    R_air = (L_air*0.001)/(K_air*Area)
    R_conv_2 = 1/(h_2*Area)
    R_total = R_conv_1 +2* R_glass + R_air + R_conv_2
    Q_dot = (T_infinity_1- T_infinity_2)/R_total
    return R_total, round(Q_dot,3)

L_air_array =[2,5,10,15,20]
R_total_array = []
Q_dot_array = []

for i in L_air_array:
    R_total_array.append(Q_dot_result(i)[0])
    Q_dot_array.append(Q_dot_result(i)[1])
  
plt.title("octave")
plt.plot(L_air_array, Q_dot_array ,color ="red")
plt.show()

plt.title("octave")
plt.plot(L_air_array, R_total_array, color = "green")
plt.show()

