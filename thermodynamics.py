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

##################################
#ideal gas law - statistical thermodynamics
def ideal_gas_law_st(number_of_moles, boltzmann_constant, absolute_temperature):
	return number_of_moles * boltzmann_constant * absolute_temperature

#ideal gas law - statistical thermodynamics - pressure
def ideal_gas_law_st_pressure(volume, number_of_moles, boltzmann_constant, absolute_temperature):
	return (number_of_moles * boltzmann_constant * absolute_temperature) / volume

#ideal gas law - statistical thermodynamics - volume
def ideal_gas_law_st_volume(pressure, number_of_moles, boltzmann_constant, absolute_temperature):
	return (number_of_moles * boltzmann_constant * absolute_temperature) / pressure

#ideal gas law - statistical thermodynamics - moles
def ideal_gas_law_st_moles(pressure, volume, boltzmann_constant, absolute_temperature):
	return (pressure * volume) / (boltzmann_constant * absolute_temperature)

#ideal gas law - statistical thermodynamics - temperature
def ideal_gas_law_st_temperature(pressure, volume, number_of_moles, boltzmann_constant):
	return (pressure * volume) / (number_of_moles * boltzmann_constant)


#solid expansion - length
def solid_expansion_length(initial_length_of_solid, solid_coefficient, change_in_temperature):
	return initial_length_of_solid * solid_coefficient * change_in_temperature

#solid expansion - area
def solid_expansion_area(initial_area_of_solid, solid_coefficient, change_in_temperature):
	return 2 * solid_coefficient * initial_area_of_solid * change_in_temperature

#solid expansion - volume
def solid_expansion_volume(initial_volume, solid_coefficient, change_in_temperature):
	return 3 * solid_coefficient * initial_volume * change_in_temperature

#liquid expansion
def liquid_expansion(initial_volume, liquid_coefficient, change_in_temperature):
	return liquid_coefficient * initial_volume * change_in_temperature

'''
print ("Sensible Heat: Q = m * c * delta T: ", sensible_heat(1, 753, 220))
print ("Specific Latent Heat: Q = m * specific latent capacity: ", specific_latent_heat(1, 2258))

print ("Ideal Gas Law - Functional Thermodynamics: PV = nRT: ", ideal_gas_law_ft(1, 8.314, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Functional Thermodynamics: PV = nRT - pressure: ", ideal_gas_law_ft_pressure(1.0, 2.0, 8.314, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Functional Thermodynamics: PV = nRT - volume: ", ideal_gas_law_ft_volume(4874.4982, 2.0, 8.314, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Functional Thermodynamics: PV = nRT - moles: ", ideal_gas_law_ft_moles(4874.4982, 1.0, 8.314, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Functional Thermodynamics: PV = nRT - temperature: ", ideal_gas_law_ft_temperature(4874.4982, 1.0, 2.0, 8.314))

print ("Ideal Gas Law - Statistical Thermodynamics: PV = nRT: ", ideal_gas_law_st(1, 8.314, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Statistical Thermodynamics: PV = nRT - pressure: ", ideal_gas_law_st_pressure(1.0, 2.0, 1.382 * 10 ** -23, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Statistical Thermodynamics: PV = nRT - volume: ", ideal_gas_law_st_volume(4874.4982, 2.0, 1.382 * 10 ** -23, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Statistical Thermodynamics: PV = nRT - moles: ", ideal_gas_law_st_moles(4874.4982, 1.0, 1.382 * 10 ** -23, celsius_to_kelvin(20)))
print ("Ideal Gas Law - Statistical Thermodynamics: PV = nRT - temperature: ", ideal_gas_law_st_temperature(4874.4982, 1.0, 2.0, 1.382 * 10 ** -23))

print ("Solid Expansion - length: intial length * expansion coefficient * change in temperature: ", solid_expansion_length(0.01, 19 * (10**-6), 10))
print ("Solid Expansion - area: intial area * expansion coefficient * change in temperature: ", solid_expansion_area(2, 19 * (10**-6), 10))
print ("Solid Expansion - volume: intial volume * expansion coefficient * change in temperature: ", solid_expansion_volume(2, 19 * (10**-6), 10))

print ("Liquid Expansion - volume: initial volume * expansion coefficient * change in temperature: ", liquid_expansion(20, 457 * (10**-6), 50))
'''