import math


# def mango(quantity, price):
#     total = 0
#     if quantity >= 3:
#         # one mango free
#         total = (quantity-math.floor(quantity / 3)) * price
#     else:
#         total = price * quantity
#     return total
#     pass


# shorthand
def mango(quantity, price):
    return ((quantity-math.floor(quantity / 3)) * price) if quantity >= 3 else price * quantity
