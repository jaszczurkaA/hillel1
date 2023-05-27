
lst = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number = 35

def get_pairs(lst, number):
    pairs = []
    for x in range(len(lst)):
        for y in range(x+1, len(lst)):
            if lst[x] + lst[y] == number:
                pairs.append((lst[x], lst[y]))
                pairs.append((lst[y], lst[x]))
    return pairs

print(get_pairs([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 35))







#     for y in a[1:]

# x = a[0]
# y = a[1]
# for x in a[0:]:
#     for y in a[1:]:
#         summ =x + y
#         if summ == b:
#             print(x, y)