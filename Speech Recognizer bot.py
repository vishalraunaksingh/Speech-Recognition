import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyjokes
import ctypes
import winshell
import time
from ecapture import ecapture as ec
import cv2
from requests import get
import pywhatkit as kit
import subprocess
import warnings
warnings.filterwarnings("ignore")
os.chdir("D:\Speech Recognition")

 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
       speak("good morning!")

    elif hour>=12 and hour<18:
         speak("good afternoon!")

    else:
        speak("good evening!")

    speak("I am Kasper sir, Please tell me how may I help you") 


def takeCommand():
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        
        try:
            print("Recoginzing....")
            query = r.recognize_google(audio, language='en-US')
            print(f"user said: {query}\n")
            
        except Exception as e:
            #print(e)
            print("Say that again please....")
            return "None"
        return query
     
        
if __name__ == "__main__":
   #speak("Hello")
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google web' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open google' in query:
            speak("Sir, What should I search on google\n")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow, Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play from youtube' in query:
            speak("Sir, What should I search on youtube\n")
            cm1 = takeCommand().lower()
            kit.playonyt(f"{cm1}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            strTime = datetime.datetime.now().strftime("%m/%d/%Y")    
            speak(f"Sir, the date is {strTime}")
            print(f"Sir, the date is {strTime}")

        elif 'news in english' in query:
            speak("Here you go to TimesofIndia\n")
            webbrowser.open("https://timesofindia.indiatimes.com/topic/online-reading")

        elif 'news in bengali' in query:
            speak("Here you go to Ananda Bazar Patrika\n")
            webbrowser.open("https://www.anandabazar.com/")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
		
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
    
        elif 'thank you' in query :
            speak("Welcome sir")
            
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Souvik Biswas, Souvik Roy, Arpan Halder, Vishal Singh.")
            print("I have been created by Souvik Biswas, Souvik Roy, Arpan Halder, Vishal Singh.")

        elif "who are you" in query:    
            speak("I am your virtual assistant Kasper Sir.")
            print("I am your virtual assistant Kasper Sir.")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"Location of wallpaper",
													0)
            speak("Background changed successfully")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
    
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==13:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "take a photo" in query:
            key = cv2. waitKey(1)
            webcam = cv2.VideoCapture(0)
            while True:
                try:
                    check, frame = webcam.read()
                    print(check) #prints true as long as the webcam is running
                    print(frame) #prints matrix values of each framecd 
                    cv2.imshow("Capturing", frame)
                    key = cv2.waitKey(1)
                    if key == ord('s'): 
                        cv2.imwrite(filename='saved_img.jpg', img=frame)
                        webcam.release()
                        img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                        img_new = cv2.imshow("Captured Image", img_new)
                        cv2.waitKey(1650)
                        cv2.destroyAllWindows()
                        print("Processing image...")
                        img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                        print("Converting RGB image to grayscale...")
                        gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                        print("Converted RGB image to grayscale...")
                        print("Resizing image to 28x28 scale...")
                        img_ = cv2.resize(gray,(28,28))
                        print("Resized...")
                        img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                        print("Image saved!")
                    
                        break
                    elif key == ord('q'):
                        print("Turning off camera.")
                        webcam.release()
                        print("Camera off.")
                        print("Program ended.")
                        cv2.destroyAllWindows()
                        break
                    
                except(KeyboardInterrupt):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your ip address is {ip}")
            print(f"Your ip address is {ip}")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "open note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown /h")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown /p /f')

        elif 'stop' in query or 'thanks for help' in query:
            speak("thanks for using me sir, have a good day.")
            print("Thanks for using me sir, have a good day.")
            break
            exit()

