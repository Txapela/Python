from gtts import gTTS
from playsound import playsound
 
def voz(text_file, lang, name_file):
    with open(text_file, "r") as file:
        text = file.readline()
    file = gTTS(text=text,lang=lang, slow = False)
    filename = name_file
    file.save(filename)
 
voz("contenido.txt","es","voz.mp3")
print("Reproduciendo:")
audio = "voz.mp3"
playsound(audio)
print("Reproducido.")