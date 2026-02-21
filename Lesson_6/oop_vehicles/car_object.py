from Lesson_6.oop_vehicles.vehicle_parent import vehicleParent


class carObject(vehicleParent):
    def __init__(self,brand,is_electric):
        self.brand = brand
        self.is_electric = is_electric
    def buttery_availblable(self,capacity,ussage):
        capacity_in_hours=10
        if (self.is_electric):
            print('trying to calculate the availableof buttery')
            remaining_capacity=capacity-ussage
            return remaining_capacity
        else:
            return -1
    def price_average_calculator(self, prices):
        avg_price=0
        for price in prices:
           avg_price=avg_price+price
        avg_price=avg_price/len(prices)
        print (avg_price)
        return avg_price





