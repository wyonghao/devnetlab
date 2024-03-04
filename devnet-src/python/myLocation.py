# Define a class with variables for **name** and **country**.
# Then define a method that belongs to the class. The method’s
# purpose is to print a sentence that uses the variables.
class Location:
    def __init__(self, name, country):
       self.name = name
       self.country = country
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " +
self.country + ".")
# First instantiation of the Location class
loc1 = Location("Tomas", "Portugal")
# Call a method from the instantiated class
loc1.myLocation()
# Three more instantiations and method calls for the Location class
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
loc2.myLocation()
loc3.myLocation()
your_loc = Location("Your_Name", "Your_Country")
your_loc.myLocation()