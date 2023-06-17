import os
import random

import openai
import pyttsx3

openai.api_key = os.getenv("OPENAI_API_KEY")

#Modeil list
# print(openai.Model.list())
model_id = 'gpt-3.5-turbo'

#gTTS engine
tts_engine = pyttsx3.init()
greetings = "Greetings, my name is Iris, i'm an enthousiast about Culture and History, how may i assist you?"


#ChatGpt_Conversation
def generate_response(prompt_text):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a cultural information assistant."},
      {"role": "user", "content": prompt_text}
    ],
    max_tokens=691
  )
  print(completion.choices[0].message)
  return completion.choices[0].message

    


#openai response
# def openai(text): 
#    def generate_response(prompt_text):
#       response = openai.Completion.create(
#         engine='text-davinci-003',
#         prompt=messages,
#         echo=True
#     )
#       return response['choices'][0]['text']
#    return generate_response(text)


# Response audio
def speak_text(text):
    tts_engine.setProperty('voice', os.getenv("DEFAULT_VOICE"))
    tts_engine.setProperty('rate', 150)
    tts_engine.say(text)
    tts_engine.runAndWait()


# Main
def main():
    while True:
        #Introduce
        print(greetings)
        speak_text(greetings)
        
        #User input
        user_input = input("Εισάγετε το κείμενο σας: ")

        #Openai response
        response = generate_response(user_input)
        print(response)
        speak_text(response)

if __name__ == '__main__': 
  main()