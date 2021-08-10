import os, wget
from pyrogram import Client, filters


app = Client("my_session", api_id=os.environ['api_id'], api_hash=os.environ['api_hash'])

guessmessage = None

@app.on_message(filters.chat('animeryu') & filters.user(1382346231))
async def delete_animebot_shit(client, message):
    if message.photo:
        global guessmessage
        guessmessage = message

    elif message.text == 'That\'s not right!!!' or message.text == 'Eww small pp and small guesses are not allowed!!!' or message.text == 'Already Guessing!!!' or 'Oops you ran out of time...' in message.text:
        await message.delete()
    
    elif 'Not guessing anything right now' in message.text:
        await message.delete()
    
    elif 'UwU you got that right!!!' in message.text:
        await message.delete()
        await guessmessage.delete()
        
@app.on_message(filters.chat('animeryu'))
async def delete_random_shit(client, message):
    if message.text.lower() == '/guess' or message.text.lower() == '/guess@any_animebot':
        await message.delete()
    
    elif message.text[:4].lower() == '/uwu':
        await message.delete()
    
    elif 'nigga' in message.text.lower() or 'nigger'.lower() in message.text.lower() or 'nibba' in message.text.lower() or 'nigha' in message.text.lower():
        await message.delete()
        
@app.on_message(filters.command('download', prefixes='?') & filters.chat('animeryu'))
async def download_url(client, message):
    file_name = wget.download(message.command[1])
    if file_name.split('.')[-1] == mp4 or file_name.split('.')[-1] == mkv:
        message.reply_video(video=file_name, supports_streaming=True)
    else:
        message.reply_document(file_name)

    
app.run()
