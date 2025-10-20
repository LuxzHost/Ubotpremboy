import requests
import os
from PyroUbot import *
from pyrogram.types import Message

def remini(image_path, model_type="enhance"):
    valid_models = ["enhance", "recolor", "dehaze"]
    if model_type not in valid_models:
        model_type = "enhance"

    url = f"https://inferenceengine.vyro.ai/{model_type}"
    with open(image_path, "rb") as img_file:
        files = {
            "model_version": (None, "1"),
            "image": ("enhance_image_body.jpg", img_file, "image/jpeg"),
        }
        headers = {
            "User-Agent": "okhttp/4.9.3",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
        }
        response = requests.post(url, files=files, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        raise Exception(
            f"Request failed with status code {response.status_code}: {response.text}"
        )
__MODULE__ = "𝚁𝙴𝙼𝙸𝙽𝙸"
__HELP__ = """
<b>✮ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ hd ✮<b>

<blockquote><b>perintah :
<code>{0}remini</code></b></blockquote>
"""

@PY.UBOT("remini|hd")
@PY.TOP_CMD
async def process_image(client, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply("<blockquote><b>Reply gambar yang mau di hd in dong king xjunz</b></blockquote>")
        return

    await message.reply("<blockquote><b>Proses King...</b></blockquote>")

    try:
        file_path = await message.reply_to_message.download()

        enhanced_image = remini(file_path, "enhance")

        temp_output_path = "enhanced_image.jpg"
        with open(temp_output_path, "wb") as temp_file:
            temp_file.write(enhanced_image)

        await client.send_photo(
            chat_id=message.chat.id,
            photo=temp_output_path,
            caption="<blockquote><b>SUDAH DI HD IN King</b></blockquote>",
            reply_to_message_id=message.id,
        )

        os.remove(temp_output_path)
    except Exception as e:
        await message.reply(f"<blockquote><b>YAAH EROR NIH KING JUNZ:(</b></blockquote>{e}")
