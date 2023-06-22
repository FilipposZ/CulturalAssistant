
import os
from dataclasses import asdict, dataclass
from typing import Literal

import openai


@dataclass
class ConversationItem:
  role: Literal['system', 'user', 'assistant']
  content: str


class Chatbot:
  def __init__(self, api_key: str | None = None, model_id: str = 'gpt-3.5-turbo'):
    self.api_key = api_key
    self.model_id = model_id
    openai.api_key = os.getenv("OPENAI_API_KEY")

    self.conversation: list[ConversationItem] = []
    
  def generate_response(self, prompt_text: str) -> ConversationItem:
    completion = openai.ChatCompletion.create(
      model=self.model_id,
      messages=[
        {"role": "system", "content": "You are a cultural information assistant."},
        *[asdict(conversationItem) for conversationItem in self.conversation],
        {"role": "user", "content": prompt_text}
      ],
      max_tokens=691
    )
    response: ConversationItem = completion.choices[0].message
    print(response)
    
    self.conversation.append(ConversationItem('user', prompt_text))
    self.conversation.append(ConversationItem(response.role, response.content))
    
    return response