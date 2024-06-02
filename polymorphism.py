class Car:
  def __init__(self, brand,model):  
    self.__brand = brand
    self.model = model
    
  def get_brand(self):
    return self.__brand + "! "
   
  #some functionality add 
  def fullname(self):
    return f"{self.brand} , {self.model}"
  
  #inheritance---------------

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size
    
my_tesla = ElectricCar("Tesla", "Model s", "85WKH")
# print(my_tesla.model)
# print(my_tesla.brand)
# print(my_tesla.battery_size)
# print(my_tesla.fullname())

#private value access 
print(my_tesla.get_brand())
    
   
 

  