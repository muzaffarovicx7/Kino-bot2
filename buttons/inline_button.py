from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



tasdiqlash = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Tasdiqlash✅", callback_data="ok"), InlineKeyboardButton(text="Bekor qilish❌", callback_data="no")],
    ]
)



knma = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Add ➕", callback_data="KAdd"), InlineKeyboardButton(text="Delete ♻️", callback_data="KDel")]
    ]
)


sorov = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kino qidirish", callback_data="qidirkod"), InlineKeyboardButton(text="Admin tastiqlash", callback_data="admtas")],
        [InlineKeyboardButton(text="QR-code", callback_data="qrcode")],
    ]
)

