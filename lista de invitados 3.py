# Sistema de Gestión de Acceso v2.0
# Desarrollado para clase de Python en iOS

def mostrar_menu_admin(lista_invitados):
    """Función para centralizar las acciones del administrador"""
    print("\n--- PANEL DE CONTROL ---")
    print("1. Agregar invitado")
    print("2. Eliminar invitado")
    print("3. Ver lista completa")
    print("4. Salir del panel")
    
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        nuevo = input("Nombre del nuevo invitado: ").lower().strip()
        if nuevo not in lista_invitados:
            lista_invitados.append(nuevo)
            print(f"✅ {nuevo} ha sido añadido.")
        else:
            print("⚠️ Ese nombre ya está en la lista.")

    elif opcion == "2":
        eliminar = input("Nombre a eliminar: ").lower().strip()
        if eliminar in lista_invitados:
            lista_invitados.remove(eliminar) # .remove() busca y quita el elemento
            print(f"❌ {eliminar} ha sido removido de la lista.")
        else:
            print("⚠️ El nombre no se encuentra en la lista.")

    elif opcion == "3":
        print(f"\n📋 Invitados actuales ({len(lista_invitados)}):")
        # Usamos un bucle for para imprimir la lista de forma elegante
        for i, invitado in enumerate(lista_invitados, 1):
            print(f"{i}. {invitado.capitalize()}")

    elif opcion == "4":
        print("Saliendo del panel de administración...")
    else:
        print("Opción no válida.")

# --- Lógica Principal ---

invitados = ["alejandra", "ceci", "darlin", "sara", "admin"]

while True:
    # .strip() elimina espacios accidentales al inicio o final
    usuario = input("\nIdentifícate (o 'salir'): ").lower().strip()

    if usuario == "salir":
        print("🔒 Sistema bloqueado. ¡Adiós!")
        break

    if usuario == "admin":
        print("\n🔑 Acceso concedido, Administrador.")
        mostrar_menu_admin(invitados)
    
    elif usuario in invitados:
        print(f"✨ ¡Bienvenido/a, {usuario.capitalize()}! Disfruta la fiesta.")
    
    else:
        print(f"🚫 Acceso denegado: {usuario} no está en la lista.")