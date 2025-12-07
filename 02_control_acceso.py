    #CONTROL DE ACCESO

try:
# Código con posibles fallos
# Pedimos la edad del usuario y la guardamos en una variable para su posterior verificación.
    print("Introduzca su edad para la compra de entradas")
    age = int(input("EDAD: "))
#mostramos la excepcion ValueError en caso de que le pasemos letras, decimales o números negativos)
    if age < 0:
        raise ValueError
except ValueError:
    print(f"La edad debe de ser un número entero (ej: 25) no puede contener ni letras, ni decimales, ni ser un número negativo.")
else:
    if age >= 0 and age <= 17:
        print(f"Tienes {age} años, Eres MENOR de edad.")
    elif age >= 18 and age <= 64:
        print(f"Tienes {age} años, Eres MAYOR de edad. Entrada general 10€")
    elif age >= 65:
        print(f"Tienes {age} años, Eres JUBILADO. Entrada VIP, pasa gratis")
#Creamos un mensaje final de que el proceso ha terminado
finally:
    print("El proceso de verificación de edad para la compra de entradas ha terminado.")