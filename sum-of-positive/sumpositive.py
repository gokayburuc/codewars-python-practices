# def positive_sum(arr):
#     sum = 0
#     for x in arr:
#         # shorthand
#         if x <= 0:
#             pass
#         else:
#             sum += x
#     return sum


def positive_sum(arr):
    return sum(x for x in arr if x >= 0)


# def positive_sum(arr):
#     return sum(x for x in arr if x > 0)
