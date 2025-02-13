import logging
from logging import FileHandler
from typing import Any

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = FileHandler("../logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Any = str) -> str:
    """Функция принимает на вход номер карты и возвращает маску."""
    logger.debug(f"Начало обработки номера карты: {card_number}")
    try:
        card_numbers = card_number.replace(" ", "")
        if len(card_numbers) != 16:
            error_message = f"Некорректный номер карты: {card_number}. Ожидается 16 цифр."
            logger.error(error_message)
            return "Вы ввели неверное значение"
        else:
            masked_card_number = f"{card_numbers[0:4]} {card_numbers[4:6]}** **** {card_numbers[12:]}"
            logger.debug(f"Маска для номера карты {card_number}: {masked_card_number}")
            return masked_card_number
    except Exception as e:
        error_message = f"Произошла ошибка при обработке номера карты {card_number}: {e}"
        logger.error(error_message)
        return "Ошибка обработки номера карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его в маскированном виде."""
    logger.debug(f"Начало обработки номера счета: {account_number}")
    try:
        account_number_clean = account_number.replace(" ", "")
        if len(account_number_clean) != 20:
            error_message = f"Некорректный номер счета: {account_number}. Ожидается 20 символов."
            logger.error(error_message)
            return "Вы ввели неверное значение"
        else:
            masked_account_number = f"**{account_number_clean[-4:]}"
            logger.debug(f"Маска для номера счета {account_number}: {masked_account_number}")
            return masked_account_number
    except Exception as e:
        error_message = f"Произошла ошибка при обработке номера счета {account_number}: {e}"
        logger.error(error_message)
        return "Ошибка обработки номера счета"


print(get_mask_card_number("1234234534564567"))
print(get_mask_account("12345678901234567890"))
