import googletrans
import speech_recognition
import gtts
import playsound



recognizer=speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print('speak now')
    voice=recognizer.listen(source)
    text=recognizer.recognize_google(voice,language="en")
    print(text)
    
    
translator=googletrans.Translator()
translation=translator.translate(text,dest="ml")
print( translation.text)


converted_adio=gtts.gTTS(translation.text, lang="ml")
converted_adio.save("hello.mp3")
playsound.playsound("hello.mp3")