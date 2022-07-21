from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start():
    yes_btn = InlineKeyboardButton('Конечно хочу!', callback_data='profile')
    start_kb = InlineKeyboardMarkup()
    start_kb.add(yes_btn)
    return start_kb

def profile():
    separate_btn = InlineKeyboardButton('Разделить звук на дорожки', callback_data='separate')
    create_meme_btn = InlineKeyboardButton('Сделать мем', callback_data='create_meme')
    profile_kb = InlineKeyboardMarkup()
    profile_kb.add(separate_btn).add(create_meme_btn)
    return profile_kb