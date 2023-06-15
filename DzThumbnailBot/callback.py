from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from main import Bot
from button import HOME

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "tutor":
        bhome = HOME
        await query.message.edit_text(
            text=f"**Tutorial ThumbnailRobot💡\n\n1.Kirimkan video ke ThumbnailRobot\n2.Kirimkan Thumnail/foto yg akan dijadikan Thumnail\n3.Selesai\n\nNote:\nBot hanya bisa memasang thumbnail dengan minimal durasi 20 detik,jika masih gagal silakan ajukan keluhannya ke developer👤",
            disable_web_page_preview=True,
            reply_markup=bhome
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
