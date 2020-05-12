import speech_recognition as sr         # import speech library
import webbrowser
r = sr.Recognizer()                     # create a speech object
file = sr.AudioFile('open.wav')       # take file path
with file as source:                    # load the file
    audio = r.record(source)            # record from source
text = r.recognize_google(audio)        # recognize the speecch

if(text=='open Facebook'):
    webbrowser.open('https://facebook.com', new=2)
else:
    print(text+' - unable to recognize')                             # print the speech
