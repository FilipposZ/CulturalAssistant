import os
import time

import openai
import pyttsx3

openai.api_key = os.getenv("OPENAI_API_KEY")

engine = pyttsx3.init()

#openai response
def openai(text): 
   def generate_response(prompt):
      response = openai.Completion.create(
        engine='text-ada-001',
        prompt=text,
        max_tokens=691,
        temperature=1,
        n=1,
        stop=None,
        log_level='info',
        logprobs=None,
        echo=True
    )
      return response['choices'][0]['text']
   return generate_response(text)

# Response audio
def speak_text(text):
    engine.setProperty('voice', 'english+f3')
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# Main
def main():
    while True:
        #Introduce
        print("Greetings, my name is Hera, i'm an enthousiast about Culture and History, how may i assist you?")
        speak_text("Greetings, my name is Hera, i'm an enthousiast about Culture and History, how may i assist you?")
        
        #User input
        user_input = input("Εισάγετε το κείμενο σας: ")

        #Openai response
        response = openai.Completion.create
        print(response)
        speak_text(response)

if __name__ == '__main__':
  main()