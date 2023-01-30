from datetime import datetime
import random
from matplotlib import pyplot as plt
from decimal import Decimal

# current_time = datetime.now()
# print(current_time)
#
# random_list = []
# random_list = [random.randint(1, 100) for i in range(101)]
# print(random_list)
# randomer_number = random.choice(random_list)
# print(randomer_number)
#
# numbers_a = range(1, 13)
# for n in numbers_a:
#     print(n)
# numbers_b = [random.randint(1, 1000) for n in numbers_a]
# print(numbers_b)
# plt.plot(numbers_a, numbers_b)
# plt.show()

# Fix the floating point math below:
two_decimal_points = Decimal("0.2") + Decimal ("0.69")
print(two_decimal_points)

four_decimal_points = Decimal("0.53") * Decimal("0.65")
print(four_decimal_points)
