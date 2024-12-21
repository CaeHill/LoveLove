class GerenciaFoto:
    def __init__(self):
        self.fotos = []

    def adicionar_foto(self, foto):
        self.fotos.append(foto)

    def get_fotos(self):
        return self.fotos
