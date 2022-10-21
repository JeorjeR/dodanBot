import os
from itertools import combinations

with open('E:\\files\\phrases\\nekit.txt', 'r', encoding='utf-8') as file:
    a = tuple(''.join(element) for element in combinations([*file], 3))
    b = tuple(''.join(element) for element in combinations([*file], 5))
    c = tuple(''.join(element) for element in combinations([*file], 8))
    d = tuple(''.join(element) for element in combinations([*file], 10))
    fl = open('E:\\files\\phrases\\nekit_2.txt', 'w', encoding='utf-8')
    for str_ in a:
        fl.write(str_)
    for str_ in b:
        fl.write(str_)
    for str_ in c:
        fl.write(str_)
    for str_ in d:
        fl.write(str_)
