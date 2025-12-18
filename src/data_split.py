from datetime import datetime
from typing import Tuple

import pandas as pd


def train_test_split(
    df: pd.DataFrame,
    cutoff_date: datetime,
    target_column_name: str,
) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    """
    Split data into train and test sets based on cutoff_date.
    
    Args:
        df: DataFrame with pickup_hour column
        cutoff_date: Date to split train/test data
        target_column_name: Name of the target column
        
    Returns:
        X_train, y_train, X_test, y_test
    """
    # Remove timezone from cutoff_date if present to match pickup_hour
    if hasattr(cutoff_date, 'tz') and cutoff_date.tz is not None:
        cutoff_date = cutoff_date.tz_localize(None)
    
    # Ensure pickup_hour is also tz-naive for comparison
    df = df.copy()
    if df['pickup_hour'].dt.tz is not None:
        df['pickup_hour'] = df['pickup_hour'].dt.tz_localize(None)
    
    train_data = df[df.pickup_hour < cutoff_date].reset_index(drop=True)
    test_data = df[df.pickup_hour >= cutoff_date].reset_index(drop=True)

    X_train = train_data.drop(columns=[target_column_name])
    y_train = train_data[target_column_name]
    X_test = test_data.drop(columns=[target_column_name])
    y_test = test_data[target_column_name]

    return X_train, y_train, X_test, y_test
