from numpy import zeros, float16, float32, float64
from time import perf_counter
import matplotlib.pylab as plt
import random

#Tamaño
N = 1000

Ns = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 16, 20, 24, 29, 35, 42, 51, 62, 75, 100, 190, 200, 240, 330, 360, 400, 490, 500, 596, 719, 868, 1048, 1264, 1526, 1842, 2222, 2682, 3237, 3906]
"""for i in range(27):
	j = random.randrange(5, 2000)
	Ns.append(j)


Ns.sort()
Ns[0] = random.randint(1, 10)"""


dts = []
mems =[]

for i in range(10):
	fid = open(f"rendimiento{i}.txt", "w")

	for N in Ns:
		

		A = zeros((N, N), dtype=float16 )+1

		B = zeros((N, N))+2


		t1 = perf_counter()
		C = A@B
		t2 = perf_counter()

		uso_memoria_total = A.nbytes + B.nbytes + C.nbytes

		dt = t2 - t1

		dts.append(dt)
		mems.append(uso_memoria_total)

		print(f"N = {N} dt = {dt} s mem = {uso_memoria_total} bytes flops = {N**3/dt} flops/s")
		
		fid.write(f"{N} {dt} {uso_memoria_total}\n")

	fid.close()

