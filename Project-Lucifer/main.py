
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicliberary
#pip install pocketsphinx

recoginzer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
     if "open google" in c.lower():
          webbrowser.open("http://google.com")
     elif "open youtube" in c.lower():
          webbrowser.open("http://youtube.com")
     elif "open instagram" in c.lower():
          webbrowser.open("http://instagram.com")
     elif c.lower().startswith("play"):
          songs= c.lower().split(" ")[1]
          link = musicliberary.music[songs]
          webbrowser.open(link)
 
if __name__ == "__main__":
    speak("initializing lucifer....")


    while True:
    #LISTEN FOR HE WAKW WORD# obtain audio from the microphone
    #OBTAIN AUDIO FROM MICROPHONE
        r = sr.Recognizer()
         

        print("recoganizing")
            # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                    print("Listning....")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "lucifer"):
                 speak("Yes sir")
                 #Listen for command
                 with sr.Microphone() as source:
                    print("lucifer Active....")
                    audio = r.listen(source)
                    command  = r.recognize_google(audio)
                    processcommand(command)
        
        
        except Exception as e:
                print("Error; {0}".format(e))
