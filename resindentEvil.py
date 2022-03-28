linha=1
soma=1    
numeroFinal=1

#Procura até 1969
while(numeroFinal<=1969):
    linha+=1
    soma+=2
    numeroFinal+=soma
    print("Linha",linha,"Número Final: ",numeroFinal)

    
print(linha)    
#Observa-se também que o número final é o número da linha ao quadrado
