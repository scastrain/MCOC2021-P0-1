import matplotlib.pylab as plt


Ns = []
dts = []
mems = []

titulo = "caso 3 half"

for i in range(10):	
	fid = open(f"rendimiento {titulo}{i}.txt", "r")	

	for line in fid:
		sl = line.split()
		N = int(sl[0])
		dt = float(sl[1])
		mem = int(sl[2])

		Ns.append(N)
		dts.append(dt)
		mems.append(mem)

	fid.close()


ejed_Tiempo = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 600]
eje_Tiempo = ["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

ejedx_Uso = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
ejex_Uso = ["10","20", "50", "100","200", "500", "1000", "2000", "5000", "10000", "20000"]

ejedy_Uso = [1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11]
ejey_Uso = ["1 KB","10 KB", "100 KB", "1 MB","10 MB", "100 MB", "1 GB", "10 GB", ""]


plt.figure()

#gráfico tiempo transcurrido

plt.subplot(2, 1, 1) #dos filas 1 columna
plt.title(f"Desempeño {titulo}")

M = 10
for i in range(M):
	plt.loglog(Ns[i*M:(i+1)*M], dts[i*M:(i+1)*M], marker="o")
plt.ylabel("Tiempo transcurrido (s)")
#plt.loglog(Ns, dts, marker="o")
plt.xticks(ejedx_Uso, [])
plt.yticks(ejed_Tiempo, eje_Tiempo)

plt.grid(b=True)

#gráfico uso de memoria

plt.subplot(2, 1, 2)

plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria (s)")
plt.loglog(Ns, mems, marker="o")
plt.xticks(ejedx_Uso, ejex_Uso, rotation=45)
plt.yticks(ejedy_Uso, ejey_Uso)
plt.axhline(y=8*10**9 , linestyle="--", color="k")

plt.grid(b=True)



plt.show()


