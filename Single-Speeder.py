# Single-Speeder.py

# TODO:
# - Implement JSON parsing, so you can put the bike config in a JSON file and the program will read it

class Bike():

    # bike needs wheel information when created
    def __init__(self, wheel_size, tire_height, chainring_teeth, cog_teeth, desc):
        self.iso_wheel_size = wheel_size
        self.measured_tire_height = tire_height
        self.wheel_diameter_mm = self.calc_wheel_diameter_mm()
        self.wheel_diameter_inches = self.calc_wheel_diameter_inches()
        self.chainring_tooth_count = chainring_teeth
        self.cog_tooth_count = cog_teeth
        self.desc = desc

    def calc_wheel_diameter_inches(self):
        return ( self.wheel_diameter_mm / 25.4 )

    def calc_wheel_diameter_mm(self):
        return ( self.iso_wheel_size + self.measured_tire_height + self.measured_tire_height )

    def calc_gear_inches(self):
        return ( ( self.wheel_diameter_inches * self.chainring_tooth_count ) / self.cog_tooth_count )

    def calc_distance_traveled(self):
        return ( self.calc_gear_inches() * 3.14 )

    def calc_gear_ratio(self):
        return round( ( self.chainring_tooth_count / self.cog_tooth_count ), 2) 
        
    def calc_speed(self, rpm):
        return round( ( ( ( rpm * self.calc_distance_traveled() ) / 12 ) / 88 ), 2 )

    def get_desc(self):
        return self.desc

bike_configs = {
        "rsd_1": Bike(584, 58, 30, 22, "RSD MiddleChild 650B, 30/22"),
        "rsd_2": Bike(584, 58, 30, 18, "RSD MiddleChild 650B, 30/18"),
        "ict_1": Bike(559, 100, 32, 22, "Surly Ice Cream Truck, 32/22"),
        "ict_2": Bike(559, 100, 28, 23, "Surly Ice Cream Truck, 28/23"),
        "fez_1": Bike(622, 58, 32, 16, "Fezzari La Sal Peak 29er, 32/16")
}

for conf, bike in bike_configs.items():
    print(f"{bike.get_desc()}")
    print(f"\tGear Ratio >> {bike.calc_gear_ratio()} : 1")
    print(f"\tSpeed @ 90 RPM >> {bike.calc_speed(90)}")
    print(f"\tSpeed @ 60 RPM >> {bike.calc_speed(60)}")
    print()
    

