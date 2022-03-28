Yoshi = 450 
Chocolate = 330 
Cookie = 340

gosta3ilhas =0;
gosta2ilhas =0;
#Qnts Gostam de 3 ilhas
for i in range(0,30):
 Yoshi-=1
 Chocolate-=1
 Cookie-=1
 gosta3ilhas+=1
#Qnts Gostam de 2 ilhas 
for i in range(gosta3ilhas,200):
 Yoshi-=1
 Chocolate-=1
 gosta2ilhas+=1
for i in range(gosta3ilhas,180):
 Yoshi-=1
 Cookie-=1
 gosta2ilhas+=1
for i in range(gosta3ilhas,100):
 Chocolate-=1
 Cookie-=1
 gosta2ilhas+=1

gostaNenhumaIlha = 1000-gosta3ilhas-gosta2ilhas-Yoshi-Cookie-Chocolate
print("Quantos não gostam de nenhuma destas localidades:",gostaNenhumaIlha, "Quantos gostam de somente 1 destas localidades:",Yoshi+Chocolate+Cookie)

