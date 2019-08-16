class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() +
              ". We sell " + self.cuisine_type + " food.")
    def open_restaurant(self):
        print("The restaurant is now open!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)


restaurant = Restaurant("gaby's", "italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

ice_cream_stand = IceCreamStand("Carvel", "Ice Cream", ["chocolate, vanilla"])
ice_cream_stand.show_flavors()
