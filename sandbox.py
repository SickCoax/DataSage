import pandas as pd
import numpy as np

# df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\Income Prediction\adult train.csv")
# df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\Titanic-Dataset.csv")
# df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\Fashion MNIST\fashion-mnist_train.csv")
# df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\creditcard.csv")
# df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\house_price.csv")
df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\car_price_dataset_medium.csv")

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


print(f"Number of Null values for each  columns : \n{df.isnull().sum()}")
print()


## Making Logic to detect problem type(classification or regression)

target = "Price_USD"

total_rows = len(df)
unique = df[target].nunique()
ratio = unique / total_rows

if df[target].dtype == "object" or df[target].dtype == "string" :
    print("Classifcation")
elif total_rows <= 10 :
    if ratio <= 0.4 :
        print("Classification")
    else :
        print("Regression")
elif total_rows <= 100 :
    if ratio <= 0.10 :
        print("Classification")
    else :
        print("Regression")
elif ratio <= 0.05 :
    print("Classification")
else :
    print("Regression")