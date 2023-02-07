# Getting Ready for Physics Class Project

# Uncomment this when you reach the "Use the Force" section
# train_mass = 22680
# train_acceleration = 10
# train_distance = 100
# bomb_mass = 1


# # Write your code below:
# def f_to_c(f_temp):
#     c_temp = (f_temp - 32) * 5/9
#     return c_temp
#
# f100_in_celsius = f_to_c(100)
#
# def c_to_f(c_temp):
#     f_temp = c_temp * (9/5) + 32
#     return f_temp
#
# c0_in_fahrenheit = c_to_f(0)
#
# def get_force(mass, acceleration):
#     force = mass * acceleration
#     return force
#
# train_force = get_force(2000, 60)
# print(train_force)
#
# print("The GE train supplies " + str(train_force) + " Newtons of force.")
#
# def get_energy(mass, c = 3 * 10 ** 8):
#     energy = mass * c ** 2
#     return  energy
#
# bomb_mass = 1000
# bomb_energy = get_energy(bomb_mass)
# print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")
#
# def get_work(mass, acceleration, distance):
#     work = get_force(mass, acceleration) * distance
#     return work
#
# train_mass = 50000
# train_acceleration = 20
# train_distance = 3000
# train_work = get_work(train_mass, train_acceleration, train_distance)
# print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
# print(train_mass)

# code challenges
# 1. Large Power
# Write your large_power function here:
def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False




