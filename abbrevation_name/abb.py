def abbrev_name(name):
    names = name.upper().split()
    abbrevation = [names[0][0], ".", names[1][0]]
    abb = "".join(abbrevation)
    print(abb.strip())
    return abb

# best solution

# def abbrevName(name):
#     return '.'.join(w[0] for w in name.split()).upper()
