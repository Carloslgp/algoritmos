a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))
c = float(input("Digite o valor de 'c': "))

resposta = b**2 -4*a*c

if resposta > 0:
    print("Existem duas raízes distintas")
elif resposta == 0:
    print("Existem duas raízes reais iguais")
elif resposta < 0:
    print("Existem duas raízes imaginárias conjugadas")
