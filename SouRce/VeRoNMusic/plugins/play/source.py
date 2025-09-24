from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VeRoNMusic import app  

# دالة لرسائل الدردشة الخاصة
@app.on_message(filters.command(["سورس", "السورس"], "") & filters.private, group=10)
async def sourcy_private(client: Client, message: Message):
    await message.reply_video(
        video="https://t.me/s2wwv/26",
        caption="●━◉⟞⟦ 𝙎𝙊𝙐𝙍𝘾𝙀 𝐉𝐀𝐊 ⟧⟝◉━●\n\n✧ ¦ مـرحـبا بـك فـي سـوࢪس فـيـࢪوטּ 😊 \n✧ ¦ وظـفـتـي هـيا حـمـايـه الـجـࢪوب ⚙️\n✧ ¦ بـشـغـل اغاني و فديوهات في الكول 🎸\n✧ ¦ بـنزل اغاني و فيديوهات بردو  يـسـڪࢪ 📥\n✧ ¦ تـم انـشاء السـوࢪس بـتاࢪيخ 24/12/2020\n\n●━◉⟞⟦ 𝙎𝙊𝙐𝙍𝘾𝙀 𝐉𝐀𝐊 ⟧⟝◉━●",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("‹ 𝖣𝖾𝗏 Veron ›", url="https://t.me/wwvvwl")],
                [InlineKeyboardButton("‹ 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ›", url="https://t.me/xvwwvl"),
                 InlineKeyboardButton("‹ 𝖦𝗋𝗈𝗎𝗉 ›", url="https://t.me/xvwwvl")],
                [InlineKeyboardButton("‹ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ›", url=f"https://t.me/{app.username}?startgroup=true")]
            ]
        )
    )

# دالة لرسائل المجموعة
@app.on_message(filters.command(["سورس", "السورس"], "") & filters.group, group=10)
async def sourcy_group(client: Client, message: Message):
    await message.reply_video(
        video="https://t.me/s2wwv/26",
        caption="●━◉⟞⟦ 𝙎𝙊𝙐𝙍𝘾𝙀 𝐉𝐀𝐊 ⟧⟝◉━●\n\n✧ ¦ مـرحـبا بـك فـي سـوࢪس فـيـࢪوטּ 😊 \n✧ ¦ وظـفـتـي هـيا حـمـايـه الـجـࢪوب ⚙️\n✧ ¦ بـشـغـل اغاني و فديوهات في الكول 🎸\n✧ ¦ بـنزل اغاني و فيديوهات بردو  يـسـڪࢪ 📥\n✧ ¦ تـم انـشاء السـوࢪس بـتاࢪيخ 24/12/2020\n\n●━◉⟞⟦ 𝙎𝙊𝙐𝙍𝘾𝙀 𝐉𝐀𝐊 ⟧⟝◉━●",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("‹ 𝖣𝖾𝗏 Veron ›", url="https://t.me/wwvvwl")],
                [InlineKeyboardButton("‹ 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ›", url="https://t.me/xvwwvl"),
                 InlineKeyboardButton("‹ 𝖦𝗋𝗈𝗎𝗉 ›", url="https://t.me/xvwwvl")],
                [InlineKeyboardButton("‹ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ›", url=f"https://t.me/{app.username}?startgroup=true")]
            ]
        )
    )

# دالة لرسائل القناة
@app.on_message(filters.command(["سورس", "السورس"], "") & filters.channel, group=10)
async def sourcy_channel(client: Client, message: Message):
    await message.reply_video(
        video="https://t.me/s2wwv/26",
        caption="●━◉⟞⟦ 𝙎𝙊𝙐𝙍𝘾𝙀 𝐉𝐀𝐊 ⟧⟝◉━●\n\n✧ ¦ مـرحـبا بـك فـي سـوࢪس فـيـࢪوטּ 😊 \n✧ ¦ وظـفـتـي هـيا حـمـايـه الـجـࢪوب ⚙️\n✧ ¦ بـشـغـل اغاني و فديوهات في الكول 🎸\n✧ ¦ بـنزل اغاني و فيديوهات بردو  يـسـڪࢪ 📥\n✧ ¦ تـم انـشاء السـوࢪس بـتاࢪيخ 24/12/2020\n\n●━◉⟞⟦ 𝙎𝙊𝙐𝙍𝘾𝙀 𝐉𝐀𝐊 ⟧⟝◉━●",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("‹ 𝖣𝖾𝗏 Veron ›", url="https://t.me/wwvvwl")],
                [InlineKeyboardButton("‹ 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ›", url="https://t.me/xvwwvl"),
                 InlineKeyboardButton("‹ 𝖦𝗋𝗈𝗎𝗉 ›", url="https://t.me/xvwwvl")],
                [InlineKeyboardButton("‹ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ›", url=f"https://t.me/{app.username}?startgroup=true")]
            ]
        )
    )
    
# دالة لرسائل الدردشة الخاصة
@app.on_message(filters.command(["انشاء سورس", "انشاء السورس"], "") & filters.private, group=10)
async def sourcy_private(client: Client, message: Message):
    await message.reply_video(
        video="https://t.me/s2wwv/26",
        caption="تاريخ انشاء سورس جاك 2020⚡",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("‹ 𝖣𝖾𝗏 Veron ›", url="https://t.me/wwvvwl")],
                [InlineKeyboardButton("‹ 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ›", url="https://t.me/xvwwvl"),
                 InlineKeyboardButton("‹ 𝖦𝗋𝗈𝗎𝗉 ›", url="https://t.me/xvwwvl")],
                [InlineKeyboardButton("‹ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ›", url=f"https://t.me/{app.username}?startgroup=true")]
            ]
        )
    )

# دالة لرسائل المجموعة
@app.on_message(filters.command(["انشاء سورس", "انشاء السورس"], "") & filters.group, group=10)
async def sourcy_group(client: Client, message: Message):
    await message.reply_video(
        video="https://t.me/s2wwv/26",
        caption="تاريخ انشاء سورس جاك 2020⚡",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("‹ 𝖣𝖾𝗏 Veron ›", url="https://t.me/wwvvwl")],
                [InlineKeyboardButton("‹ 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ›", url="https://t.me/xvwwvl"),
                 InlineKeyboardButton("‹ 𝖦𝗋𝗈𝗎𝗉 ›", url="https://t.me/xvwwvl")],
                [InlineKeyboardButton("‹ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ›", url=f"https://t.me/{app.username}?startgroup=true")]
            ]
        )
    )

# دالة لرسائل القناة
@app.on_message(filters.command(["انشاء سورس", "انشاء السورس"], "") & filters.channel, group=10)
async def sourcy_channel(client: Client, message: Message):
    await message.reply_video(
        video="https://t.me/s2wwv/26",
        caption="تاريخ انشاء سورس جاك 2020⚡",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("‹ 𝖣𝖾𝗏 Veron ›", url="https://t.me/wwvvwl")],
                [InlineKeyboardButton("‹ 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 ›", url="https://t.me/xvwwvl"),
                 InlineKeyboardButton("‹ 𝖦𝗋𝗈𝗎𝗉 ›", url="https://t.me/xvwwvl")],
                [InlineKeyboardButton("‹ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ›", url=f"https://t.me/{app.username}?startgroup=true")]
            ]
        )
    )

if __name__ == "__main__":
    app.run()
