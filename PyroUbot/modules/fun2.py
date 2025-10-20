import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message

from PyroUbot import *


__MODULE__ = "ғᴜɴ 2"
__HELP__ = """
<blockquote>✮ Bantuan Untuk Fun 2✮

♛ Perintah: <code>{0}giben</code>
卍 Penjelasan: Fake global ban.

✓ Perintah: <code>{0}gimut</code>
卍 Penjelasan: Fake global mute.

♛ Perintah: <code>{0}gikik</code>
卍 Penjelasan: Fake global kick.

♛ Perintah: <code>{0}gikes</code>
卍 Penjelasan: Fake global broadcast.</blockquote>
"""


ok = []
nyet = [
    "50",
    "350",
    "97",
    "670",
    "24",
    "909",
    "57",
    "89",
    "4652",
    "153",
    "877",
    "890",
]
babi = ["2", "3", "6", "7", "9"]


@PY.UBOT("giben")
@PY.TOP_CMD
async def giben(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("<blockquote><b>`Gbaning...`</b></blockquote>")
    else:
        ex = await message.edit("<blockquote><b>`GBANNING!`</b></blockquote>")
    if not user_id:
        return await ex.edit(
            "<blockquote><b>Balas pesan pengguna atau berikan nama pengguna/id_pengguna</b></blockquote>"
        )
    if user_id == client.me.id:
        return await ex.edit("<blockquote><b>**Lu mau gban diri sendiri? Tolol!**</b></blockquote>")
    if user_id in DEVS:
        return await ex.edit("<blockquote><b>Devs tidak bisa di gban, only Gods can defeat Gods</b></blockquote>")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit(
                "<blockquote><b>`Balas pesan pengguna atau berikan nama pengguna/id_pengguna`</b></blockquote>"
            )
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"<blockquote><b>**#GBanned**</b></blockquote>"
        f"<blockquote><b>\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})</b></blockquote>"
        f"<blockquote><b>\n**User ID:** `{user.id}`</b></blockquote>"
    )
    if reason:
        msg += f"<blockquote><b>\n**Alasan:** `{reason}`</b></blockquote>"
    msg += f"<blockquote><b>\n**Sukses di:** `{done}` **Obrolan**</b></blockquote>"
    await asyncio.sleep(5)
    await ex.edit(msg)


@PY.UBOT("gimut")
@PY.TOP_CMD
async def gimut(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("<blockquote><b>`GMuting...`</b></blockquote>")
    else:
        ex = await message.edit("<blockquote><b>`Gmuting...`</b></blockquote>")
    if not user_id:
        return await ex.edit(
            "<blockquote><b>Balas pesan pengguna atau berikan nama pengguna/id_pengguna</b></blockquote>"
        )
    if user_id == client.me.id:
        return await ex.edit("<blockquote><b>**Lu mau gmute diri sendiri? Tolol!**</b></blockquote>")
    if user_id in DEVS:
        return await ex.edit("<blockquote><b>Devs tidak bisa di gmute, only Gods can defeat Gods</b></blockquote>")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit(
                "<blockquote><b>`Balas pesan pengguna atau berikan nama pengguna/id_pengguna`</b></blockquote>"
            )
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#GMuted**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` **Obrolan**"
    await asyncio.sleep(5)
    await ex.edit(msg)


@PY.UBOT("gikik")
@PY.TOP_CMD
async def gikik(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`GKick...`")
    else:
        ex = await message.edit("`Gkicking...!`")
    if not user_id:
        return await ex.edit(
            "Balas pesan pengguna atau berikan nama pengguna/id_pengguna"
        )
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gkick diri sendiri? Tolol!**")
    if user_id in DEVS:
        return await ex.edit("Devs tidak bisa di gkick, only Gods can defeat Gods")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit(
                "`Balas pesan pengguna atau berikan nama pengguna/id_pengguna`"
            )
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#GKicked**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` **Obrolan**"
    await asyncio.sleep(5)
    await ex.edit(msg)


@PY.UBOT("gikes")
@PY.TOP_CMD
async def gikes_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = random.choice(nyet)
    fail = random.choice(babi)
    await asyncio.sleep(5)
    await tex.edit_text(
        f"**Successfully Sent Message To** `{done}` **Groups chat, Failed to Send Message To** `{fail}` **Groups**"
  )
