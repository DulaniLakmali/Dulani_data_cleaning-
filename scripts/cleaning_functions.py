
import pandas as pd
import numpy as np

def load_data(filepath):
    """Load CSV data from a given filepath."""
    return pd.read_csv(filepath)

def fill_missing_values(df):
    """Handle missing values based on predefined logic."""
    df['children'].fillna(0, inplace=True)
    df['agent'].fillna(0, inplace=True)
    df['company'].fillna(0, inplace=True)
    df['country'].fillna('Unknown', inplace=True)
    return df

def remove_duplicates(df):
    """Remove exact duplicate rows."""
    return df.drop_duplicates()

def remove_invalid_guests(df):
    """Remove rows where the total number of guests is zero."""
    return df[(df['adults'] + df['children'] + df['babies']) > 0]

def create_arrival_date(df):
    """Combine year, month, and day into a datetime object."""
    df['arrival_date'] = pd.to_datetime(df['arrival_date_year'].astype(str) + '-' +
                                        df['arrival_date_month'] + '-' +
                                        df['arrival_date_day_of_month'].astype(str),
                                        errors='coerce')
    return df

def treat_outliers_iqr(df, column):
    """Remove outliers from a numerical column using the IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]

def validate_data_ranges(df):
    """Check if arrival_date is within expected bounds and if values are logical."""
    assert df['arrival_date'].min().year >= 2015
    assert df['arrival_date'].max().year <= 2017
    return True
