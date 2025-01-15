import json
import logging
from logging import FileHandler

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> list:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    logger.debug(f"Начало загрузки транзакций из файла: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                logger.debug(f"Успешно загружено {len(data)} транзакций из файла: {file_path}")
                return data
            else:
                error_message = "Ошибка: JSON-файл должен содержать список транзакций."
                logger.error(error_message)
                print(error_message)
                return []

    except FileNotFoundError:
        error_message = f"Файл {file_path} не найден."
        logger.error(error_message)
        print(error_message)
        return []

    except json.JSONDecodeError:
        error_message = "Ошибка: Некорректный JSON. Файл пуст или повреждён."
        logger.error(error_message)
        print(error_message)
        return []

    except Exception as e:
        error_message = f"Произошла ошибка: {e}"
        logger.error(error_message)
        print(error_message)
        return []
