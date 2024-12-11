from modules.mylib import food

print(food.name)
food.cook()
food.eat()

from modules.mylib.food import cook, eat, name

print(name)
cook()
eat()

import calc_module
print(calc_module.add(1,2))

import bbb.cm2
print(bbb.cm2.add(1,2))