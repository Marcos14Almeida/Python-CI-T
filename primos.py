maximo=120
primos=[]

for numeroTeste in range(2,maximo):
    flagPrimo=True
    
    #Faz uma busca em que Divide o numeroTeste por N
    for n in range(2,maximo):
        
          #verifica se o número é primo  
          if ((numeroTeste % n) == 0) and numeroTeste//n!=1:
                   #print(numeroTeste,"Não é primo")
                   flagPrimo=False
                   break
            
    #Se ao final da busca não for primo salva o valor        
    if(flagPrimo==True):
          primos.append(numeroTeste)
          
#Lista de Números Primos          
print(primos)          
 
