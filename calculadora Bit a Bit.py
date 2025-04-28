from colorama import Fore, Style
def mostrar_menu():
    print(Fore.YELLOW + " --------------------------- ")
    print("")
    print("Calculadora Bit a Bit")
    print("")
    print(Fore.BLACK + "1. AND (&)")
    print("2. OR (|)")
    print("3. XOR (^)")
    print("0. Salir")
    print(Fore.YELLOW + " --------------------------- ")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        print(" --------------------------- ")
#podemos salir de la calculadora si ya realizamos la operacion
        if opcion == '0':
            print("🔄 Saliendo del programa ")
            print("")
            break

        if opcion in ['1', '2', '3']:
             
            try:
                numA = int(input("Número A (entero): "))
                numB = int(input("Número B (entero): "))

                if opcion == '1':
                    resultado = numA & numB
                    simbolo = '&'
                    data = """
# Compuerta AND = Produce una salida de 1 (verdadero) solo si todas las entradas son 1. 
Es como decir `Ambas condiciones deben cumplirse`
                    """
                elif opcion == '2':
                    resultado = numA | numB
                    simbolo = '|'
                    data = """
# Compuerta OR = Genera una salida de 1 si al menos una de las entradas es 1. 
Es como decir `Una u otra condición puede cumplirse`
                        """
                elif opcion == '3':
                    resultado = numA ^ numB
                    simbolo = '^'
                    data = """
# Compuerta XOR = La salida es 1 únicamente si las entradas son diferentes (una es 1 y la otra 0). 
Es como decir `Solo una condición puede cumplirse, pero no ambas`
                    """
                print(" --------------------------- ")
                print(Fore.GREEN + f"{data}")
                print(f"Operación en decimal: {numA} {simbolo} {numB} = {resultado} ")
                print(f"Operacion en binario: {bin(numA)[2:]} {simbolo} {bin(numB)[2:]} = {bin(resultado)[2:]}")
                print(Style.RESET_ALL + "")
            except ValueError:
                print(" --------------------------- ")
                print(" Ingresa solo números enteros.")
        else:
            print(" --------------------------- ")
            print(" Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()