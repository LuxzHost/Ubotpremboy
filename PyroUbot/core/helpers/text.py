from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, ubot, get_expired_date


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b></blockquote>
"""

    def START(message):
        return f"""
<blockquote><b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

<b> 📚💎@{bot.me.username} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ</b>

🚀ʙᴏᴛ ɪɴɪ ᴅɪᴋᴇᴍʙᴀɴɢᴋᴀɴ ᴏʟᴇʜ <a href=tg://openmessage?user_id={OWNER_ID}>@zerossz</a> ᴊɪᴋᴀ ᴀᴅᴀ ᴋᴇsᴀʟᴀʜᴀɴ ᴀᴛᴀᴜᴘᴜɴ ᴍᴀsᴀʟᴀʜ ᴅᴍ ᴏᴡɴᴇʀ ʙᴏᴛ ᴅɪᴀᴛᴀs

ᴘᴜʙʟɪᴄ ғɪᴛᴜʀ:
/freezero

𝙲𝙰𝚁𝙰 𝚂𝙴𝚆𝙰 𝚄𝚂𝙴𝚁𝙱𝙾𝚃:
(ᴜꜱᴇʀʙᴏᴛ ɪɴɪ ᴀᴋᴀɴ ʙᴇʀᴋᴇᴍʙᴀɴɢ!! ᴊɪᴋᴀ ɪɴɢɪɴ ᴍᴇᴍʙᴇʟɪ ᴜꜱᴇʀʙᴏᴛ ᴀᴛᴀᴜ ʀᴇꜱᴇʟʟᴇʀ ʙɪꜱᴀ ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴜᴛᴀᴍᴀ ᴋᴀʀɴᴀ ᴜꜱᴇʀʙᴏᴛ ɪɴɪ ʙᴇʟᴜᴍ ꜱᴜᴘᴘᴏʀᴛ ᴛʀᴀɴꜱᴀᴋꜱɪ ᴏᴛᴏᴍᴀᴛɪꜱ!!!, ᴊɪᴋᴀ ᴀᴅᴀ ᴋᴇɴᴅᴀʟᴀ ꜰɪᴛᴜʀ ᴇʀᴏʀ ʙɪꜱᴀ ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴜᴛᴀᴍᴀ ᴀɢᴀʀ ᴅɪ ᴘᴇʀʙᴀɪᴋɪ)

ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b></blockquote>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: {harga}.000</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
 <b>├ Qʀɪꜱ ᴀʟʟ ᴘᴀʏᴍᴇɴᴛ </b>
<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ {total}.000</b>
<b>🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}</b> 

OWNER BOT : <a href=tg://openmessage?user_id={OWNER_ID}>@zerossz</a> 

<b>🛍 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>╭〢 ᴛʜʀᴇᴇʙᴏᴛ ᴋᴇ </b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├〢 ᴀᴄᴄᴏᴜɴᴛ </b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ╰〢ᴜsᴇʀ ɪᴅ </b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def POLICY():
        return """ <blockquote><b>ᴊɪᴋᴀ ᴀᴅᴀ ᴋᴇɴᴅᴀʟᴀ sɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ  <a href=tg://openmessage?user_id={OWNER_ID}>@zerossz</a></b></blockquote>
"""
