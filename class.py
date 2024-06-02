class Car:
  def __init__(self, brand,model):  
    self.brand = brand
    self.model = model
   
  #some functionality add 
  def fullname(self):
    return f"{self.brand} , {self.model}"
 
# This is Object   
my_car = Car("TATA", "Safari")

print(my_car.model)
print(my_car.brand)
print(my_car.fullname())

new_car = Car("Hero", "CBZ")
print(new_car.brand)
print(new_car.model)
    