# ChatGPT Voice Assistant

Ein einfacher ChatGPT-Sprachassistent, der die OpenAI-API und Gradio verwendet, um eine Benutzeroberfläche bereitzustellen, auf der Benutzer ihre Fragen aufzeichnen und gesprochene Antworten erhalten können.

## Voraussetzungen

- Python 3.6 oder höher
- OpenAI    
- Gradio  
- Pyttsx3  
- Soundfile  
- FFmpeg


### Installation

### 1. Klone das Repository:

   ```bash
   git clone https://github.com/your-github-username/chatgpt-voice-assistant.git
   ```
### 2. Wechseln Sie in das Verzeichnis:

   ```bash
   cd chatgpt-voice-assistant
   ```

### 3. Erstellen Sie eine virtuelle Umgebung:

   ```bash
   python3 -m venv venv
   ```
### 4. Aktivieren Sie die virtuelle Umgebung:
 - #### MacOS: 
   ```bash
   source venv/bin/activate
    ```
 - #### Windows:
   ```bash
   .\venv\Scripts\activate
   ```
### 5. Installieren Sie die Abhängigkeiten:

   ```bash
   pip install -r requirements.txt
   ```
### 6. OpenAI-API-Schlüssel zur config.py hinzufügen:
Falls noch nicht getan, bitte eine config.py-Datei im Projektordner erstellen und den OpenAI-API-Schlüssel hinzufügen den Sie aus dem [OpenAI Dashboard](https://platform.openai.com/account/api-keys) erhalten haben:
```bash
OPENAI_API_KEY = "your_openai_api_key_here"
```
Ersetzen Sie your_openai_api_key_here durch Ihren tatsächlichen API-Schlüssel.

## FFmpeg installieren
- #### Für Windows:

Laden Sie die FFmpeg-Binärdateien von der offiziellen Website herunter: [FFmpeg Download-Seite](https://ffmpeg.org/download.html)
Extrahieren Sie die heruntergeladenen Dateien und fügen Sie den extrahierten Ordner, der die FFmpeg-Exe-Dateien enthält (normalerweise bin), zur PATH-Umgebungsvariablen hinzu. Eine Anleitung dazu finden Sie hier: [FFmpeg unter Windows installieren](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)

- #### Für MacOS:
```bash
brew install ffmpeg
```

- #### Für Linux:
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

## Ausführung
Starten Sie den ChatGPT-Sprachassistenten, indem Sie das Hauptskript ausführen:
```bash
python assistant.py
```

   Öffnen Sie Ihren Webbrowser und navigieren Sie zur angezeigten URL (normalerweise http://localhost:7860/), um die Benutzeroberfläche des Sprachassistenten zu verwenden.
   
## Autor
Autor: Martin Haferanke - 
Ursprüngliche Version von: [Hacking the Markets](https://github.com/hackingthemarkets/)
