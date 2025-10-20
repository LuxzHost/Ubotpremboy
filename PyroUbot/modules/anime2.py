from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ᴀɴɪᴍᴇ 2"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴɪᴍᴇ 2 ⦫</b>
<blockquote>
⎆ perintah :
ᚗ <code>{0}anime</code> Query
⊶ buat pertanyaan contoh <code>{0}ask</code> dimana letak Antartika

<b>ᚗ Query:</b>
    <i>⊶ keneki</i>,
    <i>⊶ megumin/i>,
    <i>⊶ yotsuba</i>,
    <i>⊶ shinomiya</i>,
    <i>⊶ yumeko</i>,
    <i>⊶ tsunade</i>,
    <i>⊶ kagura</i>,
    <i>⊶ madara</i>,
    <i>⊶ itachi</i>,
    <i>⊶ akira</i>,
    <i>⊶ toukachan</i>,
    <i>⊶ cicho</i>,
    <i>⊶ sasuke</i></blockquote>
"""

URLS = {
    "keneki": "https://api.botcahx.eu.org/api/anime/keneki?apikey=045705b1",
    "megumin": "https://api.botcahx.eu.org/api/anime/megumin?apikey=045705b1",
    "yotsuba": "https://api.botcahx.eu.org/api/anime/yotsuba?apikey=045705b1",
    "shinomiya": "https://api.botcahx.eu.org/api/anime/shinomiya?apikey=045705b1",
    "yumeko": "https://api.botcahx.eu.org/api/anime/yumeko?apikey=045705b1",
    "tsunade": "https://api.botcahx.eu.org/api/anime/tsunade?apikey=045705b1",
    "kagura": "https://api.botcahx.eu.org/api/anime/kagura?apikey=045705b1",
    "madara": "https://api.botcahx.eu.org/api/anime/madara?apikey=045705b1",
    "itachi": "https://api.botcahx.eu.org/api/anime/itachi?apikey=045705b1",
    "akira": "https://api.botcahx.eu.org/api/anime/akira?apikey=045705b1",
    "toukachan": "https://api.botcahx.eu.org/api/anime/toukachan?apikey=045705b1",
    "cicho": "https://api.botcahx.eu.org/api/anime/chiho?apikey=045705b1",
    "sasuke": "https://api.botcahx.eu.org/api/anime/sasuke?apikey=045705b1"
}

@PY.UBOT("anime")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"Query tidak valid. Gunakan salah satu dari: {valid_queries}.")
        return

    processing_msg = await message.reply("Processing....")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"Gagal mengambil gambar anime Error: {e}")
