#pip3 install gTTS
from gtts import gTTS
import os

class Speech:

    # Constructor
    def __init__(self):
        self.language='fr'

    # Read the sentance and create a file .mp3
    def speakSentence(self,sentence,file):
        myobj = gTTS(text=sentence, lang=self.language, slow=False)
        myobj.save("data/speech/"+file+".mp3")
        os.system("mpg321 speech/"+file+".mp3")
        os.remove("data/speech/"+file+".mp3")
