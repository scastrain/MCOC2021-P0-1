from time import perf_counter
import numpy as np
from scipy.linalg import solve, inv
from scipy import linalg
# se crea la funcion de Laplacian Matrix
from numpy import float32
def laplaciana(N, d= float32):
    A=-(np.eye(N,k=-1,dtype=d))+2*(np.eye(N,dtype=d))+-(np.eye(N, k=+1,dtype=d))
    return A

# Tamaño de matrices

Nm= [2,5,10,12,15,20,30,40,45,50,55,60,100,125,160,
200,250,350,500,600,1000,2000,3000, 4000, 4500]

Numcorridas=10

nombres=["A_invB_inv.txt","A_invB_npSolve.txt"]
archivos=[open(nombre,"w") for nombre in nombres]

for N in Nm:
    dts=np.zeros((Numcorridas,len(archivos)))
    print (f"N={N}")
       
    #Forma 1 
    for i in range (Numcorridas):
        # Se crea matriz laplaciana A:
        A=laplaciana(N)
        
        # Se crea un vector de unos:
        B=np.ones(N)
        # tiempo 1
        t1=perf_counter()
        
        # Se invierte la matriz A
        A_inv=linalg.inv(A)
        
        # Se multiplica por vector B
        A_invB=A_inv@B
        # tiempo 2
        t2=perf_counter()
        
        # diferencia de tiempo
        dt=t2-t1
        
        # agregar al archivo en primera columna
        dts[i][0]=dt
        
        
        
        
        # Forma 2: lo mismo pero usando linalg.solve(A,B)
        # Se crea matriz laplaciana A:
        A=laplaciana(N)
        
        # Se crea un vector de unos:
        B=np.ones(N)
        # tiempo 1
        t1=perf_counter()

        A_invB=linalg.solve(A,B,  sym_pos=False, lower=False, overwrite_a=True, overwrite_b=False, debug=None, check_finite=True, assume_a='gen', transposed=False)
        # tiempo 2
        t2=perf_counter()
        
        # diferencia de tiempo
        dt=t2-t1
        # agregar al archivo en segunda columna
        dts[i][1]=dt
        
    print ("dts: ", dts)
    
    # Se calcula el promedio de los tiempos:
    dts_mean=[]
    for j in range(len(archivos)):
        dts_mean.append(np.mean(dts[:,j]))
        
    print("dts_mean: ", dts_mean)
        
    
    # Se agregan los resultados al archivo de texto:
    for j in range(len(archivos)):
        archivos[j].write(f"{N} {dts_mean[j]}\n")
        archivos[j].flush()
        
[archivo.close()for archivo in archivos]



