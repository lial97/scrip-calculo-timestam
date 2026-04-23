import time

def calcular_timestamp():
    # 1. Obtener el timestamp actual (en segundos)
    timestamp_actual = time.time()
    print(f"Timestamp actual: {timestamp_actual}")

    # 2. Pedir al usuario qué desea sumar
    print("\n¿Qué deseas añadir al timestamp?")
    print("1. Horas")
    print("2. Minutos")
    print("3. Dias")
    opcion = input("Elige una opción (1, 2 o 3): ")

    # 3. Procesar la entrada y realizar el cálculo
    try:
        cantidad = float(input("Ingresa la cantidad a sumar: "))
        
        if opcion == "1":
            # Convertir horas a segundos: horas * 60 min * 60 seg
            segundos_a_sumar = cantidad * 3600
            unidad = "horas"

        elif opcion == "2":
            # Convertir minutos a segundos: minutos * 60 seg
            segundos_a_sumar = cantidad * 60
            unidad = "minutos"
        elif opcion == "3":
            #convertir a dias:
            unidad = "días"
            segundos_a_sumar = cantidad * 86400
        else:
            print("Opción no válida.")
            return

        # 4. Calcular el nuevo timestamp
        nuevo_timestamp = int(timestamp_actual + segundos_a_sumar)

        # 5. Mostrar resultados
        print("\n" + "="*30)
        print(f"Resultado tras sumar {cantidad} {unidad}:")
        print(f"Nuevo Timestamp: {nuevo_timestamp}")
        print("="*30)

    except ValueError:
        print("Error: Por favor ingresa un número válido.")

if __name__ == "__main__":
    calcular_timestamp()
