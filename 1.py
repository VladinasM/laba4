a = input('Введите количество вершин: ')
while not a.isdigit:
    print('Введите число:')
    a = input('Введите количество вершин: ')
while int(a) <= 0 or int(a) > 7:
    print('а<7')
    a = input('Введите количество вершин: ')

b = input('Введите количество ребер: ')
while not b.isdigit:
    print('Введите число:')
    b = input('Введите количество ребер: ')
while int(b) <= 0 or int(b) > 28:
    print('b<28')
    b = input('Введите количество ребер: ')

a = int(a)
b = int(b)

matrix = [[0] * b for i in range(a)]

rib = 0
while rib != b:
    node1 = int(input("Вершина 1: "))

    node2 = int(input("Вершина 2: "))

    if node1 == node2:
        matrix[node1][rib] = 2
    else:
        matrix[node1][rib] = 1
        matrix[node2][rib] = 1
    rib += 1
    print()


for i in range(a):
    print(matrix[i])

# Пункт А
print('a)')
tag_a = ""
for i in range(a):
    for j in range(b):
        if matrix[i][j] != 0:
            tag_a = tag_a + str(j) + ', '
    print(f' Для вершины {i} инцедентны ребра:', str(tag_a[:-2]))
    tag_a = ""

# Б
print('б)')
tag_b = 0
for i in range(a):
    for j in range(b):
        tag_b += matrix[i][j]
    print(f" Степень вершины {i}: ", tag_b)
    tag_b = 0

# В
print('в)')
tag_v = 0
zero = 0
for i in range(a):
    for j in range(b):
        tag_v += matrix[i][j]
    if tag_v == 0:
        zero += 1
        print(f"Вершина {i} имеет степень 0")
    tag_v = 0
if zero == 0:
    print('Вершины с 0 степенью отсутствуют')


# Пункт Г
print('г)')
tag_g = []
min = 0
for i in range(a):
    for j in range(b):
        if matrix[i][j] != 0:
            min += 1
    if min == 1:
        tag_g.append(i)

for i in range(len(tag_g)):
    print(" Инцидентно одному ребру: ", tag_g[i])
if len(tag_g) == 0:
    print("В графе нет вершин, инцедентных только одному ребру")

# Пункт Д
print('д)')
max_1 = 0
max_2 = 0
for i in range(a):
    for j in range(b):
        if matrix[i][j] != 0:
            max_1 += 1
    if max_2 <= max_1:
        max_2 = max_1
    max_1 = 0
print("Наибольшее число смежных рёбер: ", max_2)

# Пункт Е
print('е)')
tag_e = 0
for i in range(a):
    for j in range(b):
        if matrix[i][j] == 2:
            tag_e = True
            break

if tag_e != True:
    print("Петель нет")
if tag_e == True:
    print("Петли есть")
