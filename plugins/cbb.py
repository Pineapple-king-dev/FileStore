#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>अहिंसक प्राणी</a>\n○ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Animes_Station'>Anime Station</a>\n○ ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Ongoing_Anime_Station'>Oɴɢᴏɪɴɢ Aɴɪᴍᴇ</a>\n○ ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/AS_Movies_Station'>Movies Station</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/Anime_Talk_Station'>Aɴɪᴍᴇ Tᴀʟᴋ Sᴛᴀᴛɪᴏɴ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ɪɴᴅᴇx', url='https://t.me/Anime_Station_Index')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
