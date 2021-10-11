lista =[1,2,1,4,2,10,1,4,3,5,2]
b = int(input("N: "))
cont = 0
for x in range(0,len(lista)):
    if lista[x]==b:
        cont+=1
print("El número ",b," se repite",cont )