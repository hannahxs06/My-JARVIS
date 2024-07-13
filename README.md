# Voice-Activated Assistant Using GPT-4 and Whisper to Create JARVIS 

## Introduction

This project demonstrates how to create a voice-activated assistant that listens to your speech, transcribes it into text, sends the text to OpenAI's GPT-4 model, and then speaks out the response. The assistant mimics JARVIS from Iron Man and can be continuously engaged in a conversation. 

## Getting Started

### Pre-requisites

Before you begin, ensure you have the following:

1. Python installed on your machine.
2. A microphone connected to your machine.
3. An OpenAI API key from ChatGPT.

### Installing

Follow these steps to set up your development environment:

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
2. **Install the required libraries**:
   ```bash
   pip install openai pyttsx3 pyaudio SpeechRecognition python-dotenv
3. **Set up your Open API Key**
   ```bash
   OPENAI_API_KEY=your_openai_api_key

## Running the Code
To run the code, execute the following command in your terminal:
```bash
python main.py
```
Or you can execute it in a text editor like VS Code.

## Built With
  * openai - Used for interacting with GPT-4.
  * pyttsx3 - Used for text-to-speech conversion.
  * pyaudio - Used for audio input/output.
  * SpeechRecognition - Used for speech recognition.
  * python-dotenv - Used for loading environment variables.

## Acknowledgements
Huge thanks to this YouTube video for helping me build the [Voice-Activated Assistant Using GPT-4 and Whisper to Create JARVIS](https://www.youtube.com/watch?v=BEw5EFqCCEI&t=898s).


