jornada = 48
vh = 35
he = 40 
salario = 0
h = int(input("Ingresar Horas Trabajadas: "))
hee = 0
if h>jornada:
    hee = h - jornada
    salario = vh * jornada + hee*he
else:
    salario = vh * h 

print("Horas Trabajadas: ", h)
print("Horas extras: ", hee)
print("Salario: ", salario)
#35*48=1680
#40*2=80
