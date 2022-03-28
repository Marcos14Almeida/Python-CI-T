import numpy as np
contador=0
flagTeste = [[1,1,1,1,1,1,1,1,1]]
for moedas in range(0,25):
    for segundos in range(255):
        for DragonCoins in range (0,10):
         flag = [0,0,0,0,0,0,0,0,0]
         
#Area 2            
         if(moedas>=21):
              flag.insert(1,1)
         if(moedas<8):
              flag.insert(2,1)
         if(moedas>=8 and moedas<21) : 
              flag.insert(3,1)

#Area 3
         if(segundos>=250):
              flag.insert(4,1)
         if(segundos<235):
              flag.insert(5,1)
         if(segundos>=235 and segundos<250) :
              flag.insert(6,1)
#Area 4
            
         if(segundos<250):
          if(DragonCoins<=3):
              flag.insert(7,1)
          else:
              flag.insert(8,1)
         
#%%              
#Verifica no vetor flagTeste se tem alguma possibilidade que já foi realizada
#Caso a flagTemValorIgual for False então a possibilidade é nova e o contador aumenta              
         flagTemValorIgual=False     
         for i in range (0,len(flagTeste)):     
          if(np.array_equal(flagTeste[i],flag)==True):
            flagTemValorIgual=True;
         if(flagTemValorIgual==False):   
            flagTeste.append(flag)
            contador+=1
print(contador)

#%% 
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

        