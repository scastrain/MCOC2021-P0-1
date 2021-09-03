import numpy as np
from scipy import linalg
from time import perf_counter
from numpy.linalg import solve
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import spsolve, inv


def laplaciana_llena(N,t=np.double):
    A=np.identity(N,t)*2
    for i in range(N):
        for j in range (N):
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return A
                    

def laplaciana_dispersa(N,t=np.double):
    A=lil_matrix((N,N))
    for i in range(N):
        for j in range (N):
            if i==j:
                A[i,j]=2
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return csc_matrix(A)


Nm= [2,5,10,16,32,60,130,260,550,1050,2100,3000,4000]

Numcorridas=4


for i in range(Numcorridas):
    nombres= [f"Complejidad_SOLVE_llena{i}.txt",f"Complejidad_SOLVE_dispersa{i}.txt",f"Complejidad_INV_llena{i}.txt",f"Complejidad_INV_dispersa{i}.txt"]
    archivos=[open(nombre,"w") for nombre in nombres]
   
    for N in Nm:
        ensamblaje = np.zeros((len(archivos)))
        solucion = np.zeros ((len(archivos)))
        
        print (f"N={N}")
        
             
   #CASO 1: SOLVE- Matriz llena

        t1=perf_counter()

        A= laplaciana_llena(N)
        b = np.ones(N,dtype=np.double)
        t2=perf_counter()
            
        C =solve(A,b)
        t3=perf_counter()

        dt1 = t2 - t1
        dt2 = t3- t2
        
        ensamblaje[0]= dt1
        solucion[0]= dt2
        
                
   #CASO 2: SOLVE-Matriz dispersa

        t1=perf_counter()

        A= laplaciana_dispersa(N)
        b = np.ones(N,dtype=np.double)
        t2=perf_counter()
            
        C=spsolve(A,b)
        # c=np.linalg.solve
        t3=perf_counter()

        dt1= t2 - t1
        dt2= t3 - t2
        
        ensamblaje[1]= dt1
        solucion[1]= dt2
        
        
   #CASO 3: INV- Matriz llena:
     
        t1=perf_counter()
        
        A= laplaciana_llena(N)
        t2=perf_counter()
        
        A_inv= linalg.inv(A)
        t3=perf_counter()

        dt1= t2 - t1
        dt2= t3 - t2
        
        ensamblaje[2]= dt1
        solucion[2]= dt2
             
         
   #CASO 4: INV- Matriz dispersa       
         
        t1=perf_counter()
        A= laplaciana_dispersa(N)
        t2=perf_counter()
        
        A_inv= inv(A)
        t3=perf_counter()

        dt1= t2 - t1
        dt2= t3 - t2
               
        ensamblaje[3]= dt1
        solucion[3]= dt2
    
    # Se agregan los resultados al archivo de texto:
        for j in range(len(archivos)):
            archivos[j].write(f"{N} {ensamblaje[j]} {solucion[j]}\n")
            archivos[j].flush()
        
[archivo.close()for archivo in archivos]