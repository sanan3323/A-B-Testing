"""Reusable preprocessing and KPI functions."""
import pandas as pd

COLS = ['Campaign Name','Date','Spend Amount',
        'Number of Impressions','Reach','Website Clicks',
        'Searches','Viewed Content','Added to Cart','Purchases']


def load_campaign(path: str) -> pd.DataFrame:
    """Load a semicolon-delimited campaign CSV,
    rename columns, and parse dates."""
    df = pd.read_csv(path, delimiter=';')
    df.columns = COLS
    df['Date'] = pd.to_datetime(df['Date'],
                                dayfirst=True, errors='coerce')
    return df


def add_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """Add five derived KPI columns."""
    df = df.copy()
    df['CTR'] = df['Website Clicks'] / df['Number of Impressions']
    df['Add_to_Cart_Rate'] = df['Added to Cart'] / df['Viewed Content']
    df['Conversion_Rate'] = df['Purchases'] / df['Website Clicks']
    df['CostperClick'] = df['Spend Amount'] / df['Website Clicks']
    df['CostperPurchase'] = df['Spend Amount'] / df['Purchases']
    return df
