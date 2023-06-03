import streamlit as st
import pyaudio
import speech_recognition as sr

def main():
    st.title("Real-time Voice Transcription")

    # Create a button to start/stop the transcription
    if st.button("Start Transcription"):
        # Initialize the speech recognizer
        r = sr.Recognizer()
        r.energy_threshold = 4000

        # Start listening to the microphone
        with sr.Microphone() as source:
            st.write("Listening...")

            # Continuously listen and transcribe the speech
            while True:
                audio = r.listen(source)
                try:
                    # Perform speech recognition
                    text = r.recognize_google(audio)
                    st.write(f"Transcription: {text}")
                except sr.UnknownValueError:
                    st.write("Could not understand audio")
                except sr.RequestError as e:
                    st.write(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
