#creating text into speech.

from gtts import gTTS

text = "ladle meow, ghop ghop ghop"

tts = gTTS(text=text, lang="en")

tts.save("audio.mp3")

print("Audio saved!")
