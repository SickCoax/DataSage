import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


def infer_problem_type(df , target) :

        total_rows = len(df)
        unique = df[target].nunique()
        ratio = unique / total_rows

        if df[target].dtype == "object" or df[target].dtype == "string" :
            return "Classification"

        elif total_rows <= 10 :
            if ratio <= 0.4 :
                return "Classification"
            else :
                return "Regression"

        elif total_rows <= 100 :
            if ratio <= 0.10 :
                return "Classification"
            else :
                return "Regression"

        elif ratio <= 0.05 :
            return "Classification"

        else :
            return "Regression"






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
    print()

    problmem_type = infer_problem_type(df , target)
    print(f"Problem type : {problmem_type}")
    print()

    if problmem_type == "Classification" :
        print("Class Distribution Analysis (Percentage) :")

        distribution_count = df[target].value_counts(normalize=True)
        distribution_percent =  distribution_count *100
        print(distribution_percent)

        distribution_percent.plot(kind="bar")
        plt.xlabel("Classes")
        plt.ylabel("Percent (%)")
        plt.title("Class Distribution Analysis")
        plt.grid()
        plt.show()