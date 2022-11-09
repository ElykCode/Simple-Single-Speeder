# Single-Speeder.py

# TODO:
# - Implement JSON parsing, so you can put the bike config in a JSON file and the program will read it

class Bike():

    # bike needs wheel and chainring/cog information when created
    def __init__(self, wheel_size, tire_height, chainring_teeth, cog_teeth, desc):
        self.iso_wheel_size = float(wheel_size)
        self.measured_tire_height = float(tire_height)
        self.wheel_diameter_mm = self.calc_wheel_diameter_mm()
        self.wheel_diameter_inches = self.calc_wheel_diameter_inches()
        self.chainring_tooth_count = int(chainring_teeth)
        self.cog_tooth_count = int(cog_teeth)
        self.desc = desc

    # used to calculate gear inches later
    def calc_wheel_diameter_inches(self):
        return ( self.wheel_diameter_mm / 25.4 )

    # used to calculate wheel diameter in inches
    def calc_wheel_diameter_mm(self):
        return ( self.iso_wheel_size + self.measured_tire_height + self.measured_tire_height )

    # used to calculate distance traveled for every time the cranks go around
    def calc_gear_inches(self):
        return ( ( self.wheel_diameter_inches * self.chainring_tooth_count ) / self.cog_tooth_count )

    # used to calculate speed
    def calc_distance_traveled(self):
        return ( self.calc_gear_inches() * 3.14 )

    # gear ratio is a handy single number to compare cogs on the same bike
    def calc_gear_ratio(self):
        return round( ( self.chainring_tooth_count / self.cog_tooth_count ), 2) 

    # calculates bike speed at a given RPM using the RPM and
    # the distance traveled per one crank revolution
    def calc_speed(self, rpm):
        return round( ( ( ( rpm * self.calc_distance_traveled() ) / 12 ) / 88 ), 2 )

    # it's sometimes handy to have a bike description
    def get_desc(self):
        return self.desc

# Program Description
print("Welcome to Single-Speeder, the single speed bike calculator")
print("You will enter bike data next...\n")

# list of bikes
bikes_list = []

# Menu loop
user_input = "y"
counter = 1
while user_input.lower() != "n":
    # get wheel size
    user_input = input(f"Enter the ISO wheel size in mm for bike {counter}: ")
    # filter out empty and non-integer input
    if user_input and user_input.isdigit():
        wheel_size = user_input
    else:
        break

    # get tire height
    user_input = input(f"Enter the tire height in mm for bike {counter}: ")
    # filter out empty and non-integer input
    if user_input and user_input.isdigit():
        tire_height = user_input
    else:
        break

    # get chainring size
    user_input = input(f"Enter the number of teeth on the front chainring for bike {counter}: ")
    # filter out empty and non-integer input
    if user_input and user_input.isdigit():
        chainring_teeth = user_input
    else:
        break

    # get cog size
    user_input = input(f"Enter the number of teeth on the rear cog for bike {counter}: ")
    # filter out empty and non-integer input
    if user_input and user_input.isdigit():
        cog_teeth = user_input
    else:
        break

    # get bike description
    user_input = input(f"Enter the short description for bike {counter}: ")
    # filter out empty input
    if user_input:
        bike_desc = user_input
    else:
        break

    # add bike to list
    bikes_list.append( Bike(wheel_size, tire_height, chainring_teeth, cog_teeth, bike_desc) )

    # check if user wants to enter another bike:
    user_input = input("Do you want to enter another bike? (Y/N): ")
    print()

    # increment counter
    counter += 1

# iterate through bikes
for bike in bikes_list:
    print()
    print(f"{bike.get_desc()}")
    print(f"\tGear Ratio >> {bike.calc_gear_ratio()} : 1")
    print(f"\tSpeed @ 90 RPM >> {bike.calc_speed(90)}")
    print(f"\tSpeed @ 60 RPM >> {bike.calc_speed(60)}")
