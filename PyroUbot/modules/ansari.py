from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴀɴsᴀʀɪ ɪsʟᴀᴍɪᴄ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Ansari Islamic

perintah : <code>{0}ansari</code>
    untuk bertanya tentang ayat alquran atau tentang pertanyaan islam lainya</b></blockquote>
"""

@PY.UBOT("ansari")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<blockquote><b><emoji id=5019523782004441717>❌</emoji>bertanya tentang ayat alquran atau tentang pertanyaan islam lainya</b></blockquote>"
            )
        else:
            prs = await message.reply_text(f"<blockquote><b><emoji id=5352953358892149485>😇</emoji>Tunggu sebentar kk....</b></blockquote>")
            hai = message.text.split(' ', 1)[1]
            response = requests.get(f'https://fastrestapis.fasturl.cloud/aillm/islamic?ask={hai}')

            try:
                if "result" in response.json():
                    x = response.json()["result"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
      
