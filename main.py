from dotenv import load_dotenv

from audio_manager import AudioManager
from chatbot import Chatbot

load_dotenv()

# The ID of the OpenAI model
model_id = 'gpt-3.5-turbo'

# print(openai.Model.list()) # list all available models

# The greetings message
greetings = "Greetings, my name is Iris, i'm an enthousiast about Culture and History, how may i assist you?"

# Main
def main():
  """The main function runs the main loop of the program.
  
  The Narrator greets the user and asks him for a prompt.
  The Narrator answers with a generated voice.
  On every subsequent prompt the conversation is remembered.
  """
  audioManager = AudioManager()
  chatbot = Chatbot()
   
  audioManager.speak(greetings)
  
  while True:
    user_input = input("Enter your text: ")
    
    response = chatbot.generate_response(user_input)
    audioManager.speak(response.content)


if __name__ == '__main__':
  main()