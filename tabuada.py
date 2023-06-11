
step = int(input("Informe o número da tabuada desejada: "))
limite = (step * 10) + 1

for numero in range (0, limite, step):
    print(numero)
