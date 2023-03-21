import config
import gradio as gr
import openai
import subprocess
import soundfile as sf
from gtts import gTTS
import os

# OpenAI API Key to authenticate requests
openai.api_key = config.OPENAI_API_KEY

# List of roles to choose from in the dropdown
roles = ['Therapist', 'Lawyer', 'Social Media Manager', 'Data Analyst', 'Language Model Developer', 'Virtual Assistant',
         'E-Learning Developer', 'Chat Moderator', 'Search Engine Optimizer', 'AI Research Scientist',
         'Content Manager', 'Chatbot Developer', 'Photograph']

# The initial system message to ensure the role of chatGPT
messages = [{"role": "system", "content": ''}]


# Function to update the system message with the role of chatGPT
def update_role(role):
    global messages
    messages[0]["content"] = f'You are a {role}. Respond to all input in 25 words or less.'


# Function to setup pyttsx3 for speech output on win/mac/linux
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save('temp_audio.mp3')
    if os.name == 'posix':  # macOS / Linux
        subprocess.call(['afplay', 'temp_audio.mp3'])
    else:  # Windows
        subprocess.call(['start', 'temp_audio.mp3'])


# Function to transcribe audio and generate a response to OpenAI
def transcribe(role, audio):
    global messages
    update_role(role)

    data, samplerate = sf.read(audio)
    sf.write('temp_audio.wav', data, samplerate, format='wav', subtype='PCM_16')

    with open('temp_audio.wav', 'rb') as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    # Use the text_to_speech function to convert the text to speech
    text_to_speech(system_message['content'])

    # Output the response to the user using the system's text-to-speech engine (macOS only)
    # subprocess.call(["say", system_message['content']])

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript


# Create the interface including the dropdown for selecting the role of chatGPT and the audio input
role_dropdown = gr.Dropdown(choices=roles, label="Select ChatGPT Role")

ui = gr.Interface(
    fn=transcribe,
    inputs=[
        role_dropdown,
        gr.Audio(source="microphone", type="filepath"),
    ],
    outputs="text",
    title="Talk to ChatGPT",
)

# Launch the interface
ui.launch(share=True)
