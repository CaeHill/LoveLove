import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Tela:
    def __init__(self, gerencia_album, gerencia_foto):
        self.root = tk.Tk()
        self.root.title("Álbum de Fotos")
        self.root.geometry("1200x800")

        self.canvas = tk.Canvas(self.root, width=1200, height=800, bg="white")
        self.canvas.pack()

        self.gerencia_album = gerencia_album
        self.gerencia_foto = gerencia_foto
        self.foto_atual = None
        self.offset_x = 0
        self.offset_y = 0

        self.desenhar_albuns()
        self.desenhar_fotos()

    def desenhar_albuns(self):
        """Desenha os slots do álbum na tela."""
        for album in self.gerencia_album.get_albuns():
            x, y = album.posicao
            self.canvas.create_rectangle(x - 50, y - 50, x + 50, y + 50, outline="black", width=2)
            self.canvas.create_text(x, y + 60, text=album.descricao, font=("Arial", 10))

    def desenhar_fotos(self):
        """Desenha as fotos na tela."""
        for foto in self.gerencia_foto.get_fotos():
            img = Image.open(foto.caminho).resize((100, 100))
            img = ImageTk.PhotoImage(img)
            foto.widget = self.canvas.create_image(foto.posicao, image=img, anchor="nw")
            self.canvas.tag_bind(foto.widget, "<ButtonPress-1>", self.pegar_foto)
            self.canvas.tag_bind(foto.widget, "<B1-Motion>", self.arrastar_foto)
            self.canvas.tag_bind(foto.widget, "<ButtonRelease-1>", self.soltar_foto)
            foto.image = img  # Previne o garbage collection

    def pegar_foto(self, event):
        """Inicia o arrasto da foto."""
        widget = self.canvas.find_withtag("current")[0]
        self.foto_atual = next(f for f in self.gerencia_foto.get_fotos() if f.widget == widget)
        self.offset_x = event.x
        self.offset_y = event.y

    def arrastar_foto(self, event):
        """Move a foto com o mouse."""
        if self.foto_atual:
            x, y = event.x - self.offset_x, event.y - self.offset_y
            self.canvas.move(self.foto_atual.widget, x, y)
            self.offset_x = event.x
            self.offset_y = event.y

    def soltar_foto(self, event):
        """Finaliza o arrasto da foto e verifica posicionamento."""
        if self.foto_atual:
            x, y = self.canvas.coords(self.foto_atual.widget)
            for album in self.gerencia_album.get_albuns():
                if abs(x - album.posicao[0]) < 50 and abs(y - album.posicao[1]) < 50:
                    self.canvas.coords(self.foto_atual.widget, album.posicao)
                    album.adicionar_foto(self.foto_atual)
                    break
            self.foto_atual = None

    def executar(self):
        self.root.mainloop()
