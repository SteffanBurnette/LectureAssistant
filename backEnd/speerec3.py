import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()
    
# File to store recognized text
file_name = "lab_text.txt"

while True:
    # Use the default system microphone as the audio source
    with sr.Microphone() as source:
        print("Please say something:")
        # Adjust for ambient noise and record the audio
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        text = r.recognize_google(audio, language="en")
        print("You said:", text)

        # Append recognized text to the file
        with open(file_name, "a") as file:
            file.write(text + "\n")

        

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")