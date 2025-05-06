from colorama import Fore, Style
#Imprimimos menú de opciones.
print(Fore.YELLOW +"")
print("Calculadora Bit a Bit")
print("")
print(Fore.WHITE + "1. AND (&)")
print("2. OR (|)")
print("3. XOR (^)")
print("0. Salir")
print(Fore.YELLOW + " --------------------------- ")
opcion = input("Elige una opción: ")
print(" --------------------------- ")

#Verificamos si ingreso la opción 0 para salir del programa.
if opcion == '0':
    print("Saliendo del programa ")
    print("")
    exit()
    
if opcion in ['1', '2', '3']:
    #Solicito el ingreso de los numeros enteros al usuario.
    numA = int(input("Número A (entero): "))
    numB = int(input("Número B (entero): "))

    if opcion == '1':
        #Calculo la operación seleccionada en numero decimal
        resultado = numA & numB
        simbolo = '&'
        data = """Operación elegida AND = Produce una salida de 1 (verdadero) solo si todas las entradas son 1. 
Es decir `Ambas condiciones deben cumplirse`"""
    elif opcion == '2':
        #Calculo la operación seleccionada en numero decimal
        resultado = numA | numB
        simbolo = '|'
        data = """Operación elegida OR = Genera una salida de 1 si al menos una de las entradas es 1. 
Es decir `Al menos una condición debe cumplirse` """
    elif opcion == '3':
        #Calculo la operación seleccionada en numero decimal
        resultado = numA ^ numB
        simbolo = '^'
        data = """Operación elegida XOR = La salida es 1 únicamente si las entradas son diferentes (una es 1 y la otra 0). 
Es decir `Solo una condición puede cumplirse, pero no ambas` """
else: 
    print("Opción inválida.")
    print("Saliendo del programa ")
    print(" --------------------------- ")
    exit()
    
print(" --------------------------- ")
print(Fore.BLUE + f"{data}")
print("")
print(Fore.GREEN + f"Operación en decimal: {numA} {simbolo} {numB} = {resultado} ")
#Calculo la operación en binario.
# bin(numA) esta parte convierte el numero a binario y [2:] esta parte de la expresión elimina los dos primeros caracteres que indican que el número es binario.
print(f"Operacion en binario: {bin(numA)[2:]} {simbolo} {bin(numB)[2:]} = {bin(resultado)[2:]}")
#Deja el estilo por defecto.
print(Style.RESET_ALL + "")

    