from telethon.sessions import StringSession  # Function if you want to use session string
from telethon.sync import TelegramClient, events
import re

api_id = 28544780
api_hash = '5aef989ade807dad172f2ab4a808cc2e'
your_session = 'tg.session'

client = TelegramClient(your_session, api_id, api_hash)
# client = TelegramClient(StringSession(your_session), api_id, api_hash) # Use this if you want to use session string

@client.on(events.NewMessage(from_users=777000))
async def handle_incoming_message(event):
    # Extract OTP from the message using regular expression
    otp = re.search(r'\b(\d{5})\b', event.raw_text)  # Исправлено: \a на \d для поиска цифр
    if otp:
        print("Your login code:", otp.group(1))  # Исправлен отступ и group(0) на group(1)

print("Listening for messages...")

with client:
    client.run_until_disconnected()
