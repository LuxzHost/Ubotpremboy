from pyrogram import Client, filters
import requests
import os
import mimetypes
from PyroUbot import *

__MODULE__ = "ᴍᴇᴅɪᴀғɪʀᴇ"
__HELP__ = """
<b>✮ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴅɪᴀғɪʀᴇ ✮</b>

<blockquote><b>perintah :
<code>{0}mf</code> link
Download link mediadire</b></blockquote>
"""

@PY.UBOT("mediafire|mf")
async def _(client, message):
    args = message.text.split(" ", 1)

    if len(args) < 2:
        await message.reply_text("<emoji id=5215204871422093648>❌</emoji> Harap kirimkan URL Mediafire dengan format:\n`.mediafire <url_mediafire>`", quote=True)
        return

    mediafire_url = args[1]
    api_url = f"https://api.botcahx.eu.org/api/dowloader/mediafire?url={mediafire_url}&apikey=Biyy"

    try:
        response = requests.get(api_url)
        data = response.json()

        if data.get("status") and "result" in data:
            file_info = data["result"]
            filename = file_info["filename"]
            filesize = file_info["filesize"]
            file_url = file_info["url"]

            downloading_msg = await message.reply_text(f"<blockquote><b>📥 Mengunduh **{filename}** ({filesize})...</b></blockquote>", quote=True)

            file_path = f"./{filename}"
            file_response = requests.get(file_url, stream=True)

            with open(file_path, "wb") as file:
                for chunk in file_response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)

            mime_type, _ = mimetypes.guess_type(file_path)

            if mime_type:
                if mime_type.startswith("image"):
                    await message.reply_photo(file_path, caption=f"<blockquote><b>✅ **Gambar berhasil diunduh!**\n📂 **Nama:** `{filename}`\n📦 **Ukuran:** `{filesize}`</b></blockquote>")
                elif mime_type.startswith("video"):
                    await message.reply_video(file_path, caption=f"<blockquote><b>✅ **Video berhasil diunduh!**\n📂 **Nama:** `{filename}`\n📦 **Ukuran:** `{filesize}`</b></blockquote>")
                elif mime_type.startswith("audio"):
                    await message.reply_audio(file_path, caption=f"<blockquote><b>✅ **Audio berhasil diunduh!**\n📂 **Nama:** `{filename}`\n📦 **Ukuran:** `{filesize}`</b></blockquote>")
                else:
                    await message.reply_document(file_path, caption=f"<blockquote><b>✅ **File berhasil diunduh!**\n📂 **Nama:** `{filename}`\n📦 **Ukuran:** `{filesize}`</b></blockquote>")
            else:
                await message.reply_document(file_path, caption=f"<blockquote><b>✅ **File berhasil diunduh!**\n📂 **Nama:** `{filename}`\n📦 **Ukuran:** `{filesize}`</b></blockquote>")

            os.remove(file_path)

            await downloading_msg.delete()
        else:
            await message.reply_text("<emoji id=5215204871422093648>❌</emoji> Gagal mendapatkan informasi file dari Mediafire.", quote=True)
    except Exception as e:
        await message.reply_text(f"<emoji id=5215204871422093648>❌</emoji> Terjadi kesalahan:\n`{str(e)}`", quote=True)
        
