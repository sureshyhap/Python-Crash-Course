class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() +
              ". We sell " + self.cuisine_type + " food.")
    def open_restaurant(self):
        print("The restaurant is now open!")


restaurant = Restaurant("gaby's", "italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("szechuan kitchen", "chinese")
restaurant2 = Restaurant("shogun", "japanese")
restaurant3 = Restaurant("mcdonald's", "american")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
