from time import perf_counter
import numpy as np
from scipy import linalg
from scipy.linalg import eigh, inv
from numpy import float32, float64

# se crea la funcion de Laplacian Matrix

def laplaciana(N, d= float32):
    A=-(np.eye(N,k=-1,dtype=d))+2*(np.eye(N,dtype=d))+-(np.eye(N, k=+1,dtype=d))
    return A

# Tamaño de matrices
Nm= [2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,190,200,250,300,350, 400, 500,550,590,600,800]

Numcorridas=10

nombres=["A_eigh_caso_1.txt","A_eigh_caso_2_F.txt","A_eigh_caso_3_T.txt","A_eigh_caso_4_F.txt","A_eigh_caso_5_T.txt","A_eigh_caso_6_F.txt","A_eigh_caso_7_T.txt","A_eigh_caso_8_F.txt","A_eigh_caso_9_T.txt"]
archivos=[open(nombre,"w") for nombre in nombres]

for N in Nm:
    dts=np.zeros((Numcorridas,len(archivos)))
    print (f"N={N}")
    

    #Caso 1
    for i in range (Numcorridas):
     # Se crea matriz laplaciana A:
        A=laplaciana(N)
        t1=perf_counter()

        A_invB=linalg.eigh(A)
        t2=perf_counter()
        dt=t2-t1
        
        # agregar al archivo en segunda columna
        dts[i][0]=dt
           
        
    #Caso 2
    # Se crea matriz laplaciana A:
        A=laplaciana(N)
        t1=perf_counter()

        A_invB=linalg.eigh(A, overwrite_a=False, driver="ev")
        t2=perf_counter()
        dt=t2-t1
        
        # agregar al archivo en segunda columna
        dts[i][1]=dt
        
        
    #Caso 3
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.eigh(A, overwrite_a=True, driver="ev")
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en tercera columna:
        dts[i][2]=dt


    #Caso 4
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.eigh(A, overwrite_a=False, driver="evd")
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en cuarta columna:
        dts[i][3]=dt
        
        
        
    #Caso 5
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.eigh(A, overwrite_a=True, driver="evd")
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en quinta columna:
        dts[i][4]=dt 

    #Caso 6
    # Se crea matriz laplaciana A:
        A=laplaciana(N)
        t1=perf_counter()

        A_invB=linalg.eigh(A, overwrite_a=False, driver="evr")
        t2=perf_counter()
        dt=t2-t1
        
        # agregar al archivo en segunda columna
        dts[i][5]=dt
        
        
    #Caso 7
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.eigh(A, overwrite_a=True, driver="evr")
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en tercera columna:
        dts[i][6]=dt


    #Caso 8
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.eigh(A, overwrite_a=False, driver="evx")
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en cuarta columna:
        dts[i][7]=dt
        
        
        
    #Caso 9
    # Se crea matriz y vector
        A=laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB2=linalg.eigh(A, overwrite_a=True, driver="evx")
        t2=perf_counter()      
        dt=t2-t1
            
        # agregar al archivo en quinta columna:
        dts[i][8]=dt

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



