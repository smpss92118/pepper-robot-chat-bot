import os
import dialogflow
import requests
import json

import speech_recognition as sr
def say():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...") 
        r.adjust_for_ambient_noise(source, duration=0.5) 
        print("Say something!")
        audio=r.listen(source)

    try:
        #print("Google Speech Recognition thinks you said:")
        #print(r.recognize_google(audio, language="zh-TW"))
        global ME
        ME = r.recognize_google(audio,language = "zh-TW")
        return r.recognize_google(audio,language = "zh-TW")
#        f = open("input.txt","a")
 #       f.write(r.recognize_google(audio, language="zh-TW"))
  #      f.close()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return False
    except sr.RequestError as e:
        print("No response from Google Speech Recognition service: {0}".format(e))
        return False


PUSHER_APP_ID='774119'
PUSHER_KEY='9916cc0968cbae03f8f2'
PUSHER_SECRET='467c96d7a82208cc7daa'
PUSHER_CLUSTER='ap3'

GOOGLE_APPLICATION_CREDENTIALS='Movie-Bot-73d554d004ef.json'
DIALOGFLOW_PROJECT_ID='movie-bot-b52dc'
OMDB_API_KEY='85c75ded'

# initialize Pusher
"""
pusher_client = pusher.Pusher(
    app_id=os.getenv('PUSHER_APP_ID'),
    key=os.getenv('PUSHER_KEY'),
    secret=os.getenv('PUSHER_SECRET'),
    cluster=os.getenv('PUSHER_CLUSTER'),
    ssl=True)
"""
def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)

        f = open("input.txt","w+")
        f.write(response.query_result.fulfillment_text)
        f.write('\n')
        f.close()
        print (response.query_result.fulfillment_text)
        
        return response.query_result.fulfillment_text

def send_message(SS):
    #message = request.form['message']
    #message = input("input:")
    #message = say()
    message = SS
   # project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    project_id = DIALOGFLOW_PROJECT_ID
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    response_text = { "message":  fulfillment_text }
   # print (message)   

if __name__ == "__main__":
    #while(say()):
     #   send_message(ME)

    while(True):
       # while((say())==False):
        #    continue
        sel = input("Please input something:\n")
        send_message(sel)
