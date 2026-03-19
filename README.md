🎧 Music Voice Assistant (Python)

A simple voice-controlled assistant built in Python that can play songs on YouTube using voice commands.

🚀 Features

🎤 Voice recognition using microphone
🗣️ Text-to-speech responses
▶️ Play songs directly on YouTube
⏸️ Pause and resume music
⏭️ Skip to next song
🧠 Wake word support ("Jarvis")
❌ Exit command

🛠️ Tech Stack

Python
SpeechRecognition
pyttsx3
pywhatkit
pyautogui

📦 Installation

Install required libraries:
pip install pyttsx3 SpeechRecognition pywhatkit pyautogui pyaudio

If pyaudio fails:

pip install pipwin
pipwin install pyaudio
▶️ How to Run
python main.py
🎙️ Commands
Command	Action
Jarvis play	Plays song on YouTube
Jarvis pause	Pauses music
Jarvis resume	Resumes music
Jarvis next	Plays next video
Jarvis exit	Stops assistant
📸 Demo

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e516fe6e-04aa-40c6-8402-605d4cd929b6" />

Make sure your microphone is working
Browser should be in focus for pause/resume to work
Internet connection is required for speech recognition

💡 Future Improvements
Wake word detection without delay
Offline speech recognition
GUI interface
More commands
