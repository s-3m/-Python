src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = [val for i, val in enumerate(src[1:]) if val > src[1:][i-1]]

print(res)