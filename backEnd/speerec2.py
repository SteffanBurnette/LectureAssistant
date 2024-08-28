import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# List to store recognized text
captured_text = []

try:
    while True:
        with sr.Microphone() as source:
            print("Listening... Press Ctrl+C to stop and output the captured text.")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            text = r.recognize_google(audio, language="en")
            print(f"Recognized: {text}")
            captured_text.append(text)
        
        except sr.UnknownValueError:
            print("Could not understand the audio, please try again.")
        except sr.RequestError as e:
            print(f"Request error from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred during recognition: {e}")

except KeyboardInterrupt:
    print("\nStopped listening. Here is what was captured:")
    if captured_text:
        full_text = " ".join(captured_text)
        print(full_text)

        # Save the captured text to a file
        with open("captured_text.txt", "w") as file:
            file.write(full_text)
        print("Captured text saved to captured_text.txt")
    else:
        print("No text was captured.")

# Additional debug information
print(f"Captured text list: {captured_text}")
