from time import perf_counter
import numpy as np
from scipy import linalg
from scipy.linalg import solve, inv

# se crea la funcion de Laplacian Matrix
from numpy import float32
def laplaciana(N, d= float32):
    A=-(np.eye(N,k=-1,dtype=d))+2*(np.eye(N,dtype=d))+-(np.eye(N, k=+1,dtype=d))
    return A

# Tamaño de matrices
Nm= [2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,300,350,500,600,800,900,1000,1500, 2000]

Numcorridas=10

nombres=["A_invB_inv.txt","A_invB_spSolve.txt","A_invB_spSolve_pos.txt","A_invB_spSolve_symmetric.txt","A_invB_spSolve_overwrite_a.txt","A_invB_spSolve_pos_overwrite_b.txt","A_invB_spSolve_pos_overwrite.txt"]
archivos=[open(nombre,"w") for nombre in nombres]

for N in Nm:
    dts=np.zeros((Numcorridas,len(archivos)))
    print (f"N={N}")
    

    #FORMA 1 
    for i in range (Numcorridas):
        # Se crea matriz laplaciana A y se crea un vector de unos:
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        
        # Se invierte la matriz A y se multiplica por el vector B:
        A_inv=linalg.inv(A)
        A_invB=A_inv@B
        t2=perf_counter()
        dt=t2-t1
        
        # agregar al archivo en primera columna
        dts[i][0]=dt
        
        
        
    #FORMA2: A_invB_spSolve(A,B)
    # Se crea matriz laplaciana A:
        A=laplaciana(N)
        # Se crea un vector de unos:
        B=np.ones(N)
        t1=perf_counter()

        A_invB=linalg.solve(A,B)
        t2=perf_counter()
        dt=t2-t1
        
        # agregar al archivo en segunda columna
        dts[i][1]=dt
        
        
    #FORMA 3: A_invB_spSolve_pos(A,B)
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.solve(A,B,assume_a="pos")
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en tercera columna:
        dts[i][2]=dt


    #FORMA 4: A_invB_spSolve_symmetric(A,B)
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.solve(A,B,assume_a="sym")
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en cuarta columna:
        dts[i][3]=dt
        
        
        
    #FORMA5: A_invB_spSolve_overwrite_a(A,B)
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.solve(A,B,overwrite_a=True)
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en quinta columna:
        dts[i][4]=dt
         
        
        
    #FORMA6: A_invB_spSolve_pos_overwrite_b(A,B)
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.solve(A,B,overwrite_b=True)
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en sexta columna:
        dts[i][5]=dt
    


    #FORMA7: A_invB_spSolve_pos_overwrite(A,B)
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.solve(A,B,overwrite_a=True,overwrite_b=True)
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en sexta columna:
        dts[i][6]=dt    

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



