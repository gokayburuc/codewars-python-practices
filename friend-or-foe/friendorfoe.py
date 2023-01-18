# def friend(x):
#     friendlist = []
#     for person in x:
#         if len(person) == 4 and str(person).isalpha() == True:
#             friendlist.append(person)
#         else:
#             pass
#     return friendlist
#     # Code


# shorthand
def friend(x):
    return [friend for friend in x if len(friend) == 4 and str(friend).isalpha() == True]
