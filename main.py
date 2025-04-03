import speech_recognition as sr
import pyaudio as p
import webbrowser
import pyttsx3
import Jarvis.music_lib as music_lib
from openai import OpenAI
# from elevenlabs import generate, play, set_api_key
# from elevenlabs import generate, play, set_api_key
# from elevenlabs.client import ElevenLabs
# from elevenlabs import generate, play, set_api_key


# set_api_key=("sk_14d7ce7ed0c9908ef53c98b665bb8a33c912179e78948f95")

# audio = generate(text="Hello, this is a test using Eleven Labs!", voice="Rachel")
# play(audio)


r = sr.Recognizer() # Making a object to recognize
engine = pyttsx3.init()
# set_api_key("sk_14d7ce7ed0c9908ef53c98b665bb8a33c912179e78948f95")

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     """Use Eleven Labs AI voice for speech output"""
#     audio = generate(text=text, voice="Grandpa Spuds Oxley")  # Change "Rachel" to any available voice
#     play(audio)

def aiProcess(command):
    client = OpenAI(
    api_key="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"
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "Assistant", "content": "You are a virtual assistant named Jarvis who answers questions like Alexa and Google."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    print(completion.choices[0].message.content)


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_lib.music[song]
        webbrowser.open(link)
    else:
        print("AI Search")
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Tuning my Mind ...Jarvis")
    
    

    while True:
    # Listing for the Wake Word Jarvis
    # Obtain audio from microphone
        # r = sr.Recognizer()
       

        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                r.adjust_for_ambient_noise(source, duration=2)
                audio = r.listen(source, timeout=3,phrase_time_limit=3)
            word = r.recognize_google(audio)
            print(word)
            if (word.lower()=='jarvis'):
                speak("Yah")
                print("Jarvis is listening.")
                # Listening for Command
                with sr.Microphone() as source:
                    print("Listening....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    
                    processcommand(command)
        except Exception as e:
            print(f"Error: {e}")
            