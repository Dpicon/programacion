import customtkinter as ctk

# Configuración de la apariencia
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Pro")
        self.geometry("300x450")

        # Pantalla de visualización
        self.entry = ctk.CTkEntry(self, width=280, height=50, font=("Roboto", 24), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Definición de botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        fila = 1
        columna = 0

        for boton in botones:
            comando = lambda b=boton: self.presionar(b)
            ctk.CTkButton(self, text=boton, width=60, height=60, font=("Roboto", 18),
                          command=comando).grid(row=fila, column=columna, padx=5, pady=5)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

    def presionar(self, tecla):
        if tecla == "=":
            try:
                resultado = eval(self.entry.get())
                self.entry.delete(0, "end")
                self.entry.insert(0, str(resultado))
            except:
                self.entry.delete(0, "end")
                self.entry.insert(0, "Error")
        elif tecla == "C":
            self.entry.delete(0, "end")
        else:
            self.entry.insert("end", tecla)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()