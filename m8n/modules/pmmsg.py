# Copyright (©️) @
# By : 

from pyrogram import Client
from m8n.tgcalls import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from m8n.config import (
    BOT_USERNAME,
)

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hey 👋 I am the assistant of DKZ  music bot, didn't have a time to talk with you 🙂 kindly join @DOSTO_KI_ZHOPDI for getting support\n\nPowered by @DOSTO_KI_ZHOPDI)
  return
