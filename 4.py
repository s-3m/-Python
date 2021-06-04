import os
import math
from collections import defaultdict
import django


def if_el(size_file):
    if size_file <= 10:
        my_dict[10] += 1
    elif 10 < size_file <= 100:
        my_dict[100] += 1
    elif 100 < size_file <= 1000:
        my_dict[1000] += 1
    elif 1000 < size_file <= 10000:
        my_dict[10000] += 1
    elif 10000 < size_file <= 100000:
        my_dict[100000] += 1
    else:
        my_dict['very_big'] += 1


searh_folder = django.__path__[0]
my_dict = defaultdict(int)
for root, dirs, files in os.walk(searh_folder):
    for file in files:
        if_el(math.ceil(os.stat(os.path.join(root, file)).st_size))

print(dict(sorted(my_dict.items(), key=lambda x: str(x[0]))))


#------------------------------------второй вариант

print('\n' * 3)

searh_folder = django.__path__[0]
my_dict = defaultdict(int)
for root, dirs, files in os.walk(searh_folder):
    for file in files:
        size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        my_dict[size] += 1

print(dict(sorted(my_dict.items(), key=lambda x: str(x[0]))))
