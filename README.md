# Pandit - Voice Assistant

Pandit is a personal AI-powered voice assistant built with Python. It can recognize voice commands, respond using text-to-speech, browse the web, search Wikipedia, translate languages, open applications, and even interact with OpenAI's GPT model.

## Features
- **Speech Recognition**: Listens to user commands using `speech_recognition`.
- **Text-to-Speech**: Responds with speech using `pyttsx3`.
- **Wikipedia Search**: Retrieves information from Wikipedia.
- **Web Browsing**: Opens Google, YouTube, and other search results.
- **Application Launcher**: Opens Windows applications like Notepad, Chrome, and File Explorer.
- **AI Chatbot**: Integrates with OpenAI's GPT model for AI-based responses.
- **Language Translation**: Translates text into different languages using Google Translate.

## Installation

### Prerequisites
Ensure you have **Python 3.8+** installed on your system. You also need an **OpenAI API Key**.

### Clone the Repository
```sh
git clone https://github.com/yourusername/Pandit-Assistant.git
cd Pandit-Assistant
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up OpenAI API Key
Create an environment variable for your OpenAI API key:

#### Windows (Command Prompt)
```sh
set OPENAI_API_KEY=your_api_key_here
```
#### macOS/Linux (Terminal)
```sh
export OPENAI_API_KEY=your_api_key_here
```

## Usage
Run the assistant using:
```sh
python pandit.py
```

## Commands Pandit Understands
| Command | Action |
|---------|--------|
| "Hello" | Greets the user |
| "Your name" | Introduces itself as Pandit |
| "Wikipedia [topic]" | Searches Wikipedia for the topic |
| "Open [app]" | Opens applications like Notepad, Chrome, etc. |
| "Search [query]" | Searches Google for the query |
| "Translate" | Translates spoken text into another language |
| "AI" or "Chatbot" | Asks OpenAI's GPT for a response |
| "Exit" or "Quit" | Exits the assistant |

## Technologies Used
- Python
- `speech_recognition`
- `pyttsx3`
- `pyautogui`
- `webbrowser`
- `wikipedia`
- `openai`
- `googletrans`

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, feel free to reach out at [your-email@example.com](mailto:your-email@example.com).

---
Give Pandit a try and let us know how we can improve! 🚀

