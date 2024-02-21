import tkinter as tk

class AplicacionDibujo:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Dibujo")

        self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.coord_anterior = None  # Almacena las coordenadas anteriores del ratón

        self.canvas.bind("<B1-Motion>", self.dibujar)
        self.canvas.bind("<ButtonRelease-1>", self.restablecer_coords)

        boton_limpiar = tk.Button(root, text="Limpiar lienzo", command=self.limpiar_lienzo)
        boton_limpiar.pack(side=tk.BOTTOM)

    def dibujar(self, event):
        x, y = event.x, event.y

        if self.coord_anterior:
            x_anterior, y_anterior = self.coord_anterior
            self.canvas.create_line(x_anterior, y_anterior, x, y, fill="black", width=2)

        self.coord_anterior = (x, y)

    def restablecer_coords(self, event):
        self.coord_anterior = None

    def limpiar_lienzo(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionDibujo(root)
    root.mainloop()