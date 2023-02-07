# # learn type function
# print(type(5))
# my_dict = {}
# print(type(my_dict))
# my_list = []
# print(type(my_list))
#
#
# # create a new class
# class Facade:
#     pass
#
#
# facade_1 = Facade()
# facade_1_type = type(facade_1)
# print(facade_1_type)
#
#
# # create another class
# class Rules:
#     def washing_brushes(self):
#         return "Point bristles towards the basin while washing your brushes."
#
#
# # create another class
# class Circle1:
#     pi = 3.14
#
#     def area(self, radius):
#         return Circle1.pi * radius ** 2
#
#
# circle = Circle1()
#
# pizza_area = circle.area(12 / 2)
# teaching_table_area = circle.area(36 / 2)
# round_room_area = circle.area(11460 / 2)
#
#
# # create a class with a constructor
# class Circle:
#     pi = 3.14
#
#     def __init__(self, diameter):
#         print("Creating circle with diameter {d}".format(d=diameter))
#         self.radius = diameter / 2
#
#     def circumference(self):
#         return 2 * self.pi * self.radius
#
#     def __repr__(self):
#         return "Circle with radius {}".format(self.radius)
#
#
# medium_pizza = Circle(12)
# teaching_table = Circle(36)
# round_room = Circle(11460)
#
# print(medium_pizza.circumference())
# print(teaching_table.circumference())
# print(round_room.circumference())
#
# print(medium_pizza)
# print(teaching_table)
# print(round_room)
#
#
# # checking and getting attributes
# # can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
# #
# # for element in can_we_count_it:
# #     if hasattr(element, 'count') is True:
# #         print(str(type(element)) + " has the count attribute!")
# #     else:
# #         print(str(type(element)) + " does not have the count attribute :(")
# #
# # # everything is an Object
# # print(dir(5))
# #
# #
# # def this_function_is_an_object():
# #     return "something"
#
#
# # print(dir(this_function_is_an_object))
#
#
# # Review
# class Student:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#         self.grades = []
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#
# roger = Student('Roger van der Weyden', 10)
# sandro = Student('Sandro Botticelli', 12)
# pieter = Student('Pieter Bruegel the Elder', 8)
#
#
# class Grade:
#     minimum_passing = 65
#
#     def __init__(self, score):
#         self.score = score
#
#
# pieters_grade = Grade(100)
# pieter.add_grade(pieters_grade.score)
#
# print(pieter.grades[0])

# Basta Fazoolin' Project


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return 'The address is {}'.format(self.address)

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return 'The {} menu is available from {} to {}'.format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill

# create Menu objects
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)

dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids_menu = Menu('Kids', kids_items, 1100, 2100)

# create array of menus
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

# try calculate_bill function
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# create Franchise objects
flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Stree', menus)

# create array of franchises
franchises = [flagship_store, new_installment]

# try available_menus objects
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

# create first business object
first_business = Business('Basta Fazoolin\' with my Heart', franchises)

# create new franchise info
arepas_menu_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu('Take a\' Arepa', arepas_menu_items, 1000, 2000)

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

new_business = Business('Take a\' Arepa', [arepas_place])

print(new_business.franchises[0].menus[0])
print('For the new_installment restaurant {}. {}'.format(first_business.franchises[0], first_business.franchises[0].menus[2]))

