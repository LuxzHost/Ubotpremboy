__MODULE__ = "ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ"
__HELP__ = """
<blockquote>
<b>「 ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ 」</b>

• <b>ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}sc</code> <b>[ʟɪɴᴋ]</b>
• <b>ꜰᴜɴɢꜱɪ:</b> ᴍᴇɴɢᴜɴᴅᴜʜ ᴍᴜꜱɪᴋ ᴅᴀʀɪ ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ

• <b>ᴄᴏɴᴛᴏʜ:</b> <code>{0}sc https://soundcloud.com/username/title</code>
</blockquote>
"""

import asyncio
import requests
import os
import time as time_module
import json
import aiohttp
from PyroUbot import *

# API key untuk BetaBotz API
APIKEY = "jagoannyabot"

async def download_file(url, path):
    """Download file from URL"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(path, 'wb') as f:
                    f.write(await response.read())
                return True
            return False

async def extract_data_from_response(data):
    """Extract music URL and metadata from the BetaBotz API response"""
    try:
        # Akses data dari struktur respons BetaBotz API
        if not data.get("status"):
            return "", "ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴛʀᴀᴄᴋ", ""
        
        result = data.get("result", {})
        
        # Ambil URL musik
        music_url = result.get("url", "")
        
        # Ambil metadata
        title = result.get("title", "ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴛʀᴀᴄᴋ")
        thumbnail = result.get("thumbnail", "")
        
        return music_url, title, thumbnail
    except Exception as e:
        print(f"Error extracting data: {str(e)}")
        return "", "ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴛʀᴀᴄᴋ", ""

async def downloader_soundcloud(client, message, url):
    """SoundCloud downloader function with BetaBotz API"""
    process_msg = await message.reply(
        "<blockquote><b>⏳ ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ ᴘᴇʀᴍɪɴᴛᴀᴀɴ...</b></blockquote>"
    )
    
    # Gunakan BetaBotz API
    api_url = f"https://api.betabotz.eu.org/api/download/soundcloud?url={url}&apikey={APIKEY}"
    
    try:
        res = requests.get(api_url, timeout=15)
        
        if res.status_code != 200:
            await process_msg.edit(
                f"<blockquote><b>❌ ɢᴀɢᴀʟ ᴛᴇʀʜᴜʙᴜɴɢ ᴋᴇ ꜱᴇʀᴠᴇʀ! ᴋᴏᴅᴇ ᴇʀʀᴏʀ: {res.status_code}</b></blockquote>"
            )
            return
        
        try:
            data = res.json()
        except json.JSONDecodeError:
            await process_msg.edit(
                "<blockquote><b>❌ ʀᴇꜱᴘᴏɴꜱ ᴀᴘɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ! ʙᴜᴋᴀɴ ᴊꜱᴏɴ.</b></blockquote>"
            )
            return
        
        await process_msg.edit(
            "<blockquote><b>🔍 ꜱᴇᴅᴀɴɢ ᴍᴇɴɢᴀɴᴀʟɪꜱɪꜱ ʀᴇꜱᴘᴏɴ ᴀᴘɪ...</b></blockquote>"
        )
        
        music_url, title, thumbnail = await extract_data_from_response(data)
        
        if not music_url:
            await process_msg.edit(
                "<blockquote><b>❌ ᴜʀʟ ᴍᴜꜱɪᴋ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴅᴀʟᴀᴍ ʀᴇꜱᴘᴏɴꜱ!</b></blockquote>"
            )
            return
        
        await process_msg.edit(
            "<blockquote><b>📥 ᴍᴇɴɢᴜɴᴅᴜʜ ᴍᴜꜱɪᴋ...</b></blockquote>"
        )
        
        music_path = f"soundcloud_music_{int(time_module.time())}.mp3"
        
        if await download_file(music_url, music_path):
            await process_msg.edit(
                "<blockquote><b>📤 ꜱᴇᴅᴀɴɢ ᴍᴇɴɢɪʀɪᴍ ᴀᴜᴅɪᴏ...</b></blockquote>"
            )
            
            title_short = title[:40] + "..." if len(title) > 40 else title
            
            # Download thumbnail jika tersedia
            thumb_path = None
            if thumbnail:
                thumb_path = f"soundcloud_thumb_{int(time_module.time())}.jpg"
                await download_file(thumbnail, thumb_path)
            
            try:
                await client.send_audio(
                    message.chat.id, 
                    music_path, 
                    thumb=thumb_path if thumb_path else None,
                    caption=f"""
<blockquote>
<b>┏━═━═━═━═━═━═━═━═━┓</b>
<b>┃ 🎵 @JᴀɢᴏᴀɴUsᴇʀBᴏᴛ</b>
<b>┃                 </b>
<b>┗━═━═━═━═━═━═━═━═━┛</b>

<code>🎵 ᴍᴜꜱɪᴋ ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ</code>
<code>📝 ᴊᴜᴅᴜʟ:</code> <i>{title_short}</i>
<code>🔗 ᴜʀʟ:</code> <code>{url}</code>
<code>⬇️ ᴏʟᴇʜ:</code> {client.me.mention}
<code>⚡️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</code> <code>PyroUbot</code>
</blockquote>"""
                )
            finally:
                # Bersihkan file temporary
                if os.path.exists(music_path):
                    os.remove(music_path)
                if thumb_path and os.path.exists(thumb_path):
                    os.remove(thumb_path)
                
                await process_msg.delete()
        else:
            await process_msg.edit(
                "<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴɢᴜɴᴅᴜʜ ᴀᴜᴅɪᴏ! ᴜʀʟ ᴍᴜɴɢᴋɪɴ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ.</b></blockquote>"
            )
    
    except requests.exceptions.Timeout:
        await process_msg.edit(
            "<blockquote><b>⏱️ ᴡᴀᴋᴛᴜ ᴘᴇʀᴍɪɴᴛᴀᴀɴ ʜᴀʙɪꜱ! ꜱᴇʀᴠᴇʀ ꜱᴇᴅᴀɴɢ ꜱɪʙᴜᴋ, ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ.</b></blockquote>"
        )
    except requests.exceptions.RequestException as e:
        await process_msg.edit(
            f"<blockquote><b>❌ ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ ᴊᴀʀɪɴɢᴀɴ! ᴇʀʀᴏʀ: {str(e)}</b></blockquote>"
        )
    except Exception as e:
        await process_msg.edit(
            f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ! ᴇʀʀᴏʀ: {str(e)}</b></blockquote>"
        )

@PY.UBOT("sc")
async def soundcloud_downloader(client, message):
    """Command handler for SoundCloud downloads"""
    # Hapus pesan perintah pengguna
    try:
        await message.delete()
    except Exception as e:
        pass  # Jika gagal menghapus, lanjutkan saja
    
    if len(message.command) < 2:
        await client.send_message(
            message.chat.id,
            f"""
<blockquote>
<b>❌ ꜰᴏʀᴍᴀᴛ ᴘᴇʀɪɴᴛᴀʜ ᴛɪᴅᴀᴋ ʟᴇɴɢᴋᴀᴘ!</b>

<b>ᴄᴀʀᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴ:</b>
<code>{message.text.split()[0]}</code> <i>[ʟɪɴᴋ ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ]</i> → ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴜʜ ᴍᴜꜱɪᴋ
</blockquote>
"""
        )
        return
        
    soundcloud_url = " ".join(message.command[1:])
    await downloader_soundcloud(client, message, soundcloud_url)