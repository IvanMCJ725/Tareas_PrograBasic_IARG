numero = int(input("Ingrese un numero entero: "))
if numero >= 0:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")
else:
    print("El número debe ser entero positivo o cero")