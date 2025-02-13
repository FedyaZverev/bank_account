import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture()
def test_filter():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


def test_currency(test_filter):
    result = list(filter_by_currency(test_filter, "USD"))
    assert result == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


@pytest.mark.parametrize(
    "currency_code, expected_result",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                }
            ],
        ),
        ("EUR", []),
    ],
)
def test_filter_by_currency(test_filter, currency_code, expected_result):
    result = list(filter_by_currency(test_filter, currency_code))
    assert result == expected_result


@pytest.fixture
def sample_transactions():
    return [
        {"id": 939719570, "state": "EXECUTED", "description": "Перевод организации"},
        {"id": 142264268, "state": "EXECUTED", "description": "Перевод со счета на счет"},
        {"id": 873106923, "state": "EXECUTED", "description": "Перевод со счета на счет"},
    ]


@pytest.mark.parametrize(
    "input_transactions, expected_descriptions",
    [
        (
            [
                {"id": 939719570, "state": "EXECUTED", "description": "Перевод организации"},
                {"id": 142264268, "state": "EXECUTED", "description": "Перевод со счета на счет"},
                {"id": 873106923, "state": "EXECUTED", "description": "Перевод со счета на счет"},
                {"id": 895315941, "state": "EXECUTED", "description": "Перевод с карты на карту"},
                {"id": 594226727, "state": "CANCELED", "description": "Перевод организации"},
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),
        ([{"id": 123, "state": "EXECUTED"}], ["Описание отсутствует"]),
        ([], []),
        (
            [
                {"id": 939719570, "state": "EXECUTED", "description": "Перевод организации"},
                {"id": 142264268, "state": "EXECUTED", "description": "Перевод со счета на счет"},
            ],
            ["Перевод организации", "Перевод со счета на счет"],
        ),
    ],
)
def test_transaction_descriptions(sample_transactions, input_transactions, expected_descriptions):
    result = list(transaction_descriptions(input_transactions))

    assert result == expected_descriptions

    assert len(sample_transactions) == 3


def test_sample_transactions_fixture(sample_transactions):
    assert all("description" in transaction for transaction in sample_transactions)
    assert all(transaction["state"] == "EXECUTED" for transaction in sample_transactions)


@pytest.fixture
def card_range():
    return {"start": 1000, "stop": 1005, "count": 6}


@pytest.mark.parametrize(
    "start, stop, expected_first, expected_last",
    [
        (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0003"),
        (100, 105, "0000 0000 0000 0100", "0000 0000 0000 0105"),
        (9999999999999990, 9999999999999995, "9999 9999 9999 9990", "9999 9999 9999 9995"),
    ],
)
def test_card_number_generator(card_range, start, stop, expected_first, expected_last):
    assert start >= 1 and stop <= 9999999999999999

    cards = list(card_number_generator(start, stop))

    assert cards[0] == expected_first
    assert cards[-1] == expected_last

    assert len(cards) == stop - start + 1

    for card in cards:
        assert len(card) == 19
        assert card.count(" ") == 3
