import pandas as pd

def handle_missing(df):
    df = df.copy()

    missing_ratio = df.isnull().mean()


    drop_cols = [col for col in df.columns if missing_ratio[col] < 0.02 and missing_ratio[col] > 0]


    if drop_cols:
        df.dropna(subset=drop_cols, inplace=True)


    for col in df.columns:
        if df[col].isnull().sum() > 0:

            if df[col].dtype == 'object':
                mode_val = df[col].mode()
                if not mode_val.empty:
                    df[col].fillna(mode_val[0], inplace=True)

            else:
                df[col].fillna(df[col].median(), inplace=True)

    return df
