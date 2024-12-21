from foto import Foto
from album import Album
from gerenciaFoto import GerenciaFoto
from gerenciaAlbum import GerenciaAlbum
from tela import Tela

# Cria os gerenciadores
gerencia_foto = GerenciaFoto()
gerencia_album = GerenciaAlbum()

# Adiciona fotos
for i in range(1, 13):
    foto = Foto(f"Foto {i}", f"C:/Users/hillc/PycharmProjects/LoveLove/Photos/foto{i}.jpg", (800, i * 100))
    gerencia_foto.adicionar_foto(foto)

# Adiciona slots no álbum
for i in range(1, 13):
    album = Album(f"Descrição da foto {i}", (100, i * 100))
    gerencia_album.adicionar_album(album)

# Inicia a tela
tela = Tela(gerencia_album, gerencia_foto)
tela.executar()
