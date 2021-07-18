from pyrogram import Client, filters
from pyrogram.types import Message
from utils import mp, RADIO, USERNAME
from config import Config
from config import STREAM

ADMINS=Config.ADMINS

@Client.on_message(filters.command(["r", f"r@{USERNAME}"]) & filters.user(ADMINS))
async def radio(client, message: Message):
    if 1 in RADIO:
        await message.reply_text(" ⏺Stop existing Radio📻 /sr")
        return
    await mp.start_radio()
    await message.reply_text(f"▶️Started Radio📻: <code>{STREAM}</code>")
    await message.delete()

@Client.on_message(filters.command(['sr', f"sr@{USERNAME}"]) & filters.user(ADMINS))
async def stop(_, message: Message):
    if 0 in RADIO:
        await message.reply_text(" ▶️start Radio 📻 /r")
        return
    await mp.stop_radio()
    await message.reply_text("📻Radio stream ended⏹.")
    await message.delete()
