class Car:
  def __init__(self, brand,model):  
    self.__brand = brand
    self.model = model
    
  def get_brand(self):
    return self.__brand + "! "
   
  #some functionality add 
  def fullname(self):
    return f"{self.brand} , {self.model}"
  
  def fuel_type(self):
    return "petrol or Diesel"
  
  @staticmethod
  def general_description():
    return "Car are means of transport "
  
  #inheritance---------------

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size
    
  def fuel_type(self):
    return "Electric Charge "
    
my_tesla = ElectricCar("Tesla", "Model s", "85WKH")


# Multiple Inheritance use 

class Battery:
  def battery_info(self):
    return "this is battery"
  
class Engine:
  def engine_info(self):
    return "this is Engine Info"
  
class ElectricCarTwo(Battery, Engine, Car):
  pass

my_new_tesla = ElectricCarTwo("Tesla", "Model s")


print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())

   
 

  