#MIT License

#Copyright (c) 2019 Tim Yagan

import math

#celsius to kelvin
def celsius_to_kelvin(celsius):
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

#ideal gas law - functional thermodynamics
def ideal_gas_law_ft(number_of_moles, gas_constant, absolute_temperature):
	return number_of_moles * gas_constant * absolute_temperature

#ideal gas law - functional thermodynamics - pressure
def ideal_gas_law_ft_pressure(volume, number_of_moles, gas_constant, absolute_temperature):
	return (number_of_moles * gas_constant * absolute_temperature) / volume

#ideal gas law - functional thermodynamics - volume
def ideal_gas_law_ft_volume(pressure, number_of_moles, gas_constant, absolute_temperature):
	return (number_of_moles * gas_constant * absolute_temperature) / pressure

#ideal gas law - functional thermodynamics - moles
def ideal_gas_law_ft_moles(pressure, volume, gas_constant, absolute_temperature):
	return (pressure * volume) / (gas_constant * absolute_temperature)

#ideal gas law - functional thermodynamics - temperature
def ideal_gas_law_ft_temperature(pressure, volume, number_of_moles, gas_constant):
	return (pressure * volume) / (number_of_moles * gas_constant)

'''
print ("Sensible Heat: Q = m * c * delta T: ", sensible_heat(1, 753, 220))
print ("Specific Latent Heat: Q = m * specific latent capacity: ", specific_latent_heat(1, 2258))
print ("Ideal Gas Law - Functional Thermodynamics: PV = nRT: ", ideal_gas_law_ft(1, 8.314, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Functional Thermodynamics: PV = nRT - pressure: ", ideal_gas_law_ft_pressure(1.0, 2.0, 8.314, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Functional Thermodynamics: PV = nRT - volume: ", ideal_gas_law_ft_volume(4874.4982, 2.0, 8.314, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Functional Thermodynamics: PV = nRT - moles: ", ideal_gas_law_ft_moles(4874.4982, 1.0, 8.314, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Functional Thermodynamics: PV = nRT - temperature: ", ideal_gas_law_ft_temperature(4874.4982, 1.0, 2.0, 8.314))
'''