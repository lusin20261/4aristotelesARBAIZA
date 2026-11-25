print("================================")
print("   MI CALCULADORA   ")
print("================================")

while True:
    print("")
    print("¿Qué operación deseas realizar?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    print("=============================")

    opcion = input("elige una opción: ")

    if opcion == "1":
        num1 = input("Ingresa el primer número: ")
        num1 = int(num1)
        num2 = input("Ingresa el segundo número: ")
        num2 = int(num2)
        print("El resultado de la suma es:",num1 + num2)
        


