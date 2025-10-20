from PyroUbot import *

__MODULE__ = "ɢᴀᴍᴇ ᴠ2"
__HELP__ = """
<blockquote>Bantuan Untuk gamev2

perintah : <code>{0}gamev2</code>
   untuk memunculkan game random 2

note: jumlah menu game cuma 3</blockquote>
"""


@PY.UBOT("gamev2")
@PY.TOP_CMD
async def game_cmd(client, message):
    try:
        x = await client.get_inline_bot_results("gamebot")
        msg = message.reply_to_message or message
        random_index = random.randint(0, len(x.results) - 1)
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[random_index].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)
