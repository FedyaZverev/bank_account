from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(word: Any = str) -> str:
    """Функция маскирует номер карты/счета"""
    word_digit = ""
    word_alpha = ""
    count = 0
    for name in word:
        if name.isdigit():
            word_digit += name
            count += 1
        if name.isalpha():
            word_alpha += name
    if count == 16:
        return f"{word_alpha} {get_mask_card_number(word_digit)}"
    if count == 20:
        return f"{word_alpha} {get_mask_account(word_digit)}"
    return "Вы ввели неверный формат"


def get_date(time: Any = str) -> str:
    """Функция принимает строку и возвращает значение в формате ДД.ММ.ГГГГ"""
    return f"{time[8:10]}.{time[5:7]}.{time[0:4]}"
