def high_and_low(numbers):
    numberlist = sorted([int(x) for x in numbers.split(" ")])
    return f'{int(numberlist[-1])} {int(numberlist[0])}'


# good practice
# def high_and_low(numbers):
#     nums = sorted(numbers.split(), key=int)
#     return '{} {}'.format(nums[-1], nums[0])
