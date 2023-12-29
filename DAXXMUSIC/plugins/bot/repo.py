from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ ☆ ωεℓ¢σмє ᴛᴏ ʀᴏᴄᴋʏ's яєρσѕ ☆ ✪

 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("rocky"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ 🥺", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ᴍᴀᴅᴀᴅ ᴄʜɪʏᴇᴀ", url="https://t.me/DECENT_CHATTING"),
          InlineKeyboardButton("👑ᴏᴡɴᴇʀ👑", url="https://t.me/M3_4_U"),
          ],
               [
                InlineKeyboardButton("ᴊᴏɪɴ ᴊᴀʀᴜʀ ᴋᴀʀɴᴀ ʜᴀɪ", url="https://t.me/II_ROCKY_II"),

],
[
              InlineKeyboardButton("ʀᴇᴘᴏ ʟᴏ", url=f"https://t.me/youreyesbammby/6"),
              InlineKeyboardButton("︎ʜᴀᴄᴋɪɴɢ", url=f"https://t.me/+uODuAfHYl9QxNWVl"),
              ],
              [
              InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧︎", url=f"https://github.com"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://github.com"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧𝗚𝗣𝗧", url=f"https://github.com"),
],
[
              InlineKeyboardButton("𝗩𝗣𝗦", url=f"https://github.com"),
              InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘︎", url=f"https://github.com"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗛𝗔𝗖𝗞︎", url=f"https://github.com"),
InlineKeyboardButton("𝗜𝗗 𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com"),
],
[
InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://github.com"),
InlineKeyboardButton("ʟᴏ", url=f"https://t.me/TUM_MUJHE_NHI_JANTI/3"),
],
[
InlineKeyboardButton("ʜᴀʏ😇", url=f"https://t.me/JADUGR_HUN_BHAI/4"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/91842fae069322f61d73f.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
