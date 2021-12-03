
## 1 - Import the packages that we need :
import speech_recognition as sr
import gtts # permet d'avoir speech recogniton developper par google
import playsound 
import os

# initialisatoin de Recognizer
r = sr.Recognizer()

# fonction pour recorder l'audio 
def get_audio():
    with sr.Microphone() as source: # ceci est activer une fois il y a un son
        print("Say something !")
        audio = r.listen(source) # convertir ce qui est enregistrer en audio
    return audio

# convertir l'audio en texte :
def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio) # utilisation de lAPI de google
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError:
        print("could not request results from API")
    return text

# Jouer une morceau : lire un texte passer en param (text to speech module)
def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = "temp.mp3"
        tts.save(tempfile)
        playsound.playsound("temp.mp3")
        os.remove(tempfile)
    except AssertionError:
        print("Could not play sound")


# Definiton de l'acitivation :
Activation_COMMAND = "hi"

# Run the application :
if __name__ == "__main__" :
    # load the audio :
    audio =  get_audio()
    # Convert the audio to text :
    command = audio_to_text(audio)
    print("You said : " + command)
    while Activation_COMMAND in command.lower():
        # L'application ne commence a tourner que lorsque il entend Bonjour OUSSAMA
        print("activated")
        # say : How can I help you ?
        play_sound("How can I help you ?")
        # Entendre l'utilisateur :
        note_audio =  get_audio()
        note_text = audio_to_text(note_audio)
        print("You just said : "+ note_text)
        play_sound("You said "+ note_text)

        play_sound("Stored new item")

        audio =  get_audio()
        command = audio_to_text(audio)

