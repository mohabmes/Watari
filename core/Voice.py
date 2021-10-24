import pyttsx3
import os.path
from gtts import gTTS
from core.Utils import *
from mpyg321.mpyg321 import MPyg321Player


class Voice:
    def __init__(self):
        if is_win():
            self.engine = VoiceWin()
        elif is_linux():
            self.engine = VoiceLinux()
        else:
            self.engine = VoiceNotSupported()

    def say(self, speech):
        self.engine.say(speech)


class VoiceWin:
    def __init__(self, rate=100):
        self.rate = rate

    def say(self, speech):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', self.rate)
        self.engine.say(speech)
        self.engine.runAndWait()


class VoiceLinux:

    MAIN_DIR = "data/audio"

    def savefile(self, filename):
        self.engine.save(filename)

    def play(self, filepath):
        player = MPyg321Player()
        player.play_song(filepath)

    def say(self, speech):
        filename = cleanStr(speech)
        filepath = "{}/{}.mp3".format(self.MAIN_DIR, cleanStr(filename))

        if os.path.isfile(filepath):
            self.play(filepath)
        else:
            self.engine = gTTS(text=speech, lang='en-uk', slow=False)
            self.savefile(filepath)
            self.play(filepath)


class VoiceNotSupported:
    def __init__(self):
        self.warning_print = False

    def say(self, speech):
        print("Speech not supported! Please install pyttsx3 or mpyg321 text-to-speech engine")
