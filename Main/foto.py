class Foto:
    def __init__(self, nome, caminho, posicao_inicial):
        self.nome = nome
        self.caminho = caminho
        self.posicao = posicao_inicial  # (x, y) inicial no canvas
        self.album = None  # Álbum em que está (inicia fora de um álbum)

    def mover_para(self, nova_posicao):
        """Atualiza a posição da foto no canvas."""
        self.posicao = nova_posicao
