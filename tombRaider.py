senha = ["A","A","A",0,0,0,0]
chars=["A","B","C","D","E","F"]
contador=0;

#Forma as letras da senha
for letra0 in chars:
    senha[0]=letra0
    for letra1 in chars: 
      senha[1]=letra1
      for letra2 in chars:
        senha[2]=letra2
        
        #forma os números da senha
        for senha[3] in range(1,10):
             for senha[4] in range(1,10):
              for senha[5] in range(1,10):
               for senha[6] in range(1,10):

                  #CONDIÇÕES
                   
                  #3 primeiros digitos diferentes
                  if(senha[0]!=senha[1] and senha[1]!=senha[2] and senha[0]!=senha[2]):
                      #DIGITOS A e D
                     if(senha[0]=='A' or senha[1]=='A' or senha[2]=='A'):
                       if(senha[0]=='D' or senha[1]=='D' or senha[2]=='D'):
                         #1ºdigito 3 ou 6 
                         if(senha[3] ==3 or senha[3]==6):
                                 #Soma 8    
                                 if(senha[3]+senha[4]+senha[5]+senha[6]==8):
                                      contador+=2
#Verifica o tempo possível
if(contador<5*60):
    tempo = "SIM"
else:
    tempo = "Não";
print("É possível:",tempo,", Tempo necessário:", contador,"s")      

