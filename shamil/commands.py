# Regen & Mod by @shamilhabeebnelli
# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
from utils import USERNAME, FFMPEG_PROCESSES
from config import Config
import os
import sys
U=USERNAME
CHAT=Config.CHAT


HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\n• I am A Bot Made by @Filimsmovie\n• I Can Play Songs in Group 's\n\n• Hit /help to know about available commands.</b>"
HELP = """
🎧 <b>I Can Play Musics</b>
SRY NO ONE GONE HELP YOU  😢

© MADE BY 
[ __@FILIMSMOVIE | @ALLUADDICT__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('🆘Help🆘', callback_data='help'),
                ],[
                InlineKeyboardButton('💫 Update Channel💫', url='https://t.me/telsabots'),
                InlineKeyboardButton('💫 Other Bots💫', url='https://t.me/telsabots/13')
                ],[
                InlineKeyboardButton('👨🏼‍💻 Dev👨🏼‍💻', url='https://t.me/alluaddict'),
                InlineKeyboardButton('🥰Group🥰', url='https://t.me/filimsmovie')
                ],[
                InlineKeyboardButton('✍️Feed Back✍️', url='https://t.me/alluaddict'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/c5ab26ca0919792e78736.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('💫 Update Channel💫', url='https://t.me/telsabots'),
                InlineKeyboardButton('💫 Other Bots💫', url='https://t.me/telsabots/13')
                ],[
                InlineKeyboardButton('👨🏼‍💻 Dev👨🏼‍💻', url='https://t.me/alluaddict'),
                InlineKeyboardButton('🥰Group🥰', url='https://t.me/filimsmovie')
                ],[
                InlineKeyboardButton('✍️Feed Back✍️', url='https://t.me/alluaddict'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/c5ab26ca0919792e78736.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
