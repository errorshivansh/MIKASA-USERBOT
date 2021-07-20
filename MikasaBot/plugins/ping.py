import asyncio
import datetime

from . import *

@bot.on(mikasa_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def pong(mikasa):
    if mikasa.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(mikasa, "`·.·★ ℘ıŋɠ ★·.·´")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"╰•★★  ℘ơŋɠ ★★•╯\n\n    ⚘  `{ms}`\n    ⚘  __**Oɯɳҽɾ**__ **:**  {mikasa_mention}"
    )


CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your ʍɨӄǟֆǟ ẞø†"
).add_warning(
  "✅ Harmless Module"
).add()

# MikasaBot
