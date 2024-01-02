!pip install pysentimiento
from pysentimiento import create_analyzer
emotion=create_analyzer(task='emotion',lang='en')
result = emotion.predict('i am scared of dogs') # if only this line, it will give probability as well of all emotions
result.output   #only for correct output (strongest emotion)
def emotion_detection(text):
  emotion=create_analyzer(task='emotion',lang='en')
  result = emotion.predict(text) # if only this line, it will give probability as well of all emotions
  return result.output   #only for correct output (strongest emotion)

hatespeech= create_analyzer(task='hate_speech', lang='en')
result= hatespeech.predict('I love apples')
next(iter(result.probas.items()))
def hatespeech_detection(text):
  hatespeech = create_analyzer(task='hate_speech', lang='en')
  result = hatespeech.predict(text)
  return next(iter(result.probas.items()))

text="Overwhelmed with joy, she embraced the unexpected success, tears of happiness streaming down her face, creating a cherished moment."
emo= emotion_detection(text)
hate= hatespeech_detection(text)

print('emotion:',emo)
print('hatespeech:',hate)
