#importing library gtts
from gtts import gTTS
language = "en"                                             #selecting language
text = "hey there! i am ayesha javed. Welcome all of you!"  #defining text
speech = gTTS(text = text, lang = language)                  
speech.save("lan.mp3")                                      #saving the speech as a mp3 file

#after running a file will be created saving the mp3 file of the speech
