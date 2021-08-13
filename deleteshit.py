import os, requests
from pyrogram import Client, filters


app = Client(os.environ['session_string'])

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
    def download_file(url):
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter below
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    f.write(chunk)
    return local_filename
    file_name = download_file(message.command[1])
    if file_name.split('.')[-1] == mp4 or file_name.split('.')[-1] == mkv:
        message.reply_video(video=file_name, supports_streaming=True)
    else:
        message.reply_document(file_name)

    
app.run()
