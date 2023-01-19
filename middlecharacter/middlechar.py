def get_middle(s):
    return s[int(len(s)/2)] if len(s) % 2 != 0 else s[int(len(s)/2)-1:int(len(s)/2)+1]

# divmod solution
# def get_middle(s):
#     index, odd = divmod(len(s), 2)
#     return s[index] if odd else s[index - 1:index + 1]


s = "esin"
index, odd = divmod(len(s), 2)
print(index)
print(odd)
