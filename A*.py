import numpy as np
import operator
from operator import itemgetter

L = 10
W = 10
B = 6 #unde sa fie bariera

Env = np.zeros((L,W))
Mat = np.zeros((L,W))


x_S = 1
y_S = 8
x_T = 9
y_T = 9

def conditie(open_list_l):
	for item in open_list_l:
		coord, _ = item
		x, y = coord
		
		if x == x_T and y == y_T:
			return 0
	return 1

def neighberhood(coord):
	returns = []
	quant = [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0)]
	for item in quant:
		x, y = tuple(map(operator.add, coord, item))
		if x < 0 or x > L-1 or y < 0 or y > W-1 or Env[x][y] == -1:
			continue
		else:
			returns.append(((x, y), Env[x][y]))
			Env[x][y] = -1
	return returns



for i in range(L):
	for j in range(W):
		Env[i][j] = abs(x_T-i) + abs(y_T-j) + abs(x_S-i) + abs(y_S-j)
for i in range(2,W):
	Env[4][i] = -1

open_list = []
open_list.append( ((x_S, y_S), Env[x_S][y_S]) )
Env[x_S][y_S] = -1


print(Env)

i = 0
while conditie(open_list) == 1:
	coord, val = open_list[0]	

	nbrs = neighberhood(coord)
	open_list = open_list + nbrs
	x, y = coord
	Mat[x][y] = 1
	del open_list[0]
	open_list.sort(key = itemgetter(1))
	i = i+1





print(Env)
print(Mat)