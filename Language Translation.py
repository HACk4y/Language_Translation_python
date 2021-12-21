import googletrans
from googletrans.client import Translator
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
print('''8888888888888888888888888888888 Shoss your Language 8888888888888888888888888888888888888888888''')
print(googletrans.LANGUAGES)
print('''88888888888888888888888888888888888 Shoss your Language 88888888888888888888888888888888888888888888888888''')
inputr= input("Enter your input languages example en\n")
output=input("Enter your output languages example en\n")
input_lang= inputr
output_lang= output



try:
    with sr.Microphone() as source:
        print('Speak now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass

translated = translator.translate(text,dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('Output.mp3')
playsound.playsound('Output.mp3')

