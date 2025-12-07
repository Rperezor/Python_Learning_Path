#Conversor Universal

# Intenta pedirle un número al usuario.
try:
    ## Pedimos al usuario la temperatura en Celsius
    celsius = float(input("Introduce la temperatura el Celsius: "))
# Si da error, muestra el siguiente mensaje:
except ValueError:
    print("Debes introducir un número (ejemplo: 25.3), no una cadena de texto")
# Si no hay error, el try es correcto entonces realiza la operación y muestra el mensaje
else:
    ## Realizamos la operación para su conversión a fahrenheit
    fahrenheit = celsius * 9/5 + 32
    ## Mostramos el resultado de la conversión
    print(f"La conversión de Celsius (C) a Fahrenheit (F) es: {fahrenheit:.2f}")
# Pase lo que pase muestra el mensaje final.
finally:
    print("Fin del la conversión")