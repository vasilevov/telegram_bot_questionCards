from aiogram import types
from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ответ", callback_data="card_answer")],
    [InlineKeyboardButton(text="Выход", callback_data="card_exit"),
    InlineKeyboardButton(text="Следующая", callback_data="card_next")
]])

answer = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вопрос", callback_data="card_question")],
    [InlineKeyboardButton(text="Выход", callback_data="card_exit"),
    InlineKeyboardButton(text="Следующая", callback_data="card_next")
]])
