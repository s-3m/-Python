from sys import argv

with open('sales.csv', 'a', encoding='utf-8') as sales_write:
    with open('sales.csv', 'r', encoding='utf-8') as sales_read:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace('.', '').isdigit()]:
            if len(argv) == 3:
                print(*sales_read.read().split()[int(argv[1]) - 1:int(argv[2])], sep='\n')
            if '.' in argv[1] or ',' in argv[1]:
                print(argv[1], file=sales_write)
            else:
                print(*sales_read.readlines()[int(argv[1])-1:])
        else:
            print(sales_read.read())