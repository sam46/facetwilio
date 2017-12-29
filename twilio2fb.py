import creds
import threading
from fbchat import Client
from fbchat.models import *
from flask import Flask, request, redirect
# from twilio.twiml.messaging_response import MessagingResponse

port = 5000
app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def smsHandler():
    try:
        if request.form['From'] == creds.twilio['phone']:
            sms = request.form['Body'].split(':')
            name, msg = sms[0], ''.join(sms[1:])
            user = fclient.searchForUsers(name)[0]
            fclient.send(Message(text=msg), thread_id=user.uid, thread_type=ThreadType.USER)
    except:
        print 'exception @ smsHandler!'
    # resp = MessagingResponse()
    # resp.message('msg123')
    # print str(resp)
    return ''
    
# if __name__ == '__main__':
#     fclient = Client(creds.fb['email'], creds.fb['pwd'])
#     app.run(debug=True)

fclient = Client(creds.fb['email'], creds.fb['pwd'])
def run():
    app.run(debug=False, port=port)
