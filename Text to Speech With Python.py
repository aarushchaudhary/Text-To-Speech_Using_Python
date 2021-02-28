# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()

# testing
engine.say("Hello There")
engine.say("I am Aarush Chaudhary")
engine.say("This is my first Text To Speech program in Python")
engine.say("Just Don't Forget 3 things")
engine.say("Follow me on GitHub")
engine.say("May the 4th is Star Wars Day")
engine.say("Star Wars The Bad Batch will premire on May the 4th on Disney Plus")
engine.say("May the Force be with you")
engine.runAndWait()
