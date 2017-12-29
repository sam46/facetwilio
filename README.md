# FaceTwilio

## Chat with your facebook friends using regular SMS texting.

You need a [twilio](https://www.twilio.com) account/phone number. <br/>
You need an [ngrok](https://ngrok.com) account.

## Setting up:
- clone this repo
- pip install requirments.txt
- create your twilio and ngrok accounts
- execute: ngrok http 5000 <br/>
  (or use a different port, but you'll have to change it in [twilio2fb.py](https://github.com/sam46/facetwilio/blob/master/twilio2fb.py) too)
- Go to your twilio phone number settings, copy **ngrok_https_url/sms** into the 'A MESSAGE COMES IN' webhook field <br/> ('ngrok_https_url' is the https url that ngrok generated in previous step)
- go to [creds.py](https://github.com/sam46/facetwilio/blob/master/creds.py) and fill in your facebook and twilio information
- run: python main.py

## Usage:
To send the message 'Hello Jane' to facebook contact 'Jane Doe', text "Jane Doe: Hello Jane" to your twilio phone number


