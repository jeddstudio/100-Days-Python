lst = [11,8,11]

for n, i in enumerate(lst):
    if i == 11:
        if sum(lst) >= 21:
            lst[n] = 1
print(lst)


'''
if sum(lst) > 21:
    for n, i in enumerate(lst):
        if i == 11:
            lst[n] = 1
print(lst)
'''