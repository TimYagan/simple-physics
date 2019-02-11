#MIT License

#Copyright (c) 2019 Tim Yagan

import math

#celsius to kelvin
def celcius_to_kelvin(celsius):
	return celsius + 273.15

#kelvin to celsius
def kelvin_to_celsius(kelvin):
	return kelvin - 273.15


#sensible heat
def sensible_heat(mass, specific_heat_capacity, temperature_change):
	return mass * specific_heat_capacity * temperature_change

#specific latent heat - energy needed at the point of a phase change
def specific_latent_heat(mass, specific_latent_capacity):
	return mass * specific_latent_capacity

print("Sensible Heat: Q = m * c * delta T: -> joules ", sensible_heat(1, 753, 220))
print("Specific Latent Heat: Q = m * specific latent capacity: -> joules ", specific_latent_heat(1, 2258))