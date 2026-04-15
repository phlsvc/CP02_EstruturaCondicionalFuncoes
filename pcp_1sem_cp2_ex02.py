A=float(input("Digite o valor do lado A: "))
B=float(input("Digite o valor do lado B: "))
C=float(input("Digite o valor do lado C: "))
def triangulo(A,B,C):
    if A>= B+C or B>= A+C or C>= A+B:
        print("Os lados não formam um triângulo")
        return
    if A**2 == B**2 + C**2 or B**2 == A**2 + C**2 or C**2 == A**2 + B**2:
        print("O triângulo é retângulo")
    elif A**2 > B**2 + C**2 or B**2 > A**2 + C**2 or C**2 > A**2 + B**2:
        print("O triângulo é obtusângulo")
    else:
        print("O triângulo é acutângulo")
    if A == B == C:
        print("O triângulo é equilátero")
    elif A == B or A == C or B == C:
        print("O triângulo é isósceles")
    else:        print("O triângulo é escaleno")
triangulo(A,B,C)