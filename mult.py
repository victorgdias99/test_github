def mult(x, y, z):
    return x*y*z

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = mult(a, b, c)
print("A multiplicação entre {}, {} e {} é {}".format(a, b, c, d))
