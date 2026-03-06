print("COMPROBACION DE INVITADOS")

mis_invitados = ["alejandra", "ceci", "darlin", "sara", "admin"]

while True:
    nombre = input("Ingresa tu nombre: ").lower()
    
    if nombre == "salir":
        print("Programa finalizado")
        break

    if nombre == "admin":
        print("Bienvenido admin, tienes acceso total a la fiesta")

    elif nombre in mis_invitados:
        print(f"Bienvenido {nombre} a la fiesta")

    else:
        print(f"Lo siento {nombre}, no estás en la lista de invitados")