from src.utils import load_transactions
from src.external_api import convert_transaction_to_rub

transactions = load_transactions('data/operations.json')

# Обрабатываем транзакции
if transactions:
    for transaction in transactions:
        converted_amount = convert_transaction_to_rub(transaction)
        if converted_amount is not None:
            print(f"Сумма в рублях для транзакции {transaction.get('id', 'неизвестен')}: {converted_amount}")
        else:
            print(f"Не удалось конвертировать транзакцию {transaction.get('id', 'неизвестен')}: {transaction}")