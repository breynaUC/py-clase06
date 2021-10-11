lista = []
n = int(input("N: "))
sum = 0
for x in range(0,n):
    z = int(input("z: "))
    lista.append(z)

for i in range(0,len(lista)):
    if lista[i]%2==0:
        sum=sum + lista[i]
print("La suma de pares es: ",sum)
#1,2,3,4,5,6,7,8,9,10