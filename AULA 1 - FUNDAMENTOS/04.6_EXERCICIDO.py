# FACA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O AUDIO DE UM ARQUIVO MP3

import pygame  # type: ignore
import os

# Inicializa o pygame
pygame.init()

# Caminho do arquivo MP3 que você deseja reproduzir
hh = "hh.mp3"

try:
    # Carrega o arquivo MP3
    pygame.mixer.music.load(hh)

    # Reproduz o arquivo MP3
    pygame.mixer.music.play()

    # Aguarda o término da reprodução
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Controla a velocidade de atualização

except FileNotFoundError:
    print(f"Arquivo '{
          hh}' não encontrado. Verifique o caminho e o nome do arquivo.")
except pygame.error as e:
    print(f"Erro do pygame ao reproduzir o arquivo '{hh}': {e}")

finally:
    # Finaliza o pygame
    pygame.quit()
