class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nMy restaurant is %s ,\nCuisine type is %s。"
              % (self.restaurant_name,
                 self.cuisine_type))
    def open_restaurant(self):
        print("\nIs time to open restaurant!")


class IceCreamSteand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ["Hami melon","vanilla","cream"]

    def print_menu_of_flavors(self):
        print("Here are the ingredients for the ice cream:")
        for every_flavors in self.flavors:
            print(every_flavors)


myicecream = IceCreamSteand("ailce house","Ice cream shop")
myicecream.print_menu_of_flavors()
