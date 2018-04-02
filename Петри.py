#coding: utf8

t = {}
t['t1'] = [['p1'],       ['p3', 'p5']]
t['t2'] = [['p4'],       ['p3', 'p5']]
t['t3'] = [['p1', 'p2'], ['p5']]
t['t4'] = [['p5'],       ['p4', 'p4', 'p7']]
t['t5'] = [['p7'],       ['p5', 'p6']]
t['t6'] = [['p2'],       ['p6']]

maks = []
ind = -1
maks.append([1, 0, 1, 0, 1, 0, 1])
run = True
while run:
    if ind + 1 >= len(maks):
        print('Больше нет возможных ходов')
        break
    ind += 1
    line = maks[ind][:]
    for key in t:
        line = maks[ind][:]
        inp = t[key][0]
        out = t[key][1]
        
        b = True
        for x in set(inp):
            if line[int(x[1:]) - 1] >= inp.count(x):
                pass
            else:
                b = False
        if not b:
            continue
        print('For', line, ':', end=' ')
        for x in set(inp):
            line[int(x[1:]) - 1] -= inp.count(x)        
        for x in set(out):
            line[int(x[1:]) - 1] += out.count(x)
        if line in maks:
            print('*', line, ' ', key, sep='')
        else:
            maks.append(line)
            print(line, ' ', key, sep='')
        qu = input()
        if qu == 'exit':
            run = False
            break