import os
import random
import re

import openai
import pyttsx3

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


class AudioManager:
  def __init__(self):
    self.engine = pyttsx3.init()
    self.engine.setProperty('rate', 150)
    self.rate = self.engine.getProperty('rate')
    self.count_uses = 0
    self.available_voices = self.engine.getProperty('voices')
    
  @property
  def volume(self):
    self.volume = self.engine.setProperty('volume', 0)
    
  @volume.setter
  def volume(self, value = 1):
    self.engine.setProperty('volume', value)
    self._volume = self.engine.getProperty('volume')
    
  @property 
  def voice(self):
    return self._voice
    
  @voice.setter
  def voice(self, voiceid):
    self.engine.setProperty('voice', voiceid)
    self._voice = self.engine.getProperty('voice')
  
  def speak(self, text):
    print(f"Speaking text: {text}")
    self.voice = self.available_voices[self.count_uses % len(self.available_voices)].id
    self.count_uses += 1
    
    self.engine.say(text)
    self.engine.runAndWait()

# Main
def main():
  audioManager = AudioManager()
  
  while True:
    #Introduce
    print(greetings)
    
    audioManager.speak(re.split('\. |, ', greetings))
    
    #User input
    user_input = input("Εισάγετε το κείμενο σας: ")

    #Openai response
    response = generate_response(user_input)
    audioManager.speak(response)

if __name__ == '__main__':
  main()