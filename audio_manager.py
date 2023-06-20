import pyttsx3


class AudioManager:
  """The AudioManager class handles all the audio related operations.

  It is responsible for managing the text-to-speech voice.
  """
  def __init__(self):
    self.engine = pyttsx3.init()
    self.available_voices = self.engine.getProperty('voices')
  
    self.engine.setProperty('voice', self.available_voices[0].id)
    self.engine.setProperty('rate', 125)
    self.engine.setProperty('volume', 1.0)
    
  def speak(self, text: str):
    """The main function of the audio manager. A voice speaks the given :attr:`text`."""
    print(f"Speaking the text: {text}")    
    self.engine.say(text)
    self.engine.runAndWait()
  
  @property
  def voice(self) -> str:
    """The selected voice of the text-to-speech engine."""
    return self.engine.getProperty('voice')
  
  @voice.setter
  def voice(self, voice: str):
    self.engine.setProperty('voice', voice)
    
  @property
  def rate(self) -> int:
    """The speed of the voice of the engine."""
    return self.engine.getProperty('rate')
  
  @rate.setter
  def rate(self, rate: int):
    self.engine.setProperty('rate', rate)
    
  @property
  def volume(self) -> float:
    """The volume of the voice. It can be between 0 and 1."""
    return self.engine.getProperty('volume')
  
  @volume.setter
  def volume(self, volume: float):
    self.engine.setProperty('volume', volume)