import  speech_recognition as sr

#Initialize recognizer
recognizer = sr.Recognizer()

#Function to recognize speech
def recognize_speech():
   #use the microphone as source for input
   with sr.Microphone() as source: 
      print("Please say something:")
      #adjust the recognizer sensitivity to ambient noise and record audio
      recognizer.adjust_for_ambient_noise(source)
      audio = recognizer.listen(source)

      try:
         #Recognize speech using Google Web Speech APT
         text = recognizer.recognize_google(audio)
         print("You said: " + text)
      except sr.UnknownValueError:
         print("Sorry, I could not understand the audio.")
      except sr.RequestError:
         print("Sorry, the speech recognition service is not available")

#call the function
recognize_speech()
