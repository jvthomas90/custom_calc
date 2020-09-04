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

# Decide which calculation formula to work with
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

# E = m*(C^2)
def calc_emc2():
    cSpeed = 299792458 # Distance (in meters) light travels in a vacuum, in a second, per-second i.e. expressed in m/s/s or m/(s^2) notation.
    mass = float(input("Enter mass in kg (kilograms) >>> "))
    energy = mass*(cSpeed**2)  # Einstein's mass-energy equivalence formula
    print("\nSince e = m(c^2) your object has %d J (joules of energy)" % energy)


# space-time fluidity, according to the Einstein's theories of relativity
def calc_spacetime():
    percent_of_c = float(input("Non-FTL 'warpspeed' (enter a value between 0.000001 and 99.99999999999999): "))
    if percent_of_c >= 100:
        raise ValueError("Where'd you get your dilithium crystals at fam? Hook me up! Till then, I can't calculate speeds faster than light!!! #SorryNotSorry")
    travel_distance =  float(input('''
How far are you willing to travel at that sub-light speed? For reference: 
    
    - The distance from Earth to Alpha and Proxima Centauri is 4.37 light years, or 41,343,000,000,000 kilometres (25,690,000,000,000 miles). Even our nearest stellar neighbour is very far away…

    - Or the red giant Betelguse, one of the largest stars that can be seen with the naked eye (located on the "belt" of the constellation of stars known as "Orion") is 640 light years away...

    - The centre of the Milky Way: Our galaxy, the Milky Way, is about 100,000 light years across. The Sun lies on the Sagittarius arm and is about 26,000 light years from the centre, which very likely contains a supermassive black hole (you know, if you ever feel like visiting *shrug*)

    - Anderomeda is simultaneously our nearest galactic neighbor as well as the furthest object that most people can see with the naked eye. This galaxy twice the size of the Milky Way is 2,500,000 light years away!
    
    - The furthest known galaxy (as of March 2016) goes by the name of GN-z11. It’s around 13.4 billion light years away (13,400,000,000 light years).
    
Bearing the above in mind, please enter the distance to your destination in light-years >> '''))

    import math
    # Lorentz/length contraction formula
    distance_lambda = travel_distance * math.sqrt(1 - ((percent_of_c * percent_of_c) / (100 * 100)))

    time_measured_fromEarth = travel_distance * (100 / percent_of_c)
    time_measured_fromCraft = distance_lambda / (percent_of_c * .01)

    print(f"\nThe distance is dilated to  {distance_lambda} light years.")
    print(f"The journey time, as viewed from earth, is {time_measured_fromEarth} years")
    print(f"The journey time, as viewed from the spaceship is {time_measured_fromCraft} years")

#prompt user to rerun program from choose() function's decision tree logic
def again():
    calc_again = input("\nDo you want to calculate again?\nPlease type Y for YES or N for NO. >> ")
    if calc_again.upper() == 'Y':
        chooose()
    elif calc_again.upper() == 'N':
        print("\nFarewell and godspeed, interstellar voyager!!!\n")
        exit
    else:
        again()

#main function calls
welcome()
chooose()
again()
