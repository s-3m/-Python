src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniq_elem = set()
temp_elem = set()


for elem in src:
    if elem not in temp_elem:
        uniq_elem.add(elem)
    else:
        uniq_elem.discard(elem)
    temp_elem.add(elem)


res = [n for n in src if n in uniq_elem]
print(res)
