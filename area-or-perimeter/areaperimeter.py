# def area_or_perimeter(l, w):
#     if l == w:
#         answer = pow(l, 2)
#     else:
#         answer = 2 * (l+w)

#     return answer


# shorthand solution
# def area_or_perimeter(l, w):
#     return pow(l, 2) if l == w else 2*(l+w)


# lambda solution
def area_or_perimeter(a, b): return a * b if a == b else 2 * (a + b)
# area_or_perimeter = lambda a, b : a * b if a == b else 2 * (a + b)
