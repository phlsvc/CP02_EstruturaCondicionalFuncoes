def menorcp(n1,n2,n3):
    if n1<n2 and n2<=n3:
        return  n1
    elif n1>=n2 and n2>n3:
        return n3
    elif n1<=n3 and n3<n2:
        return n2
    else:
        return n1

cp1=float(input("Insira a nota do Checkpoint 1: "))
cp2=float(input("Insira a nota do Checkpoint 2: "))
cp3=float(input("Insira a nota do Checkpoint 3: "))
sp1=float(input("Insira a nota do Sprint 1: "))
sp2=float(input("Insira a nota do Sprint 2: "))
gs=float(input("Insira a nota da Global Solution:"))
if cp1<=10 and cp2<=10 and cp3<=10 and sp1<=10 and sp2<=10 and gs<=10 and cp1>=0 and cp2>=0 and cp3>=0 and sp1>=0 and sp2>=0 and gs >=0:
    menor = menorcp(cp1,cp2,cp3)
    print(menor)
    media=(((cp1+cp2+sp1+sp2-menor)/4)*0.4)+(gs*0.6)
    mediaPeso=media*0.4
    print(f"Media do semestre(sem peso): {media:.1f}")
    print(f"Media do semestre com peso: {mediaPeso:.1f}")
else:
    print("Valores invalidos")