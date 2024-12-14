def filter_by_currency(transactions, currency_code):
    """
    Генератор для фильтрации транзакций по коду валюты.

    Функция проходит по списку транзакций и возвращает только те,
    которые имеют указанный код валюты в операции"""
    for transaction in transactions:

        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and "code" in transaction["operationAmount"]["currency"]
        ):

            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction


def transaction_descriptions(transactions):
    """
    Генератор описаний транзакций.

    Функция извлекает описания из списка транзакций.
    Если описание отсутствует, возвращает стандартное сообщение"""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start, stop):
    """Преобразуем стартовое и конечное значение в целые числа для итерации"""
    start_num = int(start)
    stop_num = int(stop)

    """Проверяем, чтобы start не был больше end"""
    if start_num > stop_num:
        raise ValueError("Начальное значение должно быть меньше или равно конечному значению.")

    """Проверяем, чтобы значения были в допустимом диапазоне"""
    if start_num < 1 or stop_num > 9999999999999999:
        raise ValueError("Номера карт должны быть в диапазоне от 0000000000000001 до 9999999999999999.")

    """Генерируем номера карт"""
    for num in range(start_num, stop_num + 1):
        """Форматируем номер карты в строку с пробелами"""
        card_number = f"{num:016d}"
        yield " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
