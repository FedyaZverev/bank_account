from typing import Any


def filter_by_state(transactions: Any = list, state: str = "EXECUTED") -> list:
    """Фильтрует список словарей по значению ключа 'state'."""
    filtered_transactions = [transaction for transaction in transactions if transaction.get("state") == state]
    return filtered_transactions


def sort_by_date(date_list: Any = list, sort_date: bool = True) -> list:
    """Функция сортирует список словарей по дате."""
    sorted_data = []
    if date_list:
        sorted_data = sorted(date_list, key=lambda x: x.get("date"), reverse=sort_date)
    return sorted_data
