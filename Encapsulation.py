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
  
  #inheritance---------------

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size
    
  def fuel_type(self):
    return "Electric Charge "
    
my_tesla = ElectricCar("Tesla", "Model s", "85WKH")

safari = Car("TaTa", "Safari")
print(my_tesla.fuel_type())
print(safari.fuel_type())


   
 

  