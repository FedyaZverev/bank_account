import json


def load_transactions(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            else:
                print("Ошибка: JSON-файл должен содержать список транзакций.")
                return []

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        print("Ошибка: Некорректный JSON. Файл пуст или повреждён.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []
