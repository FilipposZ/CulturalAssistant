import os

import openai

from audio_manager import AudioManager

openai.api_key = os.getenv("OPENAI_API_KEY")

#Modeil list
# print(openai.Model.list())
model_id = 'gpt-3.5-turbo'

#gTTS engine
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




# Main
def main():
  audioManager = AudioManager()

  while True:
    #Introduce
    print(greetings)
    
    audioManager.speak(greetings)
    
    #User input
    user_input = input("Εισάγετε το κείμενο σας: ")

    #Openai response
    response = generate_response(user_input)
    audioManager.speak(response)

if __name__ == '__main__':
  main()