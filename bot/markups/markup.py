import datetime
from typing import List

import pytz
from config import types, InlineKeyboardBuilder, settings
from sql_function import databasework
import math

def menu(): # старт кнопки

    markup = (
        InlineKeyboardBuilder() #🚀
        .button(text='🔙 В главное меню', callback_data='main_menu')
        .adjust(2, repeat=True)
        .as_markup()
    )
    
    return markup

