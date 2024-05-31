import pyttsx3

def fTransformarTextoEnAudio(sTexto, rate, volume):
    # Configurar el motor de texto a voz
    oMotor = pyttsx3.init()
    lVoces = oMotor.getProperty('voices')  # Obtener las voces disponibles

    # Buscar una voz masculina
    sVozHombre = None
    for sVoz in lVoces:
        if "male" in sVoz.name.lower():
            sVozHombre = sVoz
            break

    if sVozHombre:
        oMotor.setProperty('voice', sVozHombre.id)  # Establecer la voz masculina
    else:
        print("No se encontró una voz masculina. Se utilizará la voz predeterminada.")

    oMotor.setProperty('rate', rate)  # Establecer la velocidad de lectura
    oMotor.setProperty('volume', volume)  # Establecer el volumen

    # Reproducir el texto como voz
    oMotor.say(sTexto)
    oMotor.runAndWait()

if __name__ == "__main__":
    sTexto = """
    HOLAHOLAHOLAHOLAHOLA
    HOLAHOLAHOLAHOLAHOLA
    HOLAHOLAHOLAHOLAHOLA
    """

    fTransformarTextoEnAudio(sTexto, rate=100, volume=1.0)  # Ajustar la velocidad y el volumen según sea necesario
