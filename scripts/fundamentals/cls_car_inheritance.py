# Exercise: Create a Car class
# Create a Car class with two instance attributes:

# .color, which stores the name of the car’s color as a string
# .mileage, which stores the number of miles on the car as an integer
# Then instantiate two Car objects—a blue car with 20,000 miles 
# and a red car with 30,000 miles—and print out their colors and mileage.
# Reference: https://realpython.com/python3-object-oriented-programming/#check-your-understanding

# Parent class
class Automobile():
    
    def __init__(self, auto_type, seat_capacity):
        self.auto_type = auto_type
        self.seat_capacity = seat_capacity
        #print("This is an Automobile")
        
    def automobile_type(self):
        print("I am an automobile of ",self.auto_type, " type!")
    
    def automobile_property(self):
        print("I have a seating capacity of ", self.seat_capacity, "seats")

# child class
class Car(Automobile):
    
    def __init__(self, color, mileage):
        
        # call the parent class
        Automobile.__init__(self, color, mileage)
        
        # print("In Car class")
        # Attributes
        self.color = color
        self.mileage = mileage
        
    # OPERATION/ACTIONS/METHODS
    def show_car_property(self):
        print("My color is ", self.color, 
              "and my mileage is ", self.mileage)
        
# INSTANTIATE CLASS OBJECTS
blue_car = Automobile("Wagon", 4)
blue_car.automobile_type()
blue_car.automobile_property()
blue_car = Car("Blue", 20000)
blue_car.automobile_type()
blue_car.show_car_property()

# red_car = Car("red", 30000)
# red_car.show_car_property()

        

        
        