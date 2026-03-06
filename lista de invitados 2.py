print("COMPROBACION DE INVITADOS")

mis_invitados = ["alejandra", "ceci", "darlin", "sara", "admin"]

while True:
    nombre = input("Ingresa tu nombre: ").lower()
    
    if nombre == "salir":
        print("Programa finalizado")
        break

    if nombre == "admin":
        print("Bienvenido admin, tienes acceso total a la fiesta")

        # Preguntamos si quiere añadir a alguien
        accion = input("¿Deseas agregar a un nuevo invitado? (si/no): ").lower()
        
        if accion == "si":
            nuevo = input("Escribe el nombre del nuevo invitado: ").lower()
            # .append() toma lo que está en 'nuevo' y lo mete en la lista
            mis_invitados.append(nuevo)
            print(f"¡{nuevo} ha sido añadido con éxito!")
        else:
            
            #print("Entendido, continuamos.")
            print (f"Lista actual de invitados: {mis_invitados}")   

    elif nombre in mis_invitados:
        print(f"Bienvenido {nombre} a la fiesta")

    else:
        print(f"Lo siento {nombre}, no estás en la lista de invitados")