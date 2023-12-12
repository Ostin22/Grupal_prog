print("Menu de Restaurante")
menu = 0
burger = 0
pollo = 0
postres = 0
while menu != 4:
    menu = int(input("Ingrese un numero, 1 es para hamburguesas, 2 es para pollo, 3 es para postres y 4 es para salir del menu: "))
    if menu == 1: #Activar el menu de hamburguesas
        burger = int(input("Ingrese 1 para la hamburguesa simple, 2 para la doble, 3 para la doble con tocino: "))
        if burger == 1: #Hamburguesa simple
            burger = 2.5
        if burger == 2: #Hamburguesa doble
            burger = 5
        if burger == 3: #Hamburguesa doble con tocino
            burger = 7
        menu = menu - 1
        print(f"El valor de su hamburguesa es: {burger}")
    if menu == 2: #Activar el menu de pollo
        pollo = int(input("Ingrese 1 para 1/2 pollo, 2 para 1/4 de pollo, 3 para 1/8 de pollo y 4 para un menu familiar: "))
        if pollo == 1: # 1/2 de pollo
            pollo = 6
        if pollo == 2: # 1/4 de pollo
            pollo = 4
        if pollo == 3: # 1/8 de pollo
            pollo = 3
        if pollo == 4: # menu familiar
            pollo = 12
        menu = menu - 2
        print(f"El valor de su pedido de pollo es: {pollo}")
    if menu == 3: #Activar el menu de postres
        postres = int(input("Ingrese su postre, 1 para tres leches, 2 para brownie: "))
        if postres == 1: #Tres leches
            postres = 2.5
        if postres == 2: #Brownie
            postres = 3
        menu = menu - 3
        print(f"El valor de su postre es {postres}")
total = burger + pollo + postres
print(f"Su menu consta de: \nHamburguesas: {burger} \nPollo: {pollo} \nPostre: {postres}")
print(f"Su valor total es: {total}")
        


        

        
        
    


