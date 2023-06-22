import pyttsx3


class AudioManager:
  """The AudioManager class handles all the audio related operations.

  It is responsible for managing the text-to-speech voice.
  """
  
  def __init__(self, voice: int = 0, rate: int = 125, volume: float = 1):
    self.engine = pyttsx3.init()
    self.available_voices = self.engine.getProperty('voices')
  
    self.voice = self.available_voices[voice].id
    self.rate = rate
    self.volume = volume
    
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
  def voice(self, voiceid: str):    
    self.engine.setProperty('voice', voiceid)
    
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