from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say
from app.config import settings

class TwilioClient():
    def __init__(self):
        self._client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
        self._from_number = settings.twilio_phone_number
        
    def send_sms(self, to: str, body: str) -> str:
        message = self._client.messages.create(body=body, from_=self._from_number, to=to)
        return message.sid
    
    def make_voice_call(self, to: str, message: str) -> str:
        response = VoiceResponse()
        response.say(message, voice="alice", language="pt-PT")
        response.say(message, voice="alice", language="pt-PT")
        call = self._client.calls.create(twiml=str(response), from_=self._from_number, to=to)
        return call.sid