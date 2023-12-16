total2= 0
total3= 0
total4= 0
print("1. Habitación simple $500")
print("2. Habitación doble $700")
print("3. Habitación triple $1000")
habitacion = int(input("Elige una opción de habitación (1-3): "))

if habitacion == 1:
    total2 += 500
    tipo_habitacion = "Habitación simple"
elif habitacion == 2:
    total2 += 700
    tipo_habitacion = "Habitación doble"
elif habitacion == 3:
    total2 += 1000
    tipo_habitacion = "Habitación triple"
else:
    print("Opción de habitación no válida.")
    exit()

print("\nAdicionales")
print("1. Vista al mar + $100")
print("2. Vista al restaurante + $40")
print("3. Ninguno")

adicional = int(input("¿Cuál desea adicionar? (1-3): "))
if 1 <= adicional <= 3:
    if adicional == 1:
        total3 += 100
        tipo_adicional = "Vista al mar"
    elif adicional == 2:
        total3 += 40
        tipo_adicional = "Vista al restaurante"
    else:
        tipo_adicional = "Ninguno"

    huespedes = int(input("Ingrese el número de huéspedes: "))
    print("\nOpciones de alimentación")
    print("1. Todo incluido + $140")
    print("2. Todo incluido niños + $50")
    print("3. Solo desayuno + $80")
    print("4. Sin alimentación")

    total_huespedes = 0  
    contador = 1  
    while contador <= huespedes:  
        n = int(input("Ingresa el tipo de alimentación para el huésped {}: ".format(contador)))
        total_huespedes += (140 if n == 1 else
                            50 if n == 2 else
                            80 if n == 3 else 0)
        contador += 1

    print("\nResumen de opciones elegidas:")
    print("Tipo de habitación: {}".format(tipo_habitacion), f"precio: ${total2}")
    print("Adicional: {}".format(tipo_adicional),  f"precio: ${total3}")
    print("Total por los {}".format(huespedes),"huesped/es",  f"precio: ${ total_huespedes}")
    print("El total a pagar es: ${}".format( total_huespedes + total4 + total2 + total3 ))
else:

    print("Opción adicional no válida.")

