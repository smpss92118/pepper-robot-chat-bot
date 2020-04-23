import os
import dialogflow
import requests
import json
import operator as op


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

        f = open("output.txt","w+")
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
  #  print (message)   

if __name__ == "__main__":
    #while(say()):
     #   send_message(ME)

    cur = "difault"
    while(True):
        fin = open("input.txt","r+")
        ME = fin.read()
        if(op.eq(ME,cur)):
            if(op.eq("quit\n",cur)):
                fin.close()
                ff = open("input.txt","w+")
                ff.write("掰掰\n")
                ff.close()
                break
#            print ("ME=sur")
            fin.close()
        else:
 #           print (cur)
            cur = ME
            send_message(ME)
        fin.close()

