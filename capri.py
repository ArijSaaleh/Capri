import sys
sys.path.append('/home/arij/.local/lib/python3.9/site-packages')
import pyjokes
from ai import AI

capri = AI()

def joke ():
    funny = pyjokes.get_joke()
    print(funny)
    capri.say(funny)

command =""

while True and command !="goodbye":
    command = capri.listen()
    print("command was:", command)

    if command == "tell me a joke":
        joke()
capri.say("Goodbye, I'm going to sleep now")
