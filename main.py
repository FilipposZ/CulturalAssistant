import os
import random

import openai
import pyttsx3

openai.api_key = os.getenv("OPENAI_API_KEY")

tts_engine = pyttsx3.init()
greetings = [
  "Haaaa you suckuaaa",
  "Greetings, my name is Hera, i'm an enthousiast about Culture and History, how may i assist you?"
]

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
    tts_engine.setProperty('voice', os.getenv("DEFAULT_VOICE"))
    tts_engine.setProperty('rate', 150)
    tts_engine.say(text)
    tts_engine.runAndWait()

def choose_random_greeting():
  random_indx = random.randint(0, len(greetings))
  return greetings[random_indx]

# Main
def main():
    while True:
        #Introduce
        greeting = choose_random_greeting()
        print(greeting)
        speak_text(greeting)
        
        #User input
        user_input = input("Εισάγετε το κείμενο σας: ")

        #Openai response
        response = openai.Completion.create
        print(response)
        speak_text(response)

if __name__ == '__main__':
  main()