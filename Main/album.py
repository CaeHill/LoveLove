class Album:
    def __init__(self, descricao, posicao):
        self.descricao = descricao
        self.posicao = posicao  # (x, y) do slot no canvas
        self.foto = None  # Foto associada (inicia vazia)

    def adicionar_foto(self, foto):
        """Adiciona uma foto ao álbum."""
        self.foto = foto

    def remover_foto(self):
        """Remove a foto do álbum."""
        self.foto = None
