#If windows user; Before using please download the pyttsx3 module on your laptop 
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
while True:
    # Take user input
    text = input("Enter something for the computer to say: ")
    #Exit condition
    if text == "q":
        engine.say("Bye Bye Friend")
        engine.runAndWait()
        break
    # Speak the text
    engine.say(text)
    engine.runAndWait()