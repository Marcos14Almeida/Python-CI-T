import numpy as np

X = [24,30,36]
Y = [[13],[14],[16]]

#Equacoes Normais
Uns=np.ones(3)
Uns=np.transpose(Uns)
XT=np.transpose(X)
Matriz=np.c_[Uns,XT]

MatrizT=np.transpose(Matriz)
Result = np.matmul(MatrizT,Matriz)
Result = np.matmul(   np.linalg.inv(Result) ,  MatrizT)
Beta = np.matmul(Result,Y)
Result = np.matmul(   Matriz,  Beta     )
Erro = Result - Y
ErroT = np.transpose(Erro)

Final = np.matmul(   ErroT,      Erro )
print(Final) 


#Método dos Mínimos quadrados
np.savetxt('data1_x.npy', [X, Y])
np.savetxt('data1_y.npy', [X, Y])


np.savetxt('data2_x.npy', [X, Y])
np.savetxt('data2_y.npy', [X, Y])