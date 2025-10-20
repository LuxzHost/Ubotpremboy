import asyncio
from time import sleep
from PyroUbot import *

__MODULE__ = "𝚂𝙰𝙻𝙰𝙼"
__HELP__ = """
 <blockquote><b>Bantuan Untuk salam</b>

• <b>Perintah</b> : <code>{0}p</code>
• <b>Penjelasan : assalamu'alaikum.</b>

• <b>Perintah</b> : <code>{0}pe</code>
• <b>Penjelasan : Assalamualaikum Warahmatullahi Wabarakatuh.</b>

• <b>Perintah</b> : <code>{0}l</code>
• <b>Penjelasan : Wa'alaikumsalam.</b>

• <b>Perintah</b> : <code>{0}wl</code>
• <b>Penjelasan : Wa'alaikumsalam Warahmatullahi Wabarakatuh.</b>

• <b>Perintah</b> : <code>{0}as</code>
• <b>Penjelasan : coba aja.</b></blockquote>

"""


@PY.UBOT("p")
async def inijugajangandiapusataudigantikrnizzyganteng(client, message):
    await message.edit(
        "Assalamu'alaikum",
    )


@PY.UBOT("pe")
async def biarpanjangajayangpentingizzyganteng(client, message):
    await message.edit(
        "Assalamualaikum Warahmatullahi Wabarakatuh",
    )


@PY.UBOT("l")
async def biarmampuslusemuakontol(client, message):
    await message.edit(
        "waalaikumsalam",
    )


@PY.UBOT("wl")
async def ularnagapanajnagnyabukankepalangtapiizzygantengamat(client, message):
    await message.edit(
        "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
    )


@PY.UBOT("as")
async def pelerpelerpeler(client, message):
    await message.edit(
        "Salam dulu woy!",
    )
