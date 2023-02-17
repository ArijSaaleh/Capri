from neuralintents import GenericAssistant 
import speech_recognition
import pyttsx3 as tts 
import sys 

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)


def greet():
    print("You entered the greetings function")
    speaker.say("Hello How can I help you")
    speaker.runAndWait()

def bye():
    print("You entered the bye function")
    speaker.say("Bye until next time!")
    speaker.runAndWait()
    sys.exit(0)

mappings = {'greeting' : greet, 'goodbye': bye}

assistant = GenericAssistant('intents.json', intent_methods=mappings,model_name='test_model')
assistant.train_model()
assistant.save_model()
while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message= message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()