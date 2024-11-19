from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.fixture()
def test_get_number():
    return "1234 1234 1234 1234"


def test_number(test_get_number):
    assert get_mask_card_number(test_get_number) == "1234 12** **** 1234"


@pytest.mark.parametrize("card_number, expected", [("1234567890123456", "1234 56** **** 3456"),
                                                   ("1234 5678 9012 3456", "1234 56** **** 3456"),
                                                   ("12341234123412345", "Вы ввели неверное значение"),
                                                   ("123412341234123", "Вы ввели неверное значение")])


def test_mark_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number()

    with pytest.raises(AttributeError) as exc_info:
        get_mask_card_number(123)


@pytest.fixture()
def test_get_account():
    return "12345123451234512345"


def test_account(test_get_account):
    assert get_mask_account(test_get_account) == "**2345"


@pytest.mark.parametrize("account_number, expected", [("12345123451234512345", "**2345"),
                                                      ("12345 12345 12345 12345", "**2345"),
                                                      ("123451234512345123456", "Вы ввели неверное значение"),
                                                      ("1234512345123451234", "Вы ввели неверное значение")])


def test_mark_account(account_number, expected):
    assert get_mask_account(account_number) == expected






