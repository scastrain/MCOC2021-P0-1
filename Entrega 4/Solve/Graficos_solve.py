import matplotlib.pyplot as plt
import numpy as np



def graficar(Nombres):
    # Eje y de tiempo transcurrido:
    yticks=[0.0001,0.001,0.01,0.1,1,10,60,600]
    yticks_text=["0.1 ms","1ms","10ms","0.1 s","1 s","10 s", "1 min", "10 min"]
    
    # Eje x tamaño de matriz:
    xticks=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    xticks_text=["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
  
    plt.figure()
    
    for nombre in nombres:
        data=np.loadtxt(nombre)
        Nm=data[:,0]
        dts=data[:,1]
        
        print("Ns: ", Nm)
        print ("dts: ", dts)
        
        plt.loglog(Nm,dts.T,"-o", label=nombre)
        plt.ylabel("Tiempo transcurrido (s)")
        plt.xlabel("Tamaño de matriz")
        plt.grid(True)
        plt.title("Desempeño de Solve")
        
        plt.xticks(xticks,xticks_text, rotation=45)
        plt.yticks(yticks, yticks_text)
        
    plt.tight_layout()
    plt.legend(loc=2,prop={'size': 9})  
    plt.show()
      
    
nombres=["A_invB_inv.txt","A_invB_spSolve.txt","A_invB_spSolve_pos.txt","A_invB_spSolve_symmetric.txt","A_invB_spSolve_overwrite_a.txt","A_invB_spSolve_pos_overwrite_b.txt","A_invB_spSolve_pos_overwrite.txt"]

graficar(nombres)