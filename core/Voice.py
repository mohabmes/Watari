import os
import os.path
import logging
from gtts import gTTS
from core.Utils import *

class Voice:

    MAIN_DIR = "data/audio"

    def setStr(self, text):
        self.text = text

    def getStr(self, text):
        return self.text

    def savefile(self, filename):
        self.engine.save(filename)

    def play(self, filepath):
        os.system("mpg321 -q {}".format(filepath))

    def say(self, text):
        try:

            self.setStr(text)
            filename = cleanStr(self.text)
            filepath = "{}/{}.mp3".format(self.MAIN_DIR, cleanStr(filename))

            if os.path.isfile(filepath):
                self.play(filepath)
            else:
                self.engine = gTTS(text=self.text, lang='en-uk', slow=False)
                self.savefile(filepath)
                self.play(filepath)

        except Exception as e:
            display_error(e)
