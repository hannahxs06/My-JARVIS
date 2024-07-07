import openai
import os
import pyttsx3
import wave
import pyaudio
import speech_recognition as sr
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetch the API key from CHATGPT
OPENAI_KEY = ('PUT YOUR API KEY IN HERE')
if not OPENAI_KEY:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Set the API key
openai.api_key = OPENAI_KEY

def record_and_transcribe():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source, timeout=None)  # Listen until silence

    print("Recording finished.")
    audio_data = audio.get_wav_data()
    filename = "output.wav"

    with open(filename, "wb") as f:
        f.write(audio_data)

    print("Transcribing...")
    with open(filename, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript["text"]

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def send_to_chatGPT(messages, model="gpt-4", max_tokens=50):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    assistant_message = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": assistant_message})
    return assistant_message

messages = [{"role": "user", "content": "Please act like Jarvis from Iron Man."}]

while True:
    print("Listening for speech...")
    text = record_and_transcribe()
    print(f"User said: {text}")

    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages, max_tokens=200)  # Adjust max tokens as needed

    SpeakText(response)
    print(response)  # Print only the assistant's message content