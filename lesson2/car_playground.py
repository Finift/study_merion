from lesson2.classes.car import Car
from lesson2.classes.engine import Engine

car1 = Car()
car1.brand = "BMW"
car1.model = "3"
car1.year = 2022
car1.color = "blue"
car1.is_for_sale
car1.engine = Engine()
car1.engine.vol = 2.0
car1.engine.hp = 170
car1.engine.fuel_type = "oil"

print(car1.engine.hp)

car2 = Car()
car2.brand = "VW"
car2.engine = Engine()
car2.engine.vol = 0
car2.engine.hp = 130
car2.engine.fuel_type = "electro"

print(car2.brand, car2.model, car2.color, car2.engine.hp, car2.engine.vol)
