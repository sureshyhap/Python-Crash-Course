class Restaurant():
    """Simulates a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() +
              ". We sell " + self.cuisine_type + " food.")
        
    def open_restaurant(self):
        print("The restaurant is now open!")

    def set_number_served(self, number_served):
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print("Can't have less number served!")

    def increment_number_served(self, increment):
        if increment >= 0:
            self.number_served += increment
        else:
            print("Can't have negative increment!")


restaurant = Restaurant("gaby's", "italian")
print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(20)
print(restaurant.number_served)
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
