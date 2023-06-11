N = int(input())
i = 1

while(i <= N):
    A = input("A: ")
    B = input("B: ")

    if(len(A) < len(B)):
        print("não encaixa")
    elif(A[len(A) - len(B):] == B):
        print("encaixa")
    else:
        print("não encaixa")
    i+=1
