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

safari = Car("TaTa", "Safari")
my_car = Car("Tata", "safari")
Car("Tata", "Nexon")

# print(my_tesla.fuel_type())
# print(safari.fuel_type())
print(my_car.general_description())
print(Car.general_description())


   
 

  