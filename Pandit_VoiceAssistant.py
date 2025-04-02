import os
import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import wikipedia
import openai
from googletrans import Translator

# Load OpenAI API Key from Environment Variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Adjust speech speed

def speak(text):
    """Convert text to speech."""
    print(f"Pandit: {text}")  # Print for reference
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Recognize speech input from user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        speak("Could not request results, check your internet connection.")
        return None

def search_wikipedia(query):
    """Search Wikipedia for a given query."""
    if not query:
        speak("Please specify what you want to search on Wikipedia.")
        return

    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find any information on that.")

def browse_web(query):
    """Open websites based on the command."""
    if "youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "google" in query:
        speak("Searching Google")
        webbrowser.open("https://www.google.com")
    else:
        speak(f"Searching the web for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

def translate_text(text, target_language='en'):
    """Translate text into the specified language."""
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text

def open_application(command):
    """Open Windows applications."""
    if "notepad" in command:
        speak("Opening Notepad")
        pyautogui.hotkey('win', 'r')
        pyautogui.typewrite("notepad")
        pyautogui.press("enter")
    elif "chrome" in command:
        speak("Opening Google Chrome")
        pyautogui.hotkey('win', 'r')
        pyautogui.typewrite("chrome")
        pyautogui.press("enter")
    elif "file explorer" in command:
        speak("Opening File Explorer")
        pyautogui.hotkey('win', 'e')
    else:
        speak("Sorry, I can't open that application yet.")

def get_ai_response(prompt):
    """Get a response from OpenAI's GPT model."""
    if not openai.api_key:
        speak("OpenAI API key is missing. Please set it up.")
        return "API key missing."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        speak(f"An error occurred: {str(e)}")
        return "Error in AI response."

def handle_command(command):
    """Process and execute user commands."""
    if not command:
        return

    if "hello" in command:
        speak("Hello! How can I assist you today?")

    elif "your name" in command:
        speak("I am Pandit, your personal voice assistant.")

    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        if query:
            speak(f"Searching Wikipedia for {query}")
            search_wikipedia(query)
        else:
            speak("Please specify what you want to search on Wikipedia.")

    elif "open" in command:
        open_application(command)

    elif "search" in command or "browse" in command:
        query = command.replace("search", "").replace("browse", "").strip()
        if query:
            browse_web(query)
        else:
            speak("Please specify what you want to search.")

    elif "translate" in command:
        speak("What do you want to translate?")
        text_to_translate = recognize_speech()
        speak("Which language do you want to translate to?")
        target_language = recognize_speech()
        if text_to_translate and target_language:
            translated = translate_text(text_to_translate, target_language)
            speak(f"Translation: {translated}")

    elif "ai" in command or "chatbot" in command:
        speak("What do you want to ask the AI?")
        user_input = recognize_speech()
        if user_input:
            ai_response = get_ai_response(user_input)
            speak(ai_response)

    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day.")
        exit()

    else:
        speak("I'm still learning, but I will try to improve.")

if __name__ == "__main__":
    speak("Hello! I am Pandit, your personal assistant. How can I help you?")
    while True:
        command = recognize_speech()
        if command:
            handle_command(command)
