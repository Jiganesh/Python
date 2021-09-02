import math

# Aircraft Specification
Max_Takeoff_Wt=31751;         # in kg
Wing_Span= 11;           # in m
Wt_by_S=(Max_Takeoff_Wt/Wing_Span);
Density=1.225;           # at atmospheric condition
Coef_Drag=0.010;
K=0.062;

L_by_D_Max=math.sqrt(1/(4*Coef_Drag*K)); # lift by drag ratio max
# Minimum glide angle at which aircraft should fly
Min_glide_angle=math.degrees(math.atanh(1/(L_by_D_Max))) # minimum glide angle

# Maximum range it can cover during glide
h=11000;          # height in km
Range_max_glide=h  /math.atanh(math.radians(Min_glide_angle))  # maximum range at minimum glide angle

# Velocity at minimum climb angle
a=(2/Density);
b=math.sqrt((K)/(Coef_Drag));
c=Wt_by_S;
Velocity_min_angle=math.sqrt(a*b*c)

print("Results\n")
print("Aircraft Performance at Glide : "  )
print("Minimum Glide Angle : ", round(Min_glide_angle,4))
print("Range_max_glide : ", round(Range_max_glide,3))
print("Velocity at minimum climb angle : ", round(Velocity_min_angle,3))

