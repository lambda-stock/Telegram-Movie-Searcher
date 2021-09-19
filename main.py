from pyrogram import Client, filters
import asyncio
from time import time
import time
import os
import requests
import random

bot_token = "1990847591:AAH_7H4G0ir56lzSFe9734pYeg3JSvtjF3U"
api_id = 7076738
api_hash = 'd94bef53b704118a934e5a4d776f8999'

app = Client(
	"LambdaBot",
	bot_token=bot_token,
	api_id=api_id,
	api_hash=api_hash
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, f"""**Hoşgeldin** @{message.from_user.username}.
**Grup**: ```{message.chat.title}```
**Davet bağlantısı**:  ```t.me/{message.chat.username}```
**Kullanıcı ID'niz**: ```{message.from_user.id}```

Daha fazla bilgi için özelden yazabilirsin.
""")

#@app.on_message(filters.private)
#async def log(client, message):
#    await client.send_message('sgteammain', f"""
#Özelden bir mesaj gönderildi:
#	
#{message.text}

#Gönderen: {message.from_user.id}
#""")

@app.on_message(filters.command("info"))
async def info(client, message):
    await client.send_message(message.chat.id, f"""**Kullanıcı Bilgisi**
ID: ```{message.reply_to_message.from_user.id}```
Kullanıcı adı: @{message.reply_to_message.from_user.username}
İsim: {message.reply_to_message.from_user.first_name}
Soyad: {message.reply_to_message.from_user.last_name}
Data Center: ```{message.reply_to_message.from_user.dc_id}```
""")

@app.on_message(filters.command("data"))
async def data(client, message):
    await client.send_message(message.chat.id, f"""```{message.from_user}```""")

@app.on_message(filters.command("send"))
async def send(client, message):
    await client.send_message(message.chat.id, f"""Data was successfully sent to terminal.""")
    print(message)

@app.on_message(filters.command("input"))
async def input(client, message):
    userinput_withcmd = message.text
    userinput = userinput_withcmd.replace("/input ", "")
    await client.send_message(message.chat.id, f"{userinput}")

@app.on_message(filters.command("sf"))
async def sf(client, message):
	await client.send_sticker(message.chat.id, "CAACAgQAAx0CWqpnwwACAa9hRH5t3HVl22A_3_w_iy1591nvrAACBwsAAto7KVINinLxIBg42x4E")
@app.on_message(filters.command("get_sticker_id"))
async def get_sticker_id(client, message):
	await client.send_message(message.chat.id, f"```{message.reply_to_message.sticker.file_id}```")

@app.on_message(filters.command("send_sticker"))
async def send_sticker(client, message):
    stickinput_withcmd = message.text
    stickinput = stickinput_withcmd.replace("/send_sticker ", "")
    await client.send_sticker(message.chat.id, f"{stickinput}")

@app.on_message(filters.command("movie"))
async def movie(client, message):
    try:
	    movieinput_withcmd = message.text
	    movieinput = movieinput_withcmd.replace("/movie ", "")
	    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=acd27ee9ab6eaee8e6448c2bdc9bf1e1&query={movieinput}&language=tr-TR')
	    movie_json = response.json()
	    js_q = response.json()
	    results = js_q["results"]
	    movie_json = results[0]
	    original_title = movie_json['original_title']
	    original_language = movie_json['original_language']
	    overview = movie_json['overview']
	    logo_path = movie_json['poster_path']
	    movieData = (f'''
**İsim**: ```{original_title}```
**Dil**: ```{original_language.upper()}```
**Açıklama**: ```{overview}```
''')
	    await client.send_message(message.chat.id, f'''
{movieData}
[\u2063](https://themoviedb.org/t/p/original{logo_path})	    
''', reply_to_message_id=message.message_id)

    except IndexError:
    	await client.send_message(message.chat.id, "```Film bulunamadı.```")

@app.on_message(filters.command("random_movie"))
async def movie(client, message):
    try:
     randomId = random.randint(100, 85000)
     response = requests.get(f'https://api.themoviedb.org/3/movie/{randomId}?api_key=acd27ee9ab6eaee8e6448c2bdc9bf1e1&language=tr-TR')
     movie_json = response.json()
     original_title = movie_json['original_title']
     original_language = movie_json['original_language']
     overview = movie_json['overview']
     logo_path = movie_json['poster_path']
     movieData = (f'''
**İsim**: ```{original_title}```
**Dil**: ```{original_language.upper()}```
**Açıklama**: ```{overview}```
''')
     await client.send_message(message.chat.id, f'''
{movieData}
[\u2063](https://themoviedb.org/t/p/original{logo_path})	    
''', reply_to_message_id=message.message_id)

    except KeyError:
    	await client.send_message(message.chat.id, "```Film bulunamadı.```")

@app.on_message(filters.command("tv"))
async def movie(client, message):
    try:
	    showinput_withcmd = message.text
	    showinput = showinput_withcmd.replace("/tv ", "")
	    response = requests.get(f'https://api.themoviedb.org/3/search/tv?api_key=acd27ee9ab6eaee8e6448c2bdc9bf1e1&query={showinput}&language=tr-TR')
	    movie_json = response.json()
	    js_q = response.json()
	    results = js_q["results"]
	    movie_json = results[0]
	    original_name = movie_json['original_name']
	    original_language = movie_json['original_language']
	    overview = movie_json['overview']
	    logo_path = movie_json['poster_path']
	    movieData = (f'''
**İsim**: ```{original_name}```
**Dil**: ```{original_language.upper()}```
**Açıklama**: ```{overview}```
''')
	    await client.send_message(message.chat.id, f'''
{movieData}
[\u2063](https://themoviedb.org/t/p/original{logo_path})	    
''', reply_to_message_id=message.message_id)

    except IndexError:
    	await client.send_message(message.chat.id, "```Dizi bulunamadı.```")

app.run()
#asyncio.get_event_loop().run_until_complete(main())