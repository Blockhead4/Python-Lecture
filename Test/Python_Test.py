# Python Test

# 1. (2, 3, 5)

# 2. (1, 2, 4)

# 3.
a, b = map(int, input().split())
sum_odd = sum([i for i in range(a, b+1) if i % 2 == 1])
print(sum_odd)

# 4.
rate = int(input())

money = 1
future_money = 2*money
years = 0

while money <= future_money:
    money += money * (rate/100)
    years += 1

print(years)

# 5.
bts = ['RM', '진', '슈가', '제이홉', '지민', '뷔', '정국']

print(bts[5])
print(bts[0])
print(bts[5:])
print(bts[2:5])
print(bts[::2])

# 6.
vegetables = dict(가지=800, 오이=600, 수박=15000, 호박=1000, 깻잎=500)

from operator import itemgetter

sort_veg = sorted(vegetables.items(), key=itemgetter(1), reverse=True)
for veg, price in sort_veg:
    print('{}:{:>7,}'.format(veg, price))

# 7.
palin = 0
for i in range(101, 999):
    for k in range(100, i):
        check = str(k*i)
        if check == check[::-1]:
            if k*i > palin:
                palin = k*i
                x = k
                y = i

print(palin, x, y)

# 8.
import random

# row, col = map(int, input().split())
row = 8
col = 8

tiles = []
for _ in range(row):
    value = []
    for _ in range(col):
        value.append(random.randint(1, 4))
    tiles.append(value)

for i in tiles:
    for v in i:
        print(v, end=' ')
    print()

print()

seq_idx_h = []
for r in range(len(tiles)):
    for c in range(len(tiles[0])-2):
        if tiles[r][c] == tiles[r][c+1] == tiles[r][c+2]:
            seq_idx_h.append([r, c])

seq_idx_v = []
for r in range(len(tiles)-2):
    for c in range(len(tiles[0])):
        if tiles[r][c] == tiles[r+1][c] == tiles[r+2][c]:
            seq_idx_v.append([r, c])

for r, c in seq_idx_h:
    tiles[r][c] = '*'
    tiles[r][c+1] = '*'
    tiles[r][c+2] = '*'

for r, c in seq_idx_v:
    tiles[r][c] = '*'
    tiles[r+1][c] = '*'
    tiles[r+2][c] = '*'

for i in tiles:
    for v in i:
        print(v, end=' ')
    print()
    
# 9.
a = [1,3,5,7,9]

b = list(map(lambda x: x**2, a))
print(b)

# 10. 과제 점수(10점)