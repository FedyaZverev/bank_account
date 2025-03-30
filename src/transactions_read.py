import csv
import os

import pandas as pd

csv_data = os.path.abspath(__file__)
src_dir = os.path.dirname(__file__)
PATH_TO_CSV = os.path.join(os.path.dirname(src_dir), "data", "transactions.csv")
PATH_TO_XLSX = os.path.join(os.path.dirname(src_dir), "data", "transactions_excel.xlsx")


def reading_csv_transactions(path_csv: str) -> list:
    """Чтение csv файла"""
    with open(path_csv, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file, delimiter=";"))


def reading_excel_transactions(path_excel: str) -> list:
    """Чтение excel файла"""
    return pd.read_excel(path_excel).to_dict("records")
