import os, requests, youtube_dl
from pyrogram import Client, filters


app = Client(os.environ['session_string'], api_id=os.environ['api_id'], api_hash=os.environ['api_hash'])

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
    url = message.command[1]
    ydl_opts = {'outtmpl': 'video.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir():
        if 'video' in file: filename = file


    if filename.split('.')[-1] in ['mp4', 'mkv']:
        message.reply_video(video= os.path.abspath(filename))
    else: message.reply_document(os.path.abspath(filename))

    os.remove(os.path.abspath(filename))



    
app.run()
