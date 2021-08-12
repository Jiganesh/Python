import math
import matplotlib.pyplot as plt

gravity_constant = 9.81
R=287
b = 1.458
s =110.4

print("Enter the required altitude in meters")
altitude = int(input())

def getDetails(altitude):

    temperature = pressure=  density = speed_of_sound= viscosity =0 

    if altitude ==0 :return  [280 , 80000, 1.2 , 350]

    if altitude>0 and altitude<=11000:
        temperature = 288.15 -0.0065*altitude
        pressure = 101325*(pow(temperature/288.15,(-gravity_constant/R/(-0.0065))))
        density = 1.225 * pow(temperature/288.15,(-gravity_constant/R/(-0.0065)-1))
        speed_of_sound = math.sqrt(1.4*287.1*temperature)
        viscosity =b * pow(temperature,1.5)/(temperature+s)
    elif  altitude> 11000 and altitude <= 20000:
        temperature = 216.65
        pressure = 22632.65* math.e**(-gravity_constant*(altitude-11000)/R/temperature)
        density  =0.36* math.e**(-gravity_constant*(altitude-11000)/R/temperature)
        speed_of_sound = math.sqrt(1.4*287.1*temperature)
        viscosity =b * pow(temperature,1.5)/(temperature+s)
    elif altitude> 20000 and altitude<=32000:
        temperature = 216.65+0.001*(altitude-20000)
        pressure = 5475.17 * ((temperature/216.65)**(-gravity_constant/R/(0.001)))
        density = 0.09*((temperature/228.65)**(-gravity_constant/R/(0.001)-1))
        speed_of_sound = math.sqrt(1.4*287.1*temperature)
        viscosity = b*(temperature**1.5)/(temperature+s)
    elif altitude> 32000 and altitude<=47000:
        temperature = 228.65 + 0.0028*(altitude-32000)
        pressure = 868.02 * ((temperature/228.65)**(-gravity_constant/R/(0.0028)))
        density = 0.01*((temperature/228.65)**(-gravity_constant/R/(0.0028)-1))
        speed_of_sound = math.sqrt(1.4*287.1*temperature)
        viscosity = b*(temperature**1.5)/(temperature+s)
    elif altitude> 47000 and altitude<=51000:
        temperature = 270.65
        pressure = 110.906 * math.e**(-gravity_constant*(altitude-47000)/R/temperature)
        density = 0.00143*math.e**(-gravity_constant*(altitude-47000)/R/temperature)
        speed_of_sound = math.sqrt(1.4*287.1*temperature)
        viscosity = b*(temperature**1.5)/(temperature+s)
    

    if (temperature, pressure, density , speed_of_sound, viscosity): 
        return [temperature, pressure, density , speed_of_sound, viscosity]
    

def printOutput(altitude):
    temperature, pressure, density , speed_of_sound, viscosity = getDetails(altitude)
    print("OUTPUT : \n")

    print("Sea Level Temperature :  288.15")
    print("ALTITUDE (H):" ,round(altitude,4) , "meter (m)")
    print("TEMPERATURE (T):",round(temperature,4),"Kelvin (k)")
    print("PRESSURE (P):",round(pressure,4), "Pascal (Pa)")
    print("DENSITY :",round(density,7), "Kilogram per Cubic meter (kg/m^3)")
    print("SPEED OF SOUND :",round(speed_of_sound,4), "meter per second (m/s)")
    print("VISCOSITY :",round(viscosity,5), "10^-6", "kg/ms")


printOutput(altitude)

'''

altitudes = [0, 10, 20 ,30 , 40 , 50 ]


#Graph of Altitude vs Temperature
temperatures = []
for i in altitudes:
    temperatures.append(getDetails(i*1000)[0])
plt.plot(temperatures, altitudes)
plt.xlabel('Temperature')
# naming the y axis
plt.ylabel('Altitude')
# giving a title to my graph
plt.title('Altitude vs Temperature')
plt.show()

#Graph of Altitude vs Pressure
pressures = []
for i in altitudes:
    pressures.append(getDetails(i*1000)[1])
plt.plot(pressures, altitudes)
plt.xlabel('Pressure')
# naming the y axis
plt.ylabel('Altitude')
# giving a title to my graph
plt.title('Altitude Vs Pressure')
plt.show()

#Graph of Altitude vs density
densities = []
for i in altitudes:
    densities.append(getDetails(i*1000)[2])
plt.plot(densities, altitudes)
plt.xlabel('Density')
# naming the y axis
plt.ylabel('Altitude')
# giving a title to my graph
plt.title('Altitude Vs Density')
plt.show()

#Graph of Altitude vs Speed of Sound
sos = []
for i in altitudes:
    sos.append(getDetails(i*1000)[3])
plt.plot(sos, altitudes)
plt.xlabel('Speed of Sound')
# naming the y axis
plt.ylabel('Altitude')
# giving a title to my graph
plt.title('Altitude Vs Speed of Sound')
plt.show()


'''












































