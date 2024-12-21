class GerenciaAlbum:
    def __init__(self):
        self.albuns = []

    def adicionar_album(self, album):
        self.albuns.append(album)

    def get_albuns(self):
        return self.albuns
