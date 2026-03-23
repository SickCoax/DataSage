import pandas as pd
import numpy as np 

def analyze_basic(df) :
    print(f"Number of Columns : {len(df.columns)}")
    print(f"Number of Rows : {len(df)}")
    print()

    cat_cols = df.select_dtypes(include=["string" , "object"]).columns
    num_cols = df.select_dtypes(include=["number"]).columns
    print()

    print(f"Number of catagorial column : {len(cat_cols)}")
    print(f"Number of Numerical column : {len(num_cols)}")
    print()

    print(f"Catagorial Column : {cat_cols}")
    print(f"Numerical Column : {num_cols}")
    print()

    print(df.info())
    print()

    print(df.describe())
    print()

    Null_Values = [
        "?" , 
        " ?",
        "? ",
        "NA" , 
        "N/A" , 
        "null" , 
        "NULL" , 
        "None" , 
        "nan" , 
        "-" , 
        "--" , 
        "unknown" , 
        "missing"
    ]

    df = df.replace(Null_Values , np.nan)


    print(f"Null values for each  columns : \n{df.isnull().sum()}")







def analyze_ml(df , target) :

    print(f"Number of Columns : {len(df.columns)}")
    print(f"Number of Rows : {len(df)}")
    print()

    cat_cols = df.select_dtypes(include=["string" , "object"]).columns
    num_cols = df.select_dtypes(include=["number"]).columns
    print()

    print(f"Number of catagorial column : {len(cat_cols)}")
    print(f"Number of Numerical column : {len(num_cols)}")
    print()

    print(f"Catagorial Column : {cat_cols}")
    print(f"Numerical Column : {num_cols}")
    print()

    print(df.info())
    print()

    print(df.describe())
    print()

    Null_Values = [
        "?" , 
        " ?",
        "? ",
        "NA" , 
        "N/A" , 
        "null" , 
        "NULL" , 
        "None" , 
        "nan" , 
        "-" , 
        "--" , 
        "unknown" , 
        "missing"
    ]

    df = df.replace(Null_Values , np.nan)


    print(f"Null values for each  columns : \n{df.isnull().sum()}")
    