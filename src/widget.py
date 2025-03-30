from typing import Any

from src.masks import get_mask_account, get_mask_card_number

word_1 = ""
word_2 = ""


def mask_account_card(mask_number: Any = str) -> str:
    """Функция маскирует номер карты/счета"""
    word_digit = ""
    word_alpha = ""
    count = 0
    mask_number.replace(" ", "")
    for char in mask_number:
        if char.isdigit():
            word_digit += char
            count += 1
        if char.isalpha():
            word_alpha += char
    word_alpha = word_alpha.lower()
    if "visa" in word_alpha:
        word_1 = word_alpha[0:4]
        word_2 = word_alpha[4:]
        word_1 = word_1.title()
        word_2 = word_2.title()
        word_alpha = word_1 + " " + word_2
    elif "master" in word_alpha:
        word_1 = word_alpha[0:6]
        word_2 = word_alpha[6:]
        word_1 = word_1.title()
        word_2 = word_2.title()
        word_alpha = word_1 + word_2
    else:
        word_alpha = word_alpha.title()
    if word_alpha != "":
        word_alpha = word_alpha + " "
    if count == 16:
        return f"{word_alpha}{get_mask_card_number(word_digit)}"
    elif count == 20:
        return f"{word_alpha}{get_mask_account(word_digit)}"
    return "Вы ввели неверный формат"


def get_date(data_str: Any = str) -> str:
    """Функция принимает строку и возвращает значение в формате ДД.ММ.ГГГГ"""
    if len(data_str) != 26:
        return "Вы ввели неверный формат"
    else:
        return f"{data_str[8:10]}.{data_str[5:7]}.{data_str[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
