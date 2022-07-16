import csv
import math

csvfile = open('data/ulabox.csv', newline='')
file = csv.DictReader(csvfile)
lineas = [linea for linea in file]
print("Longitud del archivo: " + str(len(lineas)) + " Lineas")
variables = list(map(str, list(lineas[0].keys())))
for i in range(3):
    variables[i] = "Discreta: " + variables[i]
for i in range(len(variables)-3):
    variables[i+3] = "Continua: " + variables[i+3]
print("\n\nVariables del archivo: \n    " + ("\n    ".join(variables)))

rango = {}

for linea in lineas:
    for v in linea:
        if(rango.get(v) == None):
            rango[v] = [float(linea[v])]
        else:
            rango[v].append(float(linea[v]))

print("\n\n{0:<25}{1:^25}{2:>25}".format("Variable","Maximos","Minimos"))
for var in rango:
    print("{0:<25}{1:^25}{2:>25}".format(str(var),str(max(rango[var])),str(min(rango[var]))))

print("\n\n{0:<25}{1:^25}{2:^25}{3:>25}".format("Variable","Media","Mediana","Moda"))
for var in rango:
    media = (sum(rango[var]) / 30000)

    ordenados = rango[var].copy()
    ordenados.sort()

    dicModa = {}
    for num in ordenados:
        if(dicModa.get(num)):
            dicModa[num] += 1
            continue
        dicModa[num] = 1

    print("{0:<25}{1:^25}{2:^25}{3:>25}".format(str(var), str(media), str(ordenados[15000]), str(max(dicModa))))


print("\n\n{0:<25}{1:>25}".format("Variable","Desviacion"))
for var in rango:
    media = (sum(rango[var]) / 30000)
    s = 0
    for i in rango[var]:
        s += (i - media) ** 2
    desv = math.sqrt(s / 30000)

    print("{0:<25}{1:>25}".format(str(var), str(desv)))

print("\n\n{0:<25}{1:^25}{2:^25}{3:^25}{4:^25}".format("Variable","1er Q","2do Q","3er Q","4to Q"))
for var in rango:
    temp = rango[var]
    temp.sort()
    n = 30000
    print("{0:<25}{1:^25}{2:^25}{3:^25}{4:^25}".format(var, temp[int(((n)+1)/4)-1], temp[int(((2*n)+2)/4)-1], temp[int(((3*n)+3)/4)-1], temp[int(((4*n)+4)/4)-2]))
