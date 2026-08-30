import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
FILE_NAME = BASE_DIR / "data" / "expenses.csv"


def load_data():

    df = pd.read_csv(FILE_NAME)

    df["Date"] = pd.to_datetime(df["Date"])

    return df