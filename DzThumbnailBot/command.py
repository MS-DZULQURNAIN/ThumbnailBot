from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from config import START_MSG, CHANNEL_ID
from DzThumbnailBot.button import START_BTN

# FUNCTION COMMAND
def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Bot.on(filter("start"))
async def start(bot, message):
  text = START_MSG.format(message.from_user.mention)
  butt = START_BTN
  await message.reply_text(text, reply_markup=butt, disable_web_pahe_preview=True)
  id = f'{message.sender_id}'
  tag = f'{message.sender.first_name}](tg://user?id={message.sender_id})'
  await bot.send_message(int(CHANNEL_ID), f"**#BOT_START**\n\n{tag} MEMULAI BOT🔥\nUser id : `{id}`")
