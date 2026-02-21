from Lesson_6.oop_vehicles.car_object import carObject
from Lesson_6.oop_vehicles.truck_object import TruckObject

car_1 = carObject('toyota', is_electric=True)
car_2 = carObject('mazda', is_electric=False)
truck_1 = TruckObject('volvo', wheels_amount=8)

# car_price = car_1.price_calculator(470000, 18)
# truck_price = truck_1.price_calculator(300000)
# # if car_price>truck_price:
# #     print('car price is higher than truck price')
# assert car_price > truck_price, "car price is lower than truck price not as expected"
car_1.price_average_calculator([10,50 ,30])
print('the end')
