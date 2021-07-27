import os
from pyrogram import Client, filters

app = Client("my_session", api_id=os.environ['api_id'], api_hash=os.environ['api_hash'])

guessmessage = None
waifumessage = None

@app.on_message(filters.chat('animeryu') & filters.user(1382346231))
async def delete_animebot_shit(client, message):
    if message.photo:
        global guessmessage
        guessmessage = message

    elif message.text == 'That\'s not right!!!' or message.text == 'Eww small pp and small guesses are not allowed!!!' or message.text == 'Already Guessing!!!' or 'Oops you ran out of time...' in message.text:
        await message.reply_to_message.delete()
        await message.delete()
    
    elif 'Not guessing anything right now' in message.text:
        await message.delete()
    
    elif 'UwU you got that right!!!' in message.text:
        await message.reply_to_message.delete()
        await message.delete()
        await guessmessage.delete()

@app.on_message(filters.chat('animeryu') & filters.user(792028928))
async def delete_waufubot_shit(client, message):
    if message.photo:
        global waifumessage
        waifumessage = message
    elif message.text == 'rip, that\'s not quite right...':
        await message.reply_to_message.delete()
        await message.delete()
    elif 'This waifu has been added to your harem.' in message.text:
        await message.reply_to_message.delete()
        await waifumessage.delete()
    
app.run()
