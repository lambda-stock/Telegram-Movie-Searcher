from pyrogram import Client, filters
import asyncio
from time import time
import time
import os
import requests
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import Telegraph

telegraph = Telegraph()

telegraph.create_account(short_name='1337')

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
	    telegraphCreate = telegraph.create_page(
	    original_title,
	    html_content=f'<p>{overview}</p>'
	    )
	    post = 'https://telegra.ph/{}'.format(telegraphCreate['path'])
	    movieData = (f'''
**Name**: ```{original_title}```
**Language**: ```{original_language.upper()}```
**Overview**: ```{overview[:500] + "..."}```
''')
	    await client.send_photo(message.chat.id, f"https://themoviedb.org/t/p/original{logo_path}", caption = f'''
{movieData}	    
''', reply_to_message_id=message.message_id, reply_markup=InlineKeyboardMarkup(
    [
        [
             InlineKeyboardButton(
                "Devamını oku", url=f"{post}"
            )
        ]
    ]
))
    except (IndexError, KeyError)
    	await client.send_message(message.chat.id, "```Movie not found.```")

@app.on_message(filters.command("random_movie"))
async def random_movie(client, message):
    try:
     randomId = random.randint(100, 85000)
     response = requests.get(f'https://api.themoviedb.org/3/movie/{randomId}?api_key={tmdb_api_key}&language={tmdb_lang}')
     movie_json = response.json()
     original_title = movie_json['original_title']
     original_language = movie_json['original_language']
     overview = movie_json['overview']
     logo_path = movie_json['poster_path']
     telegraphCreate = telegraph.create_page(
     original_title,
     html_content=f'<p>{overview}</p>'
     )
     post = 'https://telegra.ph/{}'.format(telegraphCreate['path'])
     movieData = (f'''
**Name**: ```{original_title}```
**Language**: ```{original_language.upper()}```
**Overview**: ```{overview[:500] + "..."}```
''')
     await client.send_photo(message.chat.id, f"https://themoviedb.org/t/p/original{logo_path}", caption = f'''
{movieData}	    
''', reply_to_message_id=message.message_id, reply_markup=InlineKeyboardMarkup(
    [
        [
             InlineKeyboardButton(
                "Devamını oku", url=f"{post}"
            )
        ]
    ]
))
    except (IndexError, KeyError):
    	await client.send_message(message.chat.id, "```Movie not found.```")

@app.on_message(filters.command("show"))
async def show(client, message):
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
	    telegraphCreate = telegraph.create_page(
	    original_name,
	    html_content=f'<p>{overview}</p>'
	    )
	    post = 'https://telegra.ph/{}'.format(telegraphCreate['path'])
	    movieData = (f'''
**Name**: ```{original_name}```
**Language**: ```{original_language.upper()}```
**Overview**: ```{overview[:500] + "..."}```
''')
	    await client.send_photo(message.chat.id, f"https://themoviedb.org/t/p/original{logo_path}", caption = f'''
{movieData}	    
''', reply_to_message_id=message.message_id, reply_markup=InlineKeyboardMarkup(
    [
        [
             InlineKeyboardButton(
                "Devamını oku", url=f"{post}"
            )
        ]
    ]
))
    except (IndexError, KeyError):
    	await client.send_message(message.chat.id, "```TV Show not found.```")

@app.on_message(filters.command("movie_id"))
async def movie_id(client, message):
    try:
	    movie_idinput_withcmd = message.text
	    movie_idinput = movie_idinput_withcmd.replace("/movie_id ", "")
	    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_idinput}?api_key={tmdb_api_key}&language=tr-TR')
	    movie_json = response.json()
	    original_title = movie_json['original_title']
	    original_language = movie_json['original_language']
	    overview = movie_json['overview']
	    logo_path = movie_json['poster_path']
	    telegraphCreate = telegraph.create_page(
	    original_title,
	    html_content=f'<p>{overview}</p>'
	    )
	    post = 'https://telegra.ph/{}'.format(telegraphCreate['path'])
	    movieData = (f'''
**İsim**: ```{original_title}```
**Dil**: ```{original_language.upper()}```
**Açıklama**: ```{overview[:500] + "..."}```
''')
	    await client.send_photo(message.chat.id, f"https://themoviedb.org/t/p/original{logo_path}", caption = f'''
{movieData}	    
''', reply_to_message_id=message.message_id, reply_markup=InlineKeyboardMarkup(
    [
        [
             InlineKeyboardButton(
                "Devamını oku", url=f"{post}"
            )
        ]
    ]
))

    except (IndexError, KeyError):
    	await client.send_message(message.chat.id, "```Film bulunamadı.```")

app.run()
#asyncio.get_event_loop().run_until_complete(main())