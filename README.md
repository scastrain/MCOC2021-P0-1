# MCOC2021-P0-1

# Mi computador principal

* Marca/modelo: Acer A315-41
* Tipo: Notebook
* Año adquisición: 2019
* Procesador:
  * Marca/Modelo: AMD Ryzen 5 3500U
  * Velocidad Base: 2.1 GHz
  * Velocidad Máxima: 3.7 GHz
  * Numero de núcleos: 4 
  * Humero de hilos: 8
  * Arquitectura: AMD "Zen"
  * Set de instrucciones: XFR, FMA3, SSE 4.2, AVX2, SMT
* Tamaño de las cachés del procesador
  * L1: 128KB
  * L2: 512KB
  * L3: 4MB
* Memoria 
  * Total: 4 GB
  * Tipo memoria: DDR4
  * Velocidad 2400 MHz
  * Numero de (SO)DIMM: 4
* Tarjeta Gráfica
  * Marca / Modelo: AMD Radeon Vega 8
  * Memoria dedicada: No tiene
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: Kingston
  * Tipo: SSD
  * Tamaño: 480 GB
  * Particiones: 2
  * Sistema de archivos: SATA, Rev

  
* Dirección MAC de la tarjeta wifi: 3C-91-80-93-76-7D
* Dirección IP (Interna, del router): 192.168.0.21
* Dirección IP (Externa, del ISP): 192.168.0.1
* Proveedor internet: VTR Banda Ancha S.A.

# Desempeño MATMUL
* ![image](https://user-images.githubusercontent.com/88336928/128522536-330b3860-e223-4055-9f2f-75fad39c89d4.png)

* ¿Cómo difiere del gráfico del profesor/ayudante?
Se puede ver que difiere el tiempo de corrida, a diferencia del profesor la diferencia de tiempo (dts) para ciertos valores varian en ciertos puntos, como por ejemplo, al comienzo. Sobre el uso de la memoria ambos graficos son similares.

* ¿A qué se pueden deber las diferencias en cada corrida?
Se deben a la diferencia en el tipo de procesador, ya que este tiene un intervalo de ejecucion de tiempo distinto.

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
Esto ocurre ya qe cada vez que se ejecuta el código se realiza todo nuevamente, por lo que en cada iteración va a variar por algunos segundo. Esto puede depender de otros programas que esten abiertos al mismo tiempo. En cambio el gráfico de memoria es linea, ya que miestras mas grande la matriz más bytes se utilizaran.  

* ¿Qué versión de python está usando?
versión 3.8

* ¿Qué versión de numpy está usando?
versión 1.20.1

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar.
![image](https://user-images.githubusercontent.com/88336928/128525360-e352486f-f0e7-4fe7-abbf-c5ee546bd0b3.png)
Se utilizan los 4 procesadores y 8 hilos.

# Desempeño de INVERSA
* Para cada tipo de dato se puede ver en los gráficos:
![Caso 1 double](https://user-images.githubusercontent.com/88336928/129896762-00aa975c-b884-4b8d-8cef-407cf3af7801.png)
![Caso 1 single](https://user-images.githubusercontent.com/88336928/129896813-b6cbae76-187a-4b11-99d0-710676f398e1.png)
![Caso 2 double](https://user-images.githubusercontent.com/88336928/129896839-9dcdf194-5f48-4e94-9843-53ce633d7a29.png)
![Caso 2 half](https://user-images.githubusercontent.com/88336928/129896861-2ba295c5-889e-4604-8d5d-c7313f8b86a2.png)
![Caso 2 longdouble](https://user-images.githubusercontent.com/88336928/129896886-86e01d75-bc05-46b6-b010-38c40146fb4f.png)
![Caso 2 single](https://user-images.githubusercontent.com/88336928/129896906-8c5ea3d3-1eff-4cb4-b176-f5e70db521af.png)
![Caso 3 double](https://user-images.githubusercontent.com/88336928/129896934-c2c50294-7b5c-45d0-a3bc-ae5eabcc1fce.png)
![Figure_1](https://user-images.githubusercontent.com/88336928/129896957-26168bd6-b2e4-459b-ae71-dc24c89108f9.png)
![Caso 3 Longdouble](https://user-images.githubusercontent.com/88336928/129896977-421f9a1b-9b8b-4d0c-95b5-6b5292313bbc.png)
![Caso 3 single](https://user-images.githubusercontent.com/88336928/129896995-a42fdac8-f09a-4280-be6e-cdd2a509cdee.png)

Para el caso 1 half y longdouble, no se logra ejecutar.
Además se puede ver que se utiliza más memoria a medida que el tamaño de la matriz aumenta.

* ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?
Se utiliza el algoritmo de Laplacian Matrix, este es un algoritmo con complejidad factorial, lo cual hace que resolver el sistema mediante este método no sea la mejor opción, debido a su demora. Matriz donde las columnas representan a las aristas del grafo y las filas a los vértices. El elemento (i,j) representa que la arista i incide en el vértice j. La diagonal esta compuesta por 2, y las diagonales adyacentes superior e inferior a la central estan compuestas por -1. Además se utiliza la Invertible Matrix, para el caso 1 se utiliza la libreria de Numpy y en el caso 2 y 3 se utiliza la libreria Scipy. En ambos casos se resuelve un sistema lineal de ecuaciones.

* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 
El paralelismo es una función que realiza el procesador para ejecutar varias tareas al mismo tiempo, realizando varios cálculos simultáneamente (paralelismo de datos). Los sistemas informáticos suelen hacer uso de cachés, ubicados cerca del procesador que almacenan las copias temporales de los valores de la memoria. Como se mencionó anteriormente el caso que presentó menos desempeño utilizando otras aplicaciones o programas mientras se corria el código fue el caso 1.


# Desempeño de Solve y Eigh
* Haga un comentario completo respecto de todo lo que ve en términos de desempeño en cada problema. 
-	Desempeño timing solve: para este caso se logo generar una matriz máxima de 2000x2000, no se ogra llegar a una de 10000x10000 ya que el rendimiento de mi computador no permite que esto ocurra en menos de 2 minutos. 
-	Desempeño timing eigh float y double: para este caso se logo generar una matriz máxima de 800x800, no se ogra llegar a una de 10000x10000. Se puede ver que este es más rápido que el desempeño de eigh double.

* ¿Como es la variabilidad del tiempo de ejecución para cada algoritmo? 
-	Tiene un incremento exponencial a medida que aumentan las matrices. 
* ¿Qué algoritmo gana (en promedio) en cada caso? 
-	Desempeño timing solve: A_invB_soSolve_pos, la cual es la matriz definida positiva.
-	Desempeño timing eigh float: A_eigh_caso_5_T la cual tiene overwrite_a=True y driver="evd"
-	Desempeño timing eigh double: : A_eigh_caso_7_T la cual tiene overwrite_a=True y driver="evr

* ¿Depende del tamaño de la matriz? 
-	Si depende del tamaño de la matriz, ya que a mayor matriz el desempeño será “peor”.
* ¿A que se puede deber la superioridad de cada opción? 
-	Se debe a la cantidad de acciones que se le pide a cada opción, las cuales difieren del set up por default.  
¿Su computador usa más de un proceso por cada corrida? 
-	Si, utiliza los cuatro procesadores.
-	![image](https://user-images.githubusercontent.com/88336928/130275105-ead7e442-9320-4eda-9b71-bb3f1458d69a.png)
 
* ¿Que hay del uso de memoria (como crece)? 
- A medida que los programas corren, el uso de memoria se mantiene constante.
![image](https://user-images.githubusercontent.com/88336928/130275128-7e86d41a-9eeb-4f3a-b8ed-b91403b9c865.png)

# Matrices dispersas y complejidad computacional
* Se realizaron 10 corridas con matrices crecientes hasta un N=4500, se observo que a medida que disminuinan las corridas, el tamaño de matriz podia ser mayor (para 280 s de corrida), pero se decidio mantener la cantidad de corridas que fueron indicadas en las entregas anteriores.
* Caso 1: Complejidad algorítmica de MATMUL
Se genero el gráfico para la multiplicación de matrices Laplacianas utilizando el formato matriz llena con datos tipo double:
![Llena](https://user-images.githubusercontent.com/88336928/130873116-feed7b4a-5d6a-4569-9fc9-5bc1bab0dfd5.png)
Luego se repitio el mismo procedimiento para matrices dispersas:
![Dispersa](https://user-images.githubusercontent.com/88336928/130873857-14301980-19a1-4ec9-b3ec-750f3ebc48dd.png)
Se puede observar que el tiempo de ensamblado es similar, pero se pueden notar diferencias en el tiempo de solucion. Para mayor tamaño de matriz la llena demora más de un segundo, en cambio la dispersa demora menos de 0.1 s.
* Código de ensamblaje:
- Matriz llena:
```
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import spsolve, inv
import numpy as np

 def laplaciana_llena(N,t=np.double):
    A=np.identity(N,t)*2
    for i in range(N):
        for j in range (N):
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return A 
``` 
- Matriz dispersa:
```
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
 ```

# Matrices dispersas y complejidad computacional

![Inv_Dispersa](https://user-images.githubusercontent.com/88336928/132034277-df108a87-119d-4d94-8c8c-c5cc3aa63aad.png)
![Inv_Llena](https://user-images.githubusercontent.com/88336928/132034283-944d76e6-e636-4e78-9f59-242c86492777.png)
![Solve_Dispersa](https://user-images.githubusercontent.com/88336928/132034297-59e05f8d-cfbf-42ec-b979-ead8cc021f14.png)
![Solve_Llena](https://user-images.githubusercontent.com/88336928/132034300-c1c0f10f-f417-4ba3-bb93-1f1936a5fa69.png)

* Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.
  Caso Solve: se puede ver como el tiempo de ensamblado es similar para ambos casos, en cambio el tiempo se solución tiene mayores variaciones. Además, para el caso de matriz llena, se ven discontinuidades a lo largo de las corridas.

  Caso Inv: se puede ver como el tiempo de ensamblado varia, la matriz dispersa se demora más que la llena. El tiempo se solución tiene también tiene variaciones, donde se puede    ver un salto en el caso de matriz llena.

* ¿Cual parece la complejidad asintótica (para N→∞N→∞)  para el ensamblado y solución en ambos casos y porqué?
  Caso Solv: Para el tiempo de ensamblado se puede ver un comportamiento de complejidad asintótica correspondiente a O(N2), para ambos casos. Para el tiempo de solución se puede ver un comportamiento de complejidad asintótica correspondiente a O(N) para la matriz dispersa y O(N2) para la matriz llena.

 Caso Inv: Para el tiempo de ensamblado se puede ver un comportamiento de complejidad asintótica correspondiente a O(N2), para ambos casos. Para el tiempo de solución se puede ver un comportamiento de complejidad asintótica correspondiente a O(N) para la matriz dispersa y O(N2) para la matriz llena.

* ¿Como afecta el tamaño de las matrices al comportamiento aparente?
 Cuando se tiene un N menor el tiempo de ensamblado y de solución es mayor, esto se debe al paralelismo, ya que el computador esta haciendo muchas acciones en un inicio. Además, el tiempo se solución se muestra variable a excepción de la matriz inversa dispersa. 
 
* ¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?
 El tiempo de ensamblado tiene corridas más estables, en cambio el tiempo de solución se muestra muy variable, por lo tanto, es más inestable para ambos casos.
 
 * Código de ensamblaje:
- Matriz llena:
```
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import spsolve, inv
import numpy as np

 def laplaciana_llena(N,t=np.double):
    A=np.identity(N,t)*2
    for i in range(N):
        for j in range (N):
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return A 
``` 
- Matriz dispersa:
```
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
 ```
 El codigo de matrices llenas es mucho más comodo que el de dispersas. El segundo caso se demoro menos, pero no fue el más optimo al momento de ensamblar la matriz.
