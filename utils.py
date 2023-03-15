from telebot import types
from typing import Optional
import urllib.request
import json
import certifi
import functools
from config import bot
import constants as const


def reply_keyboard_button(
    button_texts: list[str], 
    row_width: Optional[int]=None) -> types.ReplyKeyboardMarkup:
    
    keyboard_menu = types.ReplyKeyboardMarkup(
        resize_keyboard=True, 
        one_time_keyboard=True
    )

    keyboard_menu.add(*button_texts, row_width=row_width)

    return keyboard_menu


def inline_keyboard_button(
    button_texts: list[str]) -> types.InlineKeyboardMarkup:
    keyboard_menu = types.InlineKeyboardMarkup()
    for i, text in enumerate(button_texts):
        keyboard_menu.add(
            types.InlineKeyboardButton(
                text=text,
                callback_data=f'bttn{i}'
            )
        )
    return keyboard_menu


def assign_new_keys_for_dict(dict):
    return {
        f'bttn{i}': answer
        for i, answer in enumerate(dict.values())
    }


def send_message(
    chat, 
    message: str, 
    button_names: list[str] = None, 
    parse_mode: Optional[str]=None, 
    row_width: Optional[int]=None):
    
    markup = None
    if button_names is not None:
        markup = reply_keyboard_button(button_names, row_width)        
    bot.send_message(chat.id, message, 
        reply_markup=markup, 
        parse_mode=parse_mode
    )



def command_menu_catcher(func):   
    @functools.wraps(func)
    def wrapper(message):
        try:
            if message.text in list(const.BASIC_MENU_COMMANDS.keys()):
                send_message(
                    message.chat, 
                    const.BASIC_MENU_COMMANDS[message.text][0], 
                    const.BASIC_MENU_COMMANDS[message.text][1],
                    parse_mode='Markdown'
                )
            else:
                func(message)
        except Exception:
            bot.send_message(message.chat.id, 'Щось пішло не так')
    return wrapper

