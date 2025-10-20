from PyroUbot import *
import requests

__MODULE__ = "ᴛɪᴋᴛᴏᴋ"
__HELP__ = """
<blockquote> <b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛɪᴋᴛᴏᴋ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}tiktok</code> tiktok <b>[link nya]</b>
ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴅᴏᴡɴʟᴏᴀᴅ ᴠᴛ ɴᴏ ᴡᴍ , ᴠɪᴅɪᴏ ᴜɴᴛᴜᴋ ᴠɪᴅᴇᴏ ᴍᴜsɪᴄ ᴜɴᴛᴜᴋ ᴍᴜsɪᴋ.</b></blockquote>

"""

@PY.UBOT("tiktok")
@PY.TOP_CMD
async def tiktok_handler(client, message):
    if len(message.command) < 2:
        await message.reply("linknya mana?")
        return

    url = message.command[1]
    proses_message = await message.reply("```\nProsess King...```")

    try:
        response = requests.get(f"https://api.diioffc.web.id/api/download/tiktok?url={url}")
        data = response.json()

        if "images" in data["result"]:
            for img_url in data["result"]["images"]:
                await client.send_photo(message.chat.id, img_url)
        else:
            video_url = data["result"]["play"]
            video_caption = data["result"]["title"]
            await client.send_video(message.chat.id, video_url, caption=f"```\nDONE King```")

            audio_url = data["result"]["music_info"]["play"]
            audio_title = data["result"]["music_info"]["title"]
            audio_author = data["result"]["music_info"]["author"]
            audio_cover = data["result"]["music_info"]["cover"]

            await client.send_audio(
                message.chat.id,
                audio_url,
                title=audio_title,
                performer=audio_author,
                thumb=audio_cover
            )

        await proses_message.delete()

    except Exception as e:
        await proses_message.delete()
        await message.reply(f"Error \n{e}")
        

@PY.BOT("tiktok")
async def tiktok_handler(client, message):
    if len(message.command) < 2:
        await message.reply("linknya mana?")
        return

    url = message.command[1]
    proses_message = await message.reply("```\nProsess King...```")

    try:
        response = requests.get(f"https://api.diioffc.web.id/api/download/tiktok?url={url}")
        data = response.json()

        if "images" in data["result"]:
            for img_url in data["result"]["images"]:
                await client.send_photo(message.chat.id, img_url)
        else:
            video_url = data["result"]["play"]
            video_caption = data["result"]["title"]
            await client.send_video(message.chat.id, video_url, caption=f"```\nDONE King```")

            audio_url = data["result"]["music_info"]["play"]
            audio_title = data["result"]["music_info"]["title"]
            audio_author = data["result"]["music_info"]["author"]
            audio_cover = data["result"]["music_info"]["cover"]

            await client.send_audio(
                message.chat.id,
                audio_url,
                title=audio_title,
                performer=audio_author,
                thumb=audio_cover
            )

        await proses_message.delete()

    except Exception as e:
        await proses_message.delete()
        await message.reply(f"Error \n{e}")
        
