numero_inicial = int(input("Ingresa un numero entero de inicio: "))
numero_final = int(input("Ingresa un numero entero de finalizacion mayor que el anterior: "))
contador = numero_inicial
lista_de_numeros = []
while contador<=numero_final:
    if contador % 2 !=0:
        lista_de_numeros.append(contador)
    contador = contador + 1
print(lista_de_numeros)