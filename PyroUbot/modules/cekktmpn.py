import random
from pyrogram import *
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄᴇᴋ ᴋᴇᴛᴀᴍᴘᴀɴᴀɴ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Cek Ketampanan</b>

Perintah:
<code>{0}cektmpn [nama]</code> → Ratting berapa persen ketampanan nama  

Sumber: Random generator berdasarkan nama.</blockquote></b>
"""

KHODAM_LIST = [
    "1%🤮", "55%🙂", "30%🙃", "70%😉",
    "90%😎", "100%🤯", "4%🤢", "10%😖", "1000%😱"
]

@PY.UBOT("cektmpn")
@PY.TOP_CMD
async def cek_khodam(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply_text("⚠️ Gunakan format: cektmpn [nama]")

    nama = args[1]
    khodam = random.choice(KHODAM_LIST)
    hasil = f"<blockquote><b>🤭HASIL KETAMPANAN🤭\n\n🧑 Nama: `{nama}`\n Persen: `{khodam}`</blockquote></b>"
    await message.reply_text(hasil)