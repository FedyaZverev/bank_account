def filter_by_state(transactions, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей, каждый из которых содержит информацию о транзакции.
    :param state: Значение ключа 'state', по которому нужно фильтровать. По умолчанию 'EXECUTED'.
    :return: Список словарей, соответствующих указанному значению 'state'.
    """
    filtered_transactions = [transaction for transaction in transactions if transaction.get('state') == state]
    return filtered_transactions

from datetime import datetime



def sort_by_date(transactions, reverse=True):
    """
    Сортирует список словарей по дате.

    :param transactions: Список словарей, каждый из которых содержит информацию о транзакции.
    :param reverse: Порядок сортировки. True для сортировки по убыванию (по умолчанию), False для сортировки по возрастанию.
    :return: Список словарей, отсортированный по дате.
    """
    # Функция для преобразования строки даты в объект datetime
    def parse_date(date_str):
        return datetime.fromisoformat(date_str)

    # Сортировка списка по дате с использованием ключа сортировки
    sorted_transactions = sorted(transactions, key=lambda x: parse_date(x['date']), reverse=reverse)
    return sorted_transactions