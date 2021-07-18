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

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, emoji
from utils import mp
from config import Config
playlist=Config.playlist

HELP = """

🎧 <b>I Can Play Music On VoiceChats 🤪</b>

© Powered By 
[ __@FILIMSMOVIE | @ALLUADDICT ]
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "rp":
        group_call = mp.group_call
        if not playlist:
            return
        group_call.restart_playout()
        if not playlist:
            pl = f"😖 Nothing On Que Ser"
        else:
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(
                f"{pl}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄Replay🔄", callback_data="rp"),
                            InlineKeyboardButton("⏸Pause⏸", callback_data="ps")
                        ],[
                            InlineKeyboardButton("⏭Skip⏭", callback_data="sk"),
                            InlineKeyboardButton("👥Group👥", url="https://t.me/filimsmovie")
                        ]
                    ]
                )
            )

    elif query.data == "ps":
        if not playlist:
            return
        else:
            mp.group_call.pause_playout()
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Paused\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄Replay🔄", callback_data="rp"),
                            InlineKeyboardButton("▶️Resume▶️", callback_data="rs")
                        ],[
                            InlineKeyboardButton("⏭Skip⏭", callback_data="sk"),
                            InlineKeyboardButton("👥Group👥", url='https://t.me/filimsmovie')
                        ],
                    ]
                )
            )

    
    elif query.data == "rs":   
        if not playlist:
            return
        else:
            mp.group_call.resume_playout()
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Resumed\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄Replay🔄", callback_data="rp"),
                            InlineKeyboardButton("⏸Pause⏸", callback_data="ps")
                        ],[
                            InlineKeyboardButton("⏭Skip⏭", callback_data="sk"),
                            InlineKeyboardButton("👥Group👥", url='https://t.me/filimsmovie')
                        ],
                    ]
                )
            )

    elif query.data=="sk":   
        if not playlist:
            return
        else:
            await mp.skip_current_playing()
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Skipped\n\n{pl}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄Replay🔄", callback_data="rp"),
                            InlineKeyboardButton("⏸Pause⏸", callback_data="ps")
                        ],[
                            InlineKeyboardButton("⏭Skip⏭", callback_data="sk"),
                            InlineKeyboardButton('👥 Group👥', url='https://t.me/Filimsmovie')
                            
                    ],
                ]
            )
        )
        except:
            pass
    elif query.data=="help":
        buttons = [
            [
                InlineKeyboardButton('🔰MOVIES Channel🔰', url='https://t.me/hb_new_movies'),
                InlineKeyboardButton('👥 Group👥', url='https://t.me/Filimsmovie')
                ],[
                InlineKeyboardButton('🧑🏼‍💻Dev🧑🏼‍💻', url='https://t.me/alluaddict'),
                InlineKeyboardButton('✍️FeedBack'✍️, url='https://t.me/Alluaddict')
                ],[
                InlineKeyboardButton('⚜️Updates Channel⚜️', url='https://t.me/telsabots'),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text(
            HELP,
            reply_markup=reply_markup

        )
