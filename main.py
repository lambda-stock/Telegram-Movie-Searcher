from pyrogram import Client, filters
import asyncio
from time import time
import time
import os
import requests
import random

bot_token = os.environ['BOT_TOKEN']
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
tmdb_api_key = os.environ['TMDB_API_KEY']
tmdb_lang = os.environ['TMDB_LANG']


app = Client(
	"LambdaBot",
	bot_token=bot_token,
	api_id=api_id,
	api_hash=api_hash
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, f"""**Welcome** @{message.from_user.username}.
**Group**: ```{message.chat.title}```
**Invite Link**:  ```t.me/{message.chat.username}```
**User ID**: ```{message.from_user.id}```
**Github Repo**: [Click to go.](https://github.com/lambda-stock/Telegram-Movie-Searcher)
""")

@app.on_message(filters.command("movie"))
async def movie(client, message):
    try:
	    movieinput_withcmd = message.text
	    movieinput = movieinput_withcmd.replace("/movie ", "")
	    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={movieinput}&language={tmdb_lang}')
	    movie_json = response.json()
	    js_q = response.json()
	    results = js_q["results"]
	    movie_json = results[0]
	    original_title = movie_json['original_title']
	    original_language = movie_json['original_language']
	    overview = movie_json['overview']
	    logo_path = movie_json['poster_path']
	    movieData = (f'''
**Name**: ```{original_title}```
**Language**: ```{original_language.upper()}```
**Overview**: ```{overview}```
''')
	    await client.send_message(message.chat.id, f'''
{movieData}
[\u2063](https://themoviedb.org/t/p/original{logo_path})	    
''', reply_to_message_id=message.message_id)

    except IndexError:
    	await client.send_message(message.chat.id, "```Movie not found.```")

@app.on_message(filters.command("random_movie"))
async def movie(client, message):
    try:
     randomId = random.randint(100, 85000)
     response = requests.get(f'https://api.themoviedb.org/3/movie/{randomId}?api_key={tmdb_api_key}&language={tmdb_lang}')
     movie_json = response.json()
     original_title = movie_json['original_title']
     original_language = movie_json['original_language']
     overview = movie_json['overview']
     logo_path = movie_json['poster_path']
     movieData = (f'''
**Name**: ```{original_title}```
**Language**: ```{original_language.upper()}```
**Overview**: ```{overview}```
''')
     await client.send_message(message.chat.id, f'''
{movieData}
[\u2063](https://themoviedb.org/t/p/original{logo_path})	    
''', reply_to_message_id=message.message_id)

    except KeyError:
    	await client.send_message(message.chat.id, "```Movie not found.```")

@app.on_message(filters.command("show"))
async def movie(client, message):
    try:
	    showinput_withcmd = message.text
	    showinput = showinput_withcmd.replace("/show ", "")
	    response = requests.get(f'https://api.themoviedb.org/3/search/tv?api_key={tmdb_api_key}&query={showinput}&language={tmdb_lang}')
	    movie_json = response.json()
	    js_q = response.json()
	    results = js_q["results"]
	    movie_json = results[0]
	    original_name = movie_json['original_name']
	    original_language = movie_json['original_language']
	    overview = movie_json['overview']
	    logo_path = movie_json['poster_path']
	    movieData = (f'''
**Name**: ```{original_name}```
**Language**: ```{original_language.upper()}```
**Overview**: ```{overview}```
''')
	    await client.send_message(message.chat.id, f'''
{movieData}
[\u2063](https://themoviedb.org/t/p/original{logo_path})	    
''', reply_to_message_id=message.message_id)

    except IndexError:
    	await client.send_message(message.chat.id, "```TV Show not found.```")

app.run()
#asyncio.get_event_loop().run_until_complete(main())
