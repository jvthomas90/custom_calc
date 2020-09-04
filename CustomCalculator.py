# E=mC^2
cSpeed = 299792458 # Distance (in meters) light travels in a vacuum, in a second, per-second i.e. expressed in m/s/s or m/(s^2) notation.
mass = float(input("Enter mass in kg (kilograms) >>> "))
energy = mass*(cSpeed**2)  # Einstein's mass-energy equivalence formula
print("e = m(c^2) therefore your object has %d J (joules of energy)" % energy) # Check Energy units

# space-time fluidity, according to the Einstein's theories of relativity

percent_of_c = float(input("Enter a number between 0.000001 and 99.99999999999999: "))
travel_distance =  float(input("Enter a distance in light years: "))

import math
# Lorentz/length contraction formula
distance_lambda = travel_distance * math.sqrt(1 - ((percent_of_c * percent_of_c) / (100 * 100)))

time_measured_fromEarth = travel_distance * (100 / percent_of_c)
time_measured_fromCraft = distance_lambda / (percent_of_c * .01)

print(f"The distance is dilated to  {distance_lambda} light years.")
print(f"The journey time, as viewed from earth, is {time_measured_fromEarth} years")
print(f"The journey time, as viewed from the spaceship is {time_measured_fromCraft} years")