import time, os, requests, youtube_dl
from pyrogram import Client, filters
from pyrogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = Client(os.environ['session_string'], api_id=os.environ['api_id'], api_hash=os.environ['api_hash']
)

#For channel
async def job():
    #For the submissions with with news flair
    response = requests.get('https://www.reddit.com/r/anime/search/.json?q=flair_name%3A%22News%22&restrict_sr=1&sort=new&limit=5', headers={'User-Agent': 'r/animenews update v1'}).json()
    titles = []
    urls = []
    comment_bodys = []

    #Append values in the newly created lists
    for submission in response['data']['children']:
        #First checking if the post is already posted in telegram channel. If posted, continue to the next iteration.
        message_history = await app.get_history('AnimeNewsMedia', limit=20)
        if not message_history:
            message_history = ['']
        for message in message_history:
            if message.media:
                if submission['data']['url'] in message.caption_entities: continue
            else:
                if submission['data']['url'] in message.entities: continue

        #Ignore submisioons if they're not older than 3 minutes
        if int(time.time()) - submission['data']['created_utc'] < 180: continue 

        #Finally append values
        titles.append(submission['data']['title'])
        urls.append(submission['data']['url'])
        #For comment bodys
        response = requests.get('https://reddit.com'+submission['data']['permalink']+'.json', headers={'User-Agent': 'animenewsmediamyagent'}).json()
        for comment in response[1]['data']['children']:
            if comment['data']['is_submitter']:
                comment_bodys.append(comment['data']['body'])
                break
        if len(titles) != len(comment_bodys): comment_bodys.append(submission['data']['selftext'])
        
        time.sleep(2)

    #Post the Messages in channel
    for title, url, comment_body in zip(titles, urls, comment_bodys):
        await app.send_message(
            'AnimeNewsMedia',
            f'#News\n\n**{title}**\n\n[<a href="{url}">Source</a>]\n{comment_body}',
            disable_notification=True
        )
    


    #For the submissions with official media flair
    response = requests.get('https://www.reddit.com/r/anime/search/.json?q=flair_name%3A%22Official%20Media%22&restrict_sr=1&sort=new&limit=5', headers={'User-Agent': 'r/animenews update v1'}).json()
    titles = []
    urls = []
    comment_bodys = []

    #Append values in the newly created lists
    for submission in response['data']['children']:
        #First checking if the post is already posted in telegram channel. If posted, continue to the next iteration.
        for message in message_history:
            if submission['data']['url'] in message.caption_entities: continue
        
        #Ignore submisioons if they're not older than 3 minutes
        if int(time.time()) - submission['data']['created_utc'] < 180: continue

        #Finally append values
        titles.append(submission['data']['title'])
        urls.append(submission['data']['url'])
        #For comment bodys
        response = requests.get('https://reddit.com'+submission['data']['permalink']+'.json', headers={'User-Agent': 'animenewsmediamyagent'}).json()
        for comment in response[1]['data']['children']:
            if comment['data']['is_submitter']:
                comment_bodys.append(comment['data']['body'])
                break
        if len(titles) != len(comment_bodys): comment_bodys.append(submission['data']['selftext'])
        
        time.sleep(2)

    #Post the Messages in channel
    for title, url, comment_body in zip(titles, urls, comment_bodys):
        #Downloading Media
        ydl_opts = {'outtmpl': 'video.%(ext)s'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl: ydl.download([url])
        #Get the filename of downloadeed media
        for file in os.listdir():
            if 'video' in file: filename = file

        #Finally Post message
        if filename.split('.')[-1].lower() in ['mp4', 'mkv']:
            await app.send_video(
                'AnimeNewsMedia',
                video=os.path.abspath(filename),
                caption=f'#Official_Media\n\n**{title}**\n\n[<a href="{url}">PV/Visual</a>]\n{comment_body}',
                disable_notification=True
            )
        elif filename.split('.')[-1].lower() in ['jpg', 'png', 'jpeg']:
            await app.send_photo(
                'AnimeNewsMedia',
                photo=os.path.abspath(filename),
                caption=f'#Official_Media\n\n**{title}**\n\n[<a href="{url}">PV/Visual</a>]\n{comment_body}',
                disable_notification=True
            )
        else:
            await app.send_document(
                'AnimeNewsMedia',
                document=os.path.abspath(filename),
                caption=f'#Official_Media\n\n**{title}**\n\n[<a href="{url}">PV/Visual</a>]\n{comment_body}',
                disable_notification=True
            )
        os.remove(os.path.abspath(filename))

'''
#For deleting botspam in group
guessmessage = None
botspam_triggers = [
    'That\'s not right!!!',
    'Eww small pp and small guesses are not allowed!!!',
    'Already Guessing!!!',
    'Not guessing anything right now',
    'I can help you find everything about anime.',
    'I will create quotes in the group using the /q command in response to message',
    'Thank you for using Animebot. Check this video out or use /help to get to know various commands.'
]
userspam_triggers = [
    '/uwu',
    '/guess',
    '/start',
    'nigga',
    'nigger',
    'nigha',
    'nibba'
]
@app.on_message(filters.chat(-1001425336751))
async def deleteshit(client: Client, message: Message):
    if message.from_user.is_bot:
        global botspam_triggers
        for trigger in botspam_triggers:
            if trigger in message.text: await message.delete(); await message.reply_to_message.delete()
            elif trigger in message.caption: await message.delete(); await message.reply_to_message.delete()
        
        if 'Type /uwu and name to guess' in message.caption:
            global guessmessage
            guessmessage = message
        elif 'UwU you got that right!!!' in message.text or 'Oops you ran out of time...' in message.text:
            await message.delete()
            await guessmessage.delete()
    else:
        global userspam_triggers
        for trigger in userspam_triggers:
            if trigger.lower() in message.text: await message.delete()
'''


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=300)

scheduler.start()

app.run()



