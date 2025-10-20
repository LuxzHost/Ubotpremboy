import asyncio
import requests
import os
from pyrogram.raw.functions.messages import DeleteHistory
import aiohttp
from PyroUbot import *

__MODULE__ = "ᴛɪᴋᴛᴏᴋ"
__HELP__ = """
<blockquote> <b>Bantuan Untuk Tiktok

Perintah : <code>{0}tiktok</code> tiktok <b>[link nya]</b>
  Download Vt No Wm.</b></blockquote>

"""

async def download_file(url, path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(path, 'wb') as f:
                    f.write(await response.read())
            else:
                print(f"Failed to download file: {response.status}")

async def downloader_tiktok(client, message, perintah, tujuan):
    url = f"https://api.botcahx.eu.org/api/dowloader/tiktok?url={tujuan}&apikey=025a6ef0"
    headers = {"accept": "application/json"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as res:
            if res.status == 200:
                data = await res.json()
                if data['status'] and data['code'] == 200:
                    if perintah == "video":
                        video_url = data['result']['video']
                        video_path = "video.mp4"
                        await download_file(video_url, video_path)
                        await client.send_video(message.chat.id, video_path, caption=f"Download by: {client.me.mention}")
                        os.remove(video_path)
                    elif perintah == "music":
                        music_url = data['result']['music']
                        music_path = "music.mp3"
                        await download_file(music_url, music_path)
                        await client.send_audio(message.chat.id, music_path, caption=f"<b>Download by: {client.me.mention}</b>")
                        os.remove(music_path)
                    else:
                        return await message.reply("Gunakan format vidio atau music.")
                else:
                    print("Failed to fetch download URLs.")
            else:
                print(f"Request failed with status code {res.status}")

@PY.UBOT("tt")
async def _(client, message):
    if len(message.command) < 3:
        return await message.reply(
            f"<code>{message.text.split()[0]}</code> use vidio for video or use music for audio"
        )
    command, isi = message.command[:2]
    link = " ".join(message.command[2:])
    return await downloader_tiktok(client, message, isi, link)
