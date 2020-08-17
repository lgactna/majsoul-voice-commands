
# Python program to translate 
# speech to text and text to speech 
  
import speech_recognition as sr 

r = sr.Recognizer()  

while True:
    try:
        with sr.Microphone() as source:
            print("Say something!")
            #normally this should return once the energy threshhold drops below a certain level
            audio = r.listen(source,phrase_time_limit=4)

            MyText = r.recognize_google(audio) 
            MyText = MyText.lower() 

            MyText2 = r.recognize_google(audio, language="ja") 
            MyText3 = r.recognize_google(audio, language="zh-CN")

            print("EN: "+MyText) 
            print("JA: "+MyText2)
            print("CN: "+MyText3) 
    except sr.UnknownValueError: #unintelligible/nothing
        print("got nothing")
        continue

'''
import pyttsx3  
  
# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init("sapi5", True) 
    engine.say(command)  
    engine.runAndWait() 
      
      
# Loop infinitely for user to 
# speak 
  
while(1):     
      
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
        print("a")
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
            print("b")  
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.2) 
            r.dynamic_energy_threshold = True
              
            print("e")
            #listens for the user's input  
            audio2 = r.listen(source2)
            print("c") 
              
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
  
            print("Did you say "+MyText) 
            SpeakText(MyText) 
              
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured") 
'''
