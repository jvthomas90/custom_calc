def welcome():
    print('''▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░▄▄▀█░▄▄█▄░▄█░▄▄▀█▀▄▄▀█▀▄▄▀█░████░██░█░▄▄██▄██▀▄▀█░▄▄
█░▀▀░█▄▄▀██░██░▀▀▄█░██░█░▀▀░█░▄▄░█░▀▀░█▄▄▀██░▄█░█▀█▄▄▀
█░██░█▄▄▄██▄██▄█▄▄██▄▄██░████▄██▄█▀▀▀▄█▄▄▄█▄▄▄██▄██▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█░▄▄▀█░██▀▄▀█░██░█░██░▄▄▀█▄░▄█▀▄▄▀█░▄▄▀█░█░█░
██░████░▀▀░█░██░█▀█░██░█░██░▀▀░██░██░██░█░▀▀▄█▄█▄█▄
██░▀▀▄█▄██▄█▄▄██▄███▄▄▄█▄▄█▄██▄██▄███▄▄██▄█▄▄█▀█▀█▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n\n\n''')

def chooose():
    while True:
        choice = input("\nSelect one: 'emc2' or 'spacetime' >> ")
        if choice in ("emc2", "spacetime"):
            if choice == "emc2":
                print("\nYou've chosen to calculate the energy in an object!\n")
                calc_emc2()
            elif choice == "spacetime":
                print("\nYou've chosen to calculate relativistic effects!\n")
                calc_spacetime()
            break
        else:
            print("\n🅧  Invalid input :(\n")

def calc_emc2(): # E = m*(C^2)
    cSpeed = 299792458 # Distance (in meters) light travels in a vacuum, in a second, per-second i.e. expressed in m/s/s or m/(s^2) notation.
    mass = float(input("Enter mass in kg (kilograms) >>> "))
    energy = mass*(cSpeed**2)  # Einstein's mass-energy equivalence formula
    print("\nSince e = m(c^2) your object has %d J (joules of energy)" % energy) # Check Energy units

# space-time fluidity, according to the Einstein's theories of relativity
def calc_spacetime():
    percent_of_c = float(input("Non-FTL 'warpspeed' (enter a value between 0.000001 and 99.99999999999999): "))
    if percent_of_c >= 100:
        raise ValueError("Where'd you get your dilithium crystals at fam? Hook me up! Till then, I can't calculate speeds faster than light!!! #SorryNotSorry")
    travel_distance =  float(input("\nEnter distance to destination in light years: "))

    import math
    # Lorentz/length contraction formula
    distance_lambda = travel_distance * math.sqrt(1 - ((percent_of_c * percent_of_c) / (100 * 100)))

    time_measured_fromEarth = travel_distance * (100 / percent_of_c)
    time_measured_fromCraft = distance_lambda / (percent_of_c * .01)

    print(f"\nThe distance is dilated to  {distance_lambda} light years.")
    print(f"The journey time, as viewed from earth, is {time_measured_fromEarth} years")
    print(f"The journey time, as viewed from the spaceship is {time_measured_fromCraft} years")

def again():
    calc_again = input("\nDo you want to calculate again?\nPlease type Y for YES or N for NO. >> ")
    if calc_again.upper() == 'Y':
        chooose()
    elif calc_again.upper() == 'N':
        exit
    else:
        again()

welcome()
chooose()
again()
