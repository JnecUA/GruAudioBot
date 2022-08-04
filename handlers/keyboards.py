from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


def start():
    yes_btn = InlineKeyboardButton('Конечно хочу!', callback_data='profile')
    start_kb = InlineKeyboardMarkup()
    start_kb.add(yes_btn)
    return start_kb


def profile():
    separate_btn = InlineKeyboardButton(
        'Разделить звук на дорожки', callback_data='separate:select')
    create_meme_btn = InlineKeyboardButton(
        'Сделать мем', callback_data='create_meme')
    webApp = WebAppInfo(url="https://tavenas.github.io/GruBotClient/")
    pay_btn = InlineKeyboardButton(text="Оплата", web_app=webApp)
    profile_kb = InlineKeyboardMarkup()
    profile_kb.add(separate_btn).add(create_meme_btn).add(pay_btn)
    return profile_kb


def create_meme():
    wide_putin_btn = InlineKeyboardButton(
        'Широкий Путин', callback_data='wide_putin:select_stretch')
    back_btn = InlineKeyboardButton('Назад', callback_data='profile')
    create_meme_kb = InlineKeyboardMarkup()
    create_meme_kb.add(wide_putin_btn).add(back_btn)
    return create_meme_kb


def select_stretch():
    without_btn = InlineKeyboardButton(
        'Без растяжения', callback_data='wide_putin:1')
    small_btn = InlineKeyboardButton('Малая', callback_data='wide_putin:2')
    medium_btn = InlineKeyboardButton('Средняя', callback_data='wide_putin:3')
    high_btn = InlineKeyboardButton('Большая', callback_data='wide_putin:4')
    back_btn = InlineKeyboardButton('Назад', callback_data='create_meme')
    select_stretch_kb = InlineKeyboardMarkup()
    select_stretch_kb.add(without_btn).add(
        small_btn, medium_btn, high_btn).add(back_btn)
    return select_stretch_kb


def select_separate():
    stems2_btn = InlineKeyboardButton(
        '2stems', callback_data='separate:2stems')
    stems4_btn = InlineKeyboardButton(
        '4stems', callback_data='separate:4stems')
    stems5_btn = InlineKeyboardButton(
        '5stems', callback_data='separate:5stems')
    back_btn = InlineKeyboardButton('Назад', callback_data='profile')
    select_separate_kb = InlineKeyboardMarkup()
    select_separate_kb.add(stems2_btn, stems4_btn, stems5_btn).add(back_btn)
    return select_separate_kb


def back(callback: str):
    back_btn = InlineKeyboardButton('Назад', callback_data=callback)
    back_kb = InlineKeyboardMarkup()
    back_kb.add(back_btn)
    return back_kb
