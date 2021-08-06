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







