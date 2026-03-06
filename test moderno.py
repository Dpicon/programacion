import customtkinter as ctk

app = ctk.CTk()
app.geometry("200x150")
app.title("Prueba")

btn = ctk.CTkButton(app, text="Botón Moderno", corner_radius=20)
btn.pack(pady=40)

app.mainloop()