# Multilingual Speech Translator

This repository contains a Python script for a multilingual speech translator. It utilizes the Google Cloud Translate API, SpeechRecognition library, Google Text-to-Speech (gTTS) library, and playsound library to convert spoken input in one language to text, translate it to another language, and then convert it back to speech.

## Features
- Speech recognition: Converts spoken input into text.
- Translation: Translates the recognized text into the desired language using Google Translate.
- Text-to-speech: Converts the translated text into speech using gTTS.
- Playback: Plays the translated speech.

## Dependencies
- `googletrans`: Python library for Google Translate API.
- `speech_recognition`: Library for performing speech recognition.
- `gtts`: Google Text-to-Speech library for converting text to speech.
- `playsound`: Library for playing audio files.

## Usage
1. Ensure you have installed all the dependencies mentioned above.
2. Run the Python script.
3. Speak into the microphone when prompted.
4. The script will recognize your speech, translate it to the desired language, convert it back to speech, and play the translated speech.

## Configuration
- Ensure that you have a stable internet connection to access the Google Cloud Translate API.
- You may need to set up credentials for accessing the Google Cloud Translate API if you haven't already done so.

## Contributing
Contributions are welcome! If you find any bugs, want to improve the codebase, or add new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
