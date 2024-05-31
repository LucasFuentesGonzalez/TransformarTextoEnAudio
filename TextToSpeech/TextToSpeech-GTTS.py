import os
import pygame
from gtts import gTTS

def fTransformarTextoEnAudio(sTexto, lang="es", speaker="es"):
    # Inicializar el sistema de video de Pygame
    pygame.init()

    # Obtener la ruta del directorio actual del script
    sRutaScript = os.path.dirname(os.path.abspath(__file__))
    # Crear la ruta completa para el archivo de audio
    sRutaAudio = os.path.join(sRutaScript, "output.mp3")

    # Crear el archivo de audio con gTTS
    tts = gTTS(text=sTexto, lang=lang, tld=speaker)
    tts.save(sRutaAudio)  # Guardar el archivo de audio en la ruta especificada

    # Reproducir el archivo de audio con Pygame
    pygame.mixer.init()  # Inicializar Pygame mixer
    pygame.mixer.music.load(sRutaAudio)  # Cargar el archivo de audio
    pygame.mixer.music.play()  # Reproducir el archivo de audio

    # Esperar hasta que la reproducción termine
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Detectar si se cierra la ventana
                pygame.mixer.music.stop()  # Detener la reproducción si se cierra la ventana
                break

    # Cerrar Pygame
    pygame.quit()


if __name__ == "__main__":

    sTexto = """
    HOLAHOLAHOLAHOLAHOLA
    HOLAHOLAHOLAHOLAHOLA
    HOLAHOLAHOLAHOLAHOLA
    """

    fTransformarTextoEnAudio(sTexto)
