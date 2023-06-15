from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from config import FSUB, BOT_NAME

@Bot.on_message(filters.incoming & filters.private, group=-1)
async def fsub(bot, message):
  if not FSUB:
    return True
  try:
    await bot.get_chat_member(FSUB, message.from_user.id)
  except UserNotParticipant:
    if FSUB.startswith("-100"):
      link = await bot.export_chat_invite_link(FSUB)
    else:
      link = f"https://t.me/{FSUB}"
    tfsub = f"👋Halo {message.from_user.mention}\n\nSebelum menggunakan {BOT_NAME} kamu harus subscribe atau join channel dibawah ini jika sudah klik coba lagi💡"
    bfsub = InlineKeyboardMarkup([
                                  [InlineKeyboardButton(text="Join Channel", url=link),],
                                  [InlineKeyboardButton(text="Coba lagi", url=f"https://t.me/{bot.username}?start={message.command[1]}")]
                                ])
    await message.reply_text(tfsub, reply_markup=bfsub)
    await message.stop_propagation()
