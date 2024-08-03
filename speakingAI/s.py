from gtts import gTTS
s = input("Enter the file name: ")
f = open(s)
text = f.read()
obj = gTTS( text = text, lang= 'en' ,slow= False)
f1 = input("Enter the audio name to be saved: ")
obj.save(f1)