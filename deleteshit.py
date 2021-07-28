import os
from pyrogram import Client, filters

app = Client("my_session", api_id=os.environ['api_id'], api_hash=os.environ['api_hash'])

chat_id = ['1425336751']



guessmessage = None

@app.on_message(filters.chat(chat_id) & filters.user(1382346231))
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
        
@app.on_message(filters.chat(chat_id) & filters.user(1382346231) & filters.regex(pattern='^Thank.*Thanks..$'))
async def delete_animebot_startmessage(client, message):
    message.delete()

@app.on_message(filters.chat(chat_id) & filters.user(1382346231) & filters.regex(pattern='^Join.*sumit$'))
async def delete_animebot2_startmessage(client, message):
    message.delete()


@app.on_message(filters.chat(chat_id) & filters.user(778490365) & filters.regex(pattern='^Hello.*[\u263a-\U0001f645]$'))
async def delete_nepgear_startmessage(client, message):
    message.delete()


@app.on_message(filters.chat(chat_id) & filters.user(1416903424) & filters.regex(pattern='^Ara.*s$'))
async def delete_akeno_startmessage(client, message):
    if 'Ping' in message.reply_markup.InlineKeyboardButton.text:
        message.delete()
 

@app.on_message(filters.chat(chat_id) & filters.user(1031952739) & filters.regex(pattern='^Hello.*me$'))
async def delete_quotly_startmessage(client, message):
    message.delete()

@app.on_message(filters.chat(chat_id) & filters.user(1885165230) & filters.regex(pattern='^Im.*s$'))
async def delete_ohto_startmessage(client, message):
    message.delete()
    
    


    
    
    
app.run()
