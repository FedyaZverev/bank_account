import datetime
import json
import os
from typing import List, Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def transactions_amount(transactions: dict) -> float | int | list[Any]:
    """Функция которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    now_data = datetime.datetime.now()
    from_value = transactions["operationAmount"]["currency"]["code"]
    amount = transactions["operationAmount"]["amount"]
    date = now_data.strftime("%Y-%m-%d")

    if from_value in ["USD", "EUR"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={from_value}&amount={amount}&date={date}"
        headers = {"apikey": api_key}

        response = requests.request("GET", url, headers=headers)

        status_code = response.status_code
        if status_code == 200:
            result = response.text
            json_dict = json.loads(result)
            end_amount = float(json_dict.get('result'))
            return float(end_amount)
        else:
            return status_code
    elif from_value == "RUB":
        return float(amount)
    else:
        return []


print(
    transactions_amount(
        {
            "id": 214024827,
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {"amount": "70946.18", "currency": {"name": "USD", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366",
        }
    )
)
