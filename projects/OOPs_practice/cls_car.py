# Exercise: Create a Car class
# Create a Car class with two instance attributes:

# .color, which stores the name of the car’s color as a string
# .mileage, which stores the number of miles on the car as an integer
# Then instantiate two Car objects—a blue car with 20,000 miles 
# and a red car with 30,000 miles—and print out their colors and mileage.

class Car():
    
    def __init__(self, color, mileage):
        # Attributes
        self.color = color
        self.mileage = mileage
        
    # OPERATION/ACTIONS/METHODS
    def show_care_properties(self):
        print("The car color is ", self.color, 
              "and car mileage is ", self.mileage)
        
# INSTANTIATE CLASS OBJECTS
blue_car = Car("Blue", 20000)
blue_car.show_care_properties()

red_car = Car("red", 30000)
red_car.show_care_properties()

        

        
        