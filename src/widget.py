from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(mask_number: Any = str) -> str:
    """Функция маскирует номер карты/счета"""
    word_digit = ""
    word_alpha = ""
    count = 0
    for char in mask_number:
        if char.isdigit():
            word_digit += char
            count += 1
        if char.isalpha():
            word_alpha += char
    if count == 16:
        return f"{word_alpha} {get_mask_card_number(word_digit)}"
    if count == 20:
        return f"{word_alpha} {get_mask_account(word_digit)}"
    return "Вы ввели неверный формат"


def get_date(data_str: Any = str) -> str:
    """Функция принимает строку и возвращает значение в формате ДД.ММ.ГГГГ"""
    return f"{data_str[8:10]}.{data_str[5:7]}.{data_str[0:4]}"
