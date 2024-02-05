
from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command


import keyboard
import random
import config
import copy

router = Router()
tempCardList = list(config.cards.keys())
random_card = copy.deepcopy(random.choice(tempCardList))
tempCardList.remove(random_card)
@router.message(Command("start"))
async def start_handler(msg: Message):

    await msg.answer(random_card, reply_markup=keyboard.question)

@router.callback_query(F.data == "card_answer")
async def flip_card(callback: CallbackQuery):
    await callback.message.edit_text(config.cards[random_card], reply_markup=keyboard.answer)

@router.callback_query(F.data == "card_question")
async def flip_card(callback: CallbackQuery):
    await callback.message.edit_text(random_card, reply_markup=keyboard.question)

@router.callback_query(F.data == "card_next")
async def next_card(callback: CallbackQuery):
    global random_card
    global tempCardList
    if len(tempCardList) > 0:
        random_card = copy.deepcopy(random.choice(tempCardList))
        tempCardList.remove(random_card)
    else:
        tempCardList = list(config.cards.keys())
        random_card = copy.deepcopy(random.choice(tempCardList))
        tempCardList.remove(random_card)
    await callback.message.edit_text(random_card, reply_markup=keyboard.question)

@router.callback_query(F.data == "card_exit")
async def exit(callback: CallbackQuery):
    await callback.message.delete()
