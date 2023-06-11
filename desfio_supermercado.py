T = int(input())

for i in range(T):
    i+=1
    N,K = int(input()), int(input()) 

    if(N>K):
        retorno = int(N/K) + int(N%K)
        print(retorno)
    else:
        print(N)

