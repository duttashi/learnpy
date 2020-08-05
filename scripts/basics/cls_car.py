# Exercise: Create a Car class
# Create a Car class with two instance attributes:

# .color, which stores the name of the car’s color as a string
# .mileage, which stores the number of miles on the car as an integer
# Then instantiate two Car objects—a blue car with 20,000 miles 
# and a red car with 30,000 miles—and print out their colors and mileage.
# Reference: https://realpython.com/python3-object-oriented-programming/#check-your-understanding

# Parent class
class Automobile():
    
    def __init__(self, Type, seat_capacity):
        self.Type = Type
        self.seat_capacity = seat_capacity
        
    def properties(self):
        print("The automobile is of Type ", self.Type, 
              "and it has a seating capacity of ", self.seat_capacity, " seats")

# child class
class Car(Automobile):
    
    def __init__(self, color, mileage):
        # Attributes
        self.color = color
        self.mileage = mileage
        
    # OPERATION/ACTIONS/METHODS
    def showCarProperties(self):
        print("The car color is ", self.color, 
              "and car mileage is ", self.mileage)
        
# INSTANTIATE CLASS OBJECTS
blue_car = Car("Blue", 20000)
#blue_car.properties("Wagon",4)
blue_car.showCarProperties()

red_car = Car("red", 30000)
red_car.showCarProperties()

        

        
        