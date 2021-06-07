import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    with open('log.txt', 'a', encoding='utf-8') as d:
        str = f.readlines()
        a = []
        for i in str:
            try:
                pars = re.compile(r'((?:\d+\.){3}\d+)\D+(\d+\/\w+\S(?:\d+\:){3}\d+\s\S\d+)\S\s\S(\w+)\s((?:\S\w+){2})\s\S+\s(\d+)\s(\d)')
                b = (pars.search(i).group(1), pars.search(i).group(2), pars.search(i).group(3),
                    pars.search(i).group(4), pars.search(i).group(5), pars.search(i).group(6))
                a.append(b)
            except AttributeError:
                print(f'{i}', file=d)

for i in a:
    print(i)