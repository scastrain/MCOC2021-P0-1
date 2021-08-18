from numpy import zeros, float16, float32, float64
from time import perf_counter
import matplotlib.pylab as plt
import random
from scipy import linalg
import numpy as np

def laplaciana_half(N, dtype=np.half):
	A = zeros((N, N), dtype=dtype)

	for i in range(N):
		A[i,i] = 2
		for j in range(max(0,i-2),i):
			if abs(i-j) == 1:
				A[i,j] = -1
				A[j,i] = -1

	return A

#Tamaño

titulo = "caso 3 half"
a = float16

Ns = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 16, 20, 24, 29, 35, 42, 51, 
62, 75, 100, 190, 200, 240, 330, 360, 400, 490, 500, 540, 596, 719, 868, 900, 1048, 
1264, 1526, 1842, 2222, 2500]

dts = []
mems =[]

for i in range(10):
	fid = open(f"rendimiento {titulo}{i}.txt", "w")

	for N in Ns:
		
		
		A = laplaciana_half(N, dtype=a)
		t1 = perf_counter()
		
		Am1 = linalg.inv(A, overwrite_a=True)

		t2 = perf_counter()
		
		dt = t2 - t1
		#print(f"{dt}")
		#exit(0)

		bytes_total = A.nbytes + Am1.nbytes

		dts.append(dt)
		mems.append(bytes_total)

		print(f"N = {N} dt = {dt} s mem = {bytes_total} bytes flops = {N**3/dt} flops/s")
		
		fid.write(f"{N} {dt} {bytes_total}\n")

	fid.close()

