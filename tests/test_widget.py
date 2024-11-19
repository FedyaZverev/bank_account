from src.widget import mask_account_card, get_date
import pytest


@pytest.fixture()
def test_mask_number():
    return "1234123412341234"


def test_mask_account_card(test_mask_number):
    assert mask_account_card(test_mask_number) == "1234 12** **** 1234"


@pytest.fixture()
def test_mask_account():
    return "12341234123412341234"


def test_mask_account_number(test_mask_account):
    assert mask_account_card(test_mask_account) == "**1234"


@pytest.mark.parametrize("number, expected", [("Mae st ro12 3 4 12 3412 34 1 234", "Maestro 1234 12** **** 1234"),
                                              ("Счет12345123451234512345","Счет **2345"),
                                              ("mastercard1 23 451 2  34512 3451","MasterCard 1234 51** **** 3451"),
                                              ("Visa Classic 1234 1234 1234 1234","Visa Classic 1234 12** **** 1234"),
                                              ("VisaPlatinum 1234 1234 1234 1234","Visa Platinum 1234 12** **** 1234"),
                                              ("abvjpbr","Вы ввели неверный формат"),
                                              ("VisaGol d1 2 3412 34123  41234","Visa Gold 1234 12** **** 1234")])


def test_mark_number(number, expected):
    assert mask_account_card(number) == expected


@pytest.fixture()
def test_get_date():
    return "2024-03-11T02:26:18.671407"


def test_date(test_get_date):
    assert get_date(test_get_date) == "11.03.2024"


@pytest.mark.parametrize("data_str, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                                  ("2024-02-12T12:33:14.673407", "12.02.2024"),
                                                  ("2024-03-11T02:26:18.67140", "Вы ввели неверный формат")])


def test_get_data_mark(data_str, expected):
    assert get_date(data_str) == expected
