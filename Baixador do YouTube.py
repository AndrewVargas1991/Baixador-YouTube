# pip install pytube
from pytube import YouTube

# Caso não queira pesquisar um vídeo no YouTube, use o endereço abaixo
# Endereço: https://www.youtube.com/watch?v=jNQXAC9IVRw
# A propósito, esse é o link do vídeo mais antigo da história do YouTube

url = input('Cole aqui o endereço do vídeo e aperte ENTER: ')
youtube = YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download()

print('Vídeo baixado!')
input('Aperte ENTER para sair...')