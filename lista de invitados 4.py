import os

# --- CONFIGURACIÓN DE SEGURIDAD ---
# Definimos la contraseña del administrador
PASSWORD_ADMIN = "1234" 

# Nombre del archivo de base de datos
ARCHIVO_INVITADOS = "invitados.txt"

def guardar_invitados(lista):
    """Guarda la lista en el archivo de texto."""
    try:
        with open(ARCHIVO_INVITADOS, "w") as archivo:
            for invitado in lista:
                archivo.write(f"{invitado}\n")
        print(f"--- Sistema: {len(lista)} registros sincronizados ---")
    except Exception as e:
        print(f"--- Error de disco: {e} ---")

def cargar_invitados():
    """Carga los datos al iniciar el programa."""
    if not os.path.exists(ARCHIVO_INVITADOS):
        lista_inicial = ["alejandra", "ceci", "darlin", "sara", "admin"]
        guardar_invitados(lista_inicial)
        return lista_inicial
    
    with open(ARCHIVO_INVITADOS, "r") as archivo:
        return [linea.strip().lower() for linea in archivo.readlines() if linea.strip()]

def mostrar_menu_admin(lista_invitados):
    """Panel de administración con lógica multi-nombre."""
    print("\n--- PANEL DE CONTROL ---")
    print("1. Agregar invitado(s)")
    print("2. Eliminar invitado")
    print("3. Ver lista completa")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        entrada = input("Nombres separados por coma: ")
        nuevos = [n.strip().lower() for n in entrada.split(",") if n.strip()]
        for invitado in nuevos:
            if invitado not in lista_invitados:
                lista_invitados.append(invitado)
                print(f"✅ {invitado.capitalize()} añadido.")
            else:
                print(f"⚠️ {invitado.capitalize()} ya existe.")
        guardar_invitados(lista_invitados)

    elif opcion == "2":
        eliminar = input("Nombre a borrar: ").lower().strip()
        if eliminar in lista_invitados:
            lista_invitados.remove(eliminar)
            guardar_invitados(lista_invitados)
            print(f"❌ {eliminar} eliminado.")
        else:
            print("⚠️ No encontrado.")

    elif opcion == "3":
        print(f"\n📋 LISTA ACTUAL:")
        for i, inv in enumerate(lista_invitados, 1):
            print(f"{i}. {inv.capitalize()}")

# --- LÓGICA PRINCIPAL ---

invitados = cargar_invitados()

while True:
    usuario = input("\nIdentifícate (o 'salir'): ").lower().strip()

    if usuario == "salir":
        print("🔒 Sistema cerrado.")
        break

    if usuario == "admin":
        # --- NUEVO: SISTEMA DE CONTRASEÑA ---
        intentos = 3
        acceso_concedido = False
        
        while intentos > 0:
            pw = input(f"Contraseña de Admin (Te quedan {intentos} intentos): ")
            
            if pw == PASSWORD_ADMIN:
                print("✅ Acceso concedido.")
                acceso_concedido = True
                break # Sale del bucle de la contraseña
            else:
                intentos -= 1
                print("❌ Incorrecto.")
        
        # Si logramos entrar, mostramos el menú
        if acceso_concedido:
            mostrar_menu_admin(invitados)
        else:
            print("🚫 Acceso bloqueado. Regresando al inicio.")
        # ------------------------------------

    elif usuario in invitados:
        print(f"✨ Bienvenido/a, {usuario.capitalize()}!")
    else:
        print(f"🚫 Acceso denegado.")





    # --- FIN DEL PROGRAMA ---