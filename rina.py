#VARIABLES AND NAMES
#from array import typecodes
#from typing_extensions import runtime


Cars = 100
Space_in_a_car = 4.0
Drivers = 30
Passengers = 90
Cars_not_driven = "Cars_drivers"
Cars_driven = "Drivers"
Carpool_capacity = "cars_driven * Space_in_a_car"
Average_passengers_per_car = "passenger/cars_driven"


print("There are ", Cars, " cars available.")
print("There are only", Drivers, "drivers available")
print( "There will be", Cars_not_driven, "empty cars today.")
print("We can transport", Carpool_capacity, "people today.")
print("We have", Passengers, "to carpool today")
print("We need to put about", Average_passengers_per_car, "in each car")



my_name = 'Zed A . shaw'
my_age = 35 #not alie
my_height = 74 #inches
my_weight = 180 #Ibs
my_eyes ='Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Lets talk about {my_name}")
print(f"He's {my_height} inches tall")
print(f"He's {my_weight} pounds heavy")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usally {my_teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age} + {my_height} + {my_weight} I get {total}.")


w = "This is the left side of...."
e = "a string with a right side"

