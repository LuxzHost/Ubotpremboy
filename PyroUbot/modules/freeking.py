import random
import re
import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil
from PyroUbot import *
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import *

from PyroUbot import *

@PY.BOT("freezero")
async def _(client, message):
    buttons = BTN.ALWAYSBOYSZ(message)
    sh = await message.reply("""<u><b>𝗙𝗜𝗧𝗨𝗥 𝗙𝗥𝗘𝗘 𝗞𝗜𝗡𝗚𝗣𝗥𝗘𝗠 𝗨𝗦𝗘𝗥𝗕𝗢𝗧!</b></u>
<blockquote><b>/ai -  ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴍᴜ</b>
<b>/brat - ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇxᴛ ᴜɴᴛᴜᴋ ᴅɪ ᴊᴀᴅɪᴋᴀɴ ғᴏᴛᴏ</b>
<b>/adzan - ᴍᴀsᴜᴋᴋᴀɴ ᴋᴏᴛᴀ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴊᴀᴅᴡᴀʟ ᴀᴅᴢᴀɴ</b>
<b>/tourl - ʀᴇᴘʟʏ ғᴏᴛᴏ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪ ᴊᴀᴅɪᴋᴀɴ ʟɪɴᴋ</b>
<b>/tiktok - ʙᴇʀɪᴋᴀɴ ʟɪɴᴋ ᴠᴛ/ʟɪɴᴋ ғɪᴅɪᴏ ᴛɪᴋᴛᴏᴋ ᴜɴᴛᴜᴋ ᴅɪ ᴅᴏᴡɴʟᴏᴀᴅ</b></blockquote>

<blockquote><b>ᴏᴡɴᴇʀ ᴜsᴇʀʙᴏᴛ ᴅɪʙᴀᴡᴀʜ sɪɴɪʜ</b>
<b>ᴏᴡɴᴇʀ ᴜsᴇʀʙᴏᴛ: <a href=https://t.me/zerossz>ᴏᴡɴᴇʀ ᴜʙᴏᴛ ᴘʀᴇᴍ ϟ xZero ᴛᴇᴀᴍ</a></b></blockquote>""", reply_markup=InlineKeyboardMarkup(buttons))