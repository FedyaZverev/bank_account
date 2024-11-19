from typing import Any


def get_mask_card_number(card_number: Any = str) -> str:
    """Функция принимает на входе номер карты и возвращает маску"""
    card_numbers = card_number.replace(" ", "")
    if len(card_numbers) != 16:
        return "Вы ввели неверное значение"
    else:
        masked_card_number = f"{card_numbers[0:4]} {card_numbers[4:6]}** **** {card_numbers[12:]}"
        return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его в маскированном виде."""
    account_number_clean = account_number.replace(" ", "")
    if len(account_number_clean) != 20:
        return "Вы ввели неверное значение"
    else:
        masked_account_number = f"**{account_number_clean[-4:]}"
        return masked_account_number
