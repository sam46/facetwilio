import creds
import threading
from fbchat import Client
from fbchat.models import *
from twilio.rest import Client as TwilioClient


def forwardMsg(msg):
    tclient.messages.create(
        to=creds.twilio['phone'],
        from_=creds.twilio['twilio_phone'],
        body=str(msg)
    )

class CustomClient(Client):
    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        author = self.fetchUserInfo(author_id).values()[0]
        # print 'new msg from ({:s}):'.format(author.name), msg['delta']['body']
        thr = threading.Thread(target=forwardMsg, args=['\n{:s}: '.format(author.name)+ msg['delta']['body']])
        thr.start()

# if __name__ == '__main__':
#     tclient = TwilioClient(creds.twilio['sid'], creds.twilio['auth'])
#     fclient = CustomClient(creds.fb['email'], creds.fb['pwd'])
#     fclient.listen()


tclient = TwilioClient(creds.twilio['sid'], creds.twilio['auth'])
fclient = CustomClient(creds.fb['email'], creds.fb['pwd'])
def run():
    fclient.listen()
