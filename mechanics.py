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

#angular frequency
def angular_frequency(frequency):
	return 2 * math.pi * frequency

#angular velocity
def angular_velocity(linear_velocity, radius):
	return linear_velocity / radius

#gravitational potential
def gravitational_potential(gravity, mass, radius):
	return -1 * ((gravity * mass)/ radius)

#gravitational potential energy
def gravitational_potential_energy(gravity, mass1, mass2, distance_between_masses):
	return -1 * ((gravity * mass1 * mass2) / distance_between_masses)

#orbital speed
def orbital_speed(gravity, mass, radius):
	return math.sqrt((gravity * mass)/ radius)	

#escape speed
def escape_speed(gravity, mass, radius):
	return math.sqrt(2 * (gravity * mass)/ (radius))

#mach number
def mach_number(velocity, speed_of_sound):
	return velocity / speed_of_sound	

#efficiency
def efficiency(energy_output, energy_input):
	return (energy_output / energy_input) * 100

#power
def power(work, time):
	return work / time

#impulse
def impulse(force, time):
	return force * time

#torque - math.sin utilises radians. You have to convert radians to degrees to get an accurate torque reading
def torque(lever_distance, force, angle):
	return lever_distance * force * (math.sin(math.radians(angle)))

#pendulum period
def pendulum_period(length, gravity):
	return 2 * math.pi * (math.sqrt(length / gravity))

#pendulum frequency
def pendulum_frequency(length, gravity):
	return 1 / (2 * math.pi * (math.sqrt(length / gravity)))

#freefall speed
def freefall_speed(gravity, time):
	return gravity * time

#freefall distance
def freefall_distance(gravity, time):
	return 0.5 * gravity * (time ** 2)

#freefall time of fall
def freefall_time(velocity, gravity):
	return velocity / gravity

#friction co-efficient
def friction_coefficient(force, friction):
	return friction / force

#mechanical advantage - lever
def mechanical_advantage_lever(effort_arm_length, load_arm_lenth):
	return effort_arm_length / load_arm_lenth

#mechanical advantage - pulley
def mechanical_advantage_pulley(number_of_pulleys):
	return number_of_pulleys * 2	

#mechanical advantage - screw
def mechanical_advantage_screw(diameter, distance_between_threads):
	return math.pi * (diameter / distance_between_threads)

#mechanical advantage - wedge
def mechanical_advantage_wedge(wedge_length, wedge_thickness):
	return wedge_length / wedge_thickness

#mechanical advantage - ramp
def mechanical_advantage_ramp(ramp_height, ramp_length):
	return 1 / (ramp_height / ramp_length)

#mechanical advantage - wheel and axle
def mechanical_advantage_wheel_axle(wheel_radius, axle_radius):
	return wheel_radius / axle_radius


#projectile motion - horizontal velocity
def projectile_horizontal_velocity(velocity, angle_of_launch):
	return velocity * (math.cos(math.radians(angle_of_launch)))

#projectile motion - vertical velocity
def projectile_vertical_velocity(velocity, angle_of_launch):
	return velocity * (math.sin(math.radians(angle_of_launch)))

#projectile motion - time of flight
def projectile_time_of_flight(vertical_velocity, gravity):
	return 2 * vertical_velocity / gravity

#projectile motion - range of the projectile
def projectile_range(horizontal_velocity, vertical_velocity, gravity):
	return 2 * horizontal_velocity * vertical_velocity / gravity

#projectile motion - maximum height
def projectile_maximum_height(vertical_velocity, gravity):
	return (vertical_velocity ** 2) / (2 * gravity)

#reduced mass
def reduced_mass(mass1, mass2):
	return mass1 * mass2 / (mass1 + mass2)

#tsiolkovsky rocket equation
def tsiolkovsky_rocket_equation(exhaust_velocity, initial_mass, final_mass):
		return exhaust_velocity * math.log(initial_mass / final_mass)


'''
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
print ("Pressure Force / area: ", pressure(500, 1))
print ("Angular Frequency 2 * pi * frequency: ", angular_frequency(28))
print ("Angular Velocity v / r: ", angular_velocity(20, 5))
print ("Gravitational Potential -1 * Gm/ r ", gravitational_potential(6.6725985e-11, 1000, 50))
print ("Gravitational Potential Energy - * Gm1m2 / r: ", gravitational_potential_energy(6.6725985e-11, 6.0e-24, 250, 4.24e-10))
print ("Orbital Speed sqrt (Gm/r): ", orbital_speed(6.6725985e-11, 10, 30))
print ("Escape Speed sqrt (Gm/r): ", escape_speed(6.6725985e-11, 10, 30))
print ("Mach Number velocity / speed of sound: ", mach_number(980.3, 342.62))
print ("Efficiency energy_output / energy_input: % ", efficiency(1000, 2000))
print ("Power work / time: ", power(1000, 10))
print ("Impulse force * time: ", impulse(500, 2))
print ("Torque r * F * sin (angle-degrees): ", torque(1000, 100, 90))
print ("Pendulum Period 2pi * sqrt(L/g): ", pendulum_period(1, 9.80665))
print ("Pendulum Frequency 1/ (2pi * sqrt(L/g)): ", pendulum_frequency(1, 9.80665))
print ("Freefall Speed g * t: ", freefall_speed(9.80665, 10))
print ("Freefall Distance 0.5 * g * t^2: ", freefall_speed(9.80665, 8))
print ("Freefall Time velocity / g: ", freefall_time(78.4532, 9.80665))
print ("Friction Co-efficient friction / force: ", friction_coefficient(500, 10))
print ("Mechanical Advantage of a lever: effort arm length / load arm length: ", mechanical_advantage_lever(10, 2))
print ("Mechanical Advantage of pulleys: number of pulleys * 2: ", mechanical_advantage_pulley(2))
print ("Mechanical Advantage of a screw: pi * (diameter / distance between threads): ", mechanical_advantage_screw(100, 10))
print ("Mechanical Advantage of a wedge: wedge length / wedge thickness: ", mechanical_advantage_wedge(100, 8))
print ("Mechanical Advantage of a ramp: 1 / (ramp height/ ramp length): ", mechanical_advantage_ramp(2, 25))
print ("Mechanical Advantage of wheel and axle: wheel radius / axle radius: ", mechanical_advantage_wheel_axle(40, 20))
print ("Projectile Motion: Horizontal Velocity: v * cos(angle of launch): ", projectile_horizontal_velocity(100, 10))
print ("Projectile Motion: Vertical Velocity: v * sin(angle of launch): ", projectile_vertical_velocity(100, 10))
print ("Projectile Motion: Time of Flight: 2 * vertical velocity / gravity: ", projectile_time_of_flight(17.36482, 9.80665))
print ("Projectile Motion: Range: 2 * horizontal velocity * vertical velocity / gravity: ", projectile_range(98.4808, 17.36482, 9.80665))
print ("Projectile Motion: Maximum Height: vertical velocity^2 / (2 * gravity): ", projectile_maximum_height(17.36482, 9.80665))
print ("Reduced Mass: mass1 * mass2/ mass1 + mass2: ", reduced_mass(1000, 1200))
print ("Tsiolkovsky Rocket Equation: exhaust velocity * log(intial mass / final mass) -> (m/s): ", tsiolkovsky_rocket_equation(1000, 1000, 1))
'''