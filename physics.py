#MIT License

#Copyright (c) 2019 Tim Yagan


import math

#speed
def speed(distance, time):
	return distance / time

#Equations of motion
def motion_eq1(initial_velocity, acceleration, time):
	final_velocity = (initial_velocity + (acceleration * time))
	return final_velocity

def motion_eq2(initial_velocity, acceleration, time):
	displacement = ((initial_velocity * time) + (0.5 * acceleration * (time*time)))
	return displacement

def motion_eq3(final_velocity=None, initial_velocity=None, acceleration=None, change_in_displacement=None):
	if(final_velocity == None):
		result = (initial_velocity ** 2) + (2*(acceleration)*change_in_displacement)
		return math.sqrt(result)

	if(initial_velocity == None):
		result = (final_velocity ** 2) + (-2*(acceleration*change_in_displacement))
		return math.sqrt(result)

#velocity
def velocity(distance = 0, time = 0):
	return distance / time

#acceleration
def delta_acceleration(final_velocity, intial_velocity, time):
	return (final_velocity - intial_velocity) / time

def acceleration(velocity, time):
	return (velocity / time)	

#newton's 2nd law
def force(mass, acceleration):
	return (mass * acceleration)

#weight
def weight(mass, gravity):
	return mass * gravity

#centripetal acceleration
def centripetal_acceleration(velocity, radius):
	return (velocity ** 2) / radius

#momentum
def momentum(mass, velocity):
	return mass * velocity

#kinetic energy
def kinetic_energy_eq1(mass, velocity):
	return 0.5 * (mass * (velocity ** 2))

def kinetic_energy_eq2(momentum, mass):
	return (momentum ** 2) / (2 * mass)

#mass flow rate - conservation of mass
def mass_flow_rate(mass, time):
	return mass / time

def mass_flow_rate_complex(density, velocity, area):
	return density * velocity * area

#volume flow rate - conservation of mass
def volume_flow_rate(volume, time):
	return volume / time

#density
def density(mass, volume):
	return mass / volume

#frequency
def frequency(time):
	return 1 / time	

#pressure 
def pressure(force, area):
	return force / area

print ("Speed: ", speed(10,2))
print ("Velocity: ", velocity(1, 4))
print ("Delta Acceleration: ", delta_acceleration(1,2,2))
print ("Acceleration: ", acceleration(10,5))
print ("Motion Equation v = v0 + at: ", motion_eq1(25, -2, 3))
print ("Motion Equation s = s0 + v0t + 0.5*at2: ", motion_eq2(25, -2, 3))
print ("Motion Equation v2 = v02 + 2as: ", motion_eq3(19, None, -8, 66))
print ("Force m*a: ", force(10, 3))
print ("Weight: ", weight(65, 9.8))
print ("Centripetal Acceleration: ", centripetal_acceleration(30, 4))
print ("Momentum p=mv: ", momentum(500, 10000))
print ("Kinetic Energy 0.5*mv2: ", kinetic_energy_eq1(10, 5))
print ("Kinetic Energy p2 / 2m: ", kinetic_energy_eq1(10, 5))
print ("Mass Flow Rate mass / time: ", mass_flow_rate(1000, 10))
print ("Volume Flow Rate mass / time: ", volume_flow_rate(500, 5))
print ("Mass Flow Rate (Sea Level) density * velocity * area : ", mass_flow_rate_complex(1.225, 3000, 1))
print ("Mass Flow Rate (Airplane Cruise Level) density * velocity * area : ", mass_flow_rate_complex(0.3054, 3000, 1))
print ("Density mass / volume: ", density(100, 10))
print ("Frequency 1 /time: ", frequency(50))
print ("Pressure force / area: ", pressure(500, 1))
