from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

mikasa_pic = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
mikasa_caption = f"**🔥🔥 ℓєgєи∂яу αf мιкαѕα вσт 🔥🔥**\n\n"
mikasa_caption += f"  ↼ Oᴡɴᴇʀ ⇀   : 『 {mikasa_mention} 』\n\n"
mikasa_caption += "✘ Aʙᴏᴜᴛ Mʏ Sʏsᴛᴇᴍ ✘\n\n"
mikasa_caption += f"🔹 Tᴇʟᴇᴛʜᴏɴ               :  `{tel_ver}` \n"
mikasa_caption += f"🔹 Sᴜᴘᴘᴏʀᴛ Gʀᴘ         :  [Jᴏɪɴ](t.me/MIKASA_BOT_SUPPORT)\n"
mikasa_caption += f"🔹 Sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ :  [Jᴏɪɴ](t.me/MIKASA_BOT_OP)\n"
mikasa_caption += f"🔹 Cʀᴇᴀᴛᴏʀ  :   [Tᴇᴀᴍ Mɪᴋᴀsᴀ](t.me/official_mikasa)\n"                               
#-------------------------------------------------------------------------------

@bot.on(mikasa_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(mikasa):
    if mikasa.fwd_from:
        return
    await mikasa.get_chat()
    await mikasa.delete()
    await bot.send_file(mikasa.chat_id, mikasa_pic, caption=mikasa_caption)
    await mikasa.delete()

msg = f"""
**⚡ℓєgєи∂яу αf мιкαѕα вσт⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{tel_ver}`
**Mikasa Bot :**  **{mikasa_ver}**
**Uptime   :**  `{uptime}`
**Abuse    :**  **{abuse_m}**
**Sudo     :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(mikasa_cmd(pattern="mikasa$"))
@bot.on(sudo_cmd(pattern="mikasa$", allow_sudo=True))
async def mikasa_a(event):
    try:                
        mikasa = await bot.inline_query(botname, "alive")
        await mikasa[0].click(event.chat_id)
        if event.sender_id == official_sameer:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "mikasa", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
