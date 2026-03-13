# 🎤 Personal Voice Assistant (Wake-Word Based)

A Python-based **personal voice assistant** built during my internship, featuring a **wake word ("Alexa")**, speech-to-text command recognition, rule-based intent handling, and text-to-speech responses.

The assistant stays idle until the wake word is detected, listens for a full spoken command, executes it, and then safely returns to idle mode.

---

## ✨ Features

* 🔊 Wake word activation ("Alexa")
* 🎧 Speech-to-text using Google Speech Recognition
* 🗣️ Text-to-speech responses (offline with `pyttsx3`)
* ⏱️ Handles long spoken commands (no 2–3 word limitation)
* 🔁 Smooth transitions without microphone freezing
* 🌐 Web automation (YouTube, Google search)
* 🎵 Play songs or playlists
* 📚 Wikipedia information lookup
* 🛑 Graceful cancel / exit handling

---

## 🧠 How It Works

```text
Idle (Listening for Wake Word)
        ↓
Wake Word Detected ("Alexa")
        ↓
Prompt ("Yes?")
        ↓
Listen for Full Command
        ↓
Execute Command + Speak Response
        ↓
Return to Idle
```

The microphone and recognizer are initialized **once**, which prevents freezes and missed wake words.

---

## 🛠️ Technologies Used

* Python 3
* SpeechRecognition
* PyAudio
* pyttsx3 (Text-to-Speech)
* pywhatkit
* Wikipedia API

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Youssef-Mohammad/Syntecxhub-personal-voice-assistant.git
cd Syntecxhub-personal-voice-assistant
```

### 2️⃣ Create & activate environment (recommended)

```bash
conda create -n voice-assistant python=3.10
conda activate voice-assistant
```

### 3️⃣ Install dependencies

```bash
pip install SpeechRecognition pyttsx3 pyaudio pywhatkit wikipedia
```

> ⚠️ **Windows note**: PyAudio may require a prebuilt wheel.

---

## ▶️ Usage

```bash
python assistant.py
```

Say:

```text
Alexa
```

Then give a command such as:

* "Open YouTube"
* "Search Google for Python voice assistant"
* "What time is it"
* "Play Imagine Dragons"
* "Who is Elon Musk"

---

## 🧪 Example Commands

| Command                 | Action              |
| ----------------------- | ------------------- |
| Alexa                   | Wake assistant      |
| Open YouTube            | Opens YouTube       |
| Search machine learning | Google search       |
| Play song name          | Plays on YouTube    |
| What time is it         | Speaks current time |
| Cancel                  | Cancels command     |
| Exit                    | Stops assistant     |

---

## 🚀 Key Improvements Implemented

* Removed `phrase_time_limit` to allow long speech
* Reused microphone & recognizer to avoid freezes
* Single ambient-noise calibration at startup
* Reliable wake-word loop

---

## 📌 Internship Context

This project was developed as part of my **internship**, focusing on:

* Real-time audio processing
* Voice UX design
* Python automation
* Robust error handling

---

## 🔮 Future Enhancements

* Offline speech recognition (Whisper)
* True wake-word engine (Porcupine)
* GUI dashboard
* NLP-based intent detection
* Background listening thread

---

## 📜 License

This project is for educational and demonstration purposes.

---

## 🙌 Acknowledgments

Special thanks to my internship team for guidance and support throughout this project.
