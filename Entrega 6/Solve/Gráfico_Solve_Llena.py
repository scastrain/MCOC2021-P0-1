import numpy as np
import matplotlib.pyplot as plt


def graficar(nombres):

    yticks=[0.0001,0.001,0.01,0.1,1,10,60,600]
    yticks_text=["0.1 ms","1ms","10ms","0.1 s","1 s","10 s", "1 min", "10 min"]
    
   
    xticks=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    xticks_text=["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
    xticks_text2=[]
 
    plt.figure()    
    ensamblajey = []
    soluciony = []
    for nombre in nombres:
        data = np.loadtxt(nombre)
        
        Nm = data[:, 0]
        ensamblaje = data[:, 1]
        solucion = data[:, 2]
        
       
        ensamblaje_max = max(ensamblaje)
        Nmmax = max(Nm)       
        solucion_max = max(solucion)

        ensamblajey= 0*Nm + ensamblaje_max
        soluciony=0*Nm + solucion_max
        
        plt.subplot(2,1,1)
        plt.title("Complejidad Solve Llena")
        plt.loglog(Nm, ensamblaje.T, "k-o", alpha=0.4,markersize=3)
        plt.ylabel("Tiempo de ensamblado")
        
        
        plt.subplot(2,1,2)
        plt.loglog(Nm, solucion.T, "k-o", alpha=0.4,markersize=3)
        plt.ylabel("Tiempo de solucion")
        plt.xlabel("Tamaño matriz ")
       
    plt.subplot(2,1,1)
    plt.plot(Nm,ensamblajey, "c--") 
    plt.loglog(Nm,Nm*(ensamblaje_max/Nmmax),"y--")
    plt.plot(Nm,Nm**2*(ensamblaje_max/Nmmax**2),"g--")
    plt.plot(Nm,Nm**3*(ensamblaje_max/Nmmax**3),"r--")
    plt.plot(Nm,Nm**4*(ensamblaje_max/Nmmax**4),"m--")
    plt.xticks(xticks,xticks_text2)
    plt.yticks(yticks, yticks_text)
    plt.ylim([0.000001, 600])
    plt.xlim([0, 20000])
    
    
    plt.subplot(2,1,2)
    plt.plot(Nm,soluciony, "c--",label="Constante") 
    plt.loglog(Nm,Nm*(solucion_max/Nmmax),"y--",label="O(N)")
    plt.plot(Nm,Nm**2*(solucion_max/Nmmax**2),"g--",label="O(N^2)")
    plt.plot(Nm,Nm**3*(solucion_max/Nmmax**3),"r--",label="O(N^3)")
    plt.plot(Nm,Nm**4*(solucion_max/Nmmax**4),"m--",label="O(N^4)")
    plt.xticks(xticks,xticks_text, rotation=45)
    plt.yticks(yticks, yticks_text)
    plt.ylim([0.000001, 600])
    plt.xlim([0, 20000])
        
        
    plt.tight_layout()
    plt.legend(loc=2,prop={'size': 8}) 
    plt.show()
    
    
nombres= ["Complejidad_SOLVE_llena0.txt","Complejidad_SOLVE_llena1.txt","Complejidad_SOLVE_llena2.txt","Complejidad_SOLVE_llena3.txt"]
graficar(nombres) 



