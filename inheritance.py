class Car:
  def __init__(self, brand,model):  
    self.brand = brand
    self.model = model
   
  #some functionality add 
  def fullname(self):
    return f"{self.brand} , {self.model}"
  
  #inheritance---------------

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size
    
my_tesla = ElectricCar("Tesla", "Model s", "85WKH")
print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.battery_size)
print(my_tesla.fullname())
    
   
 
# This is Object   
# my_car = Car("TATA", "Safari")

# print(my_car.model)
# print(my_car.brand)
# print(my_car.fullname())

# new_car = Car("Hero", "CBZ")
# print(new_car.brand)
# print(new_car.model)
    
  