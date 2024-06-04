from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Посмотреть напоминания")],
    [KeyboardButton(text="Создать напоминание"), KeyboardButton(text="Удалить напоминание")]
], resize_keyboard=True)