import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import math
 
def Q_result_sphere(thickness):
    K_insulation =0.13
    h1=20
    T_inlet =50
    T_outlet =15
    Diameter_sphere =0.005
    Radius_of_sphere = Diameter_sphere/2
    Radius_of_insulation = (Diameter_sphere+2*thickness)/2
    Area = 2*(Radius_of_insulation**2)*math.pi
    R_1 = (math.log(Radius_of_insulation/Radius_of_sphere))/2*math.pi*K_insulation
    R_2 = 1/(h1/Area)
    R_total = R_1 + R_2
    Q_dot = (T_inlet-T_outlet)/R_total
    return R_total, Q_dot

thickness =[0.0005, 0.001, 0.002]
R_total_array = []
Q_dot_array = []
for i in thickness:
    R_total_array.append(Q_result_sphere(i)[0])
    Q_dot_array.append(Q_result_sphere(i)[1])


x= [0, 0.0004,0.0015, 0.002]
y=[]
z=[]
for i in x:
    y.append(Q_result_sphere(i)[0])
    z.append(Q_result_sphere(i)[1])


x = np.array([0, 0.0004,0.0015, 0.002])
y = np.array([2.9, 2.4 ,2.8,3])

X_Y_Spline = make_interp_spline(x, y)

X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)
 
# Plotting the Graph
plt.plot(X_, Y_, color = "green")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
  

x = np.array([0, 0.0004,0.0015, 0.002])
y = np.array([12,14.5,12.5,11.5])

X_Y_Spline = make_interp_spline(x, y)

X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)
 
# Plotting the Graph
plt.plot(X_, Y_, color = "red")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

