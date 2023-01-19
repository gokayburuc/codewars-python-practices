# def accum(s):
#     counter = 1
#     vals = []
#     for x in s:
#         val = (x * counter).title()
#         counter += 1
#         vals.append(val)
#     return "-".join(vals)


def accum(s):
    return "-".join([str((x+1)*y).title() for x, y in enumerate(s)])
