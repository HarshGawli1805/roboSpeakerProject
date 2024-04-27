import win32com.client as wincl

def speak(text):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)

# Take input from the user
while True:
    user_input = input("What u want me to speak?")

# Speak the input
    if user_input == 's':
        break
    speak(user_input)
