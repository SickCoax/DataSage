import pandas as pd
from analyze import analyze_basic , analyze_ml

df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\Titanic-Dataset.csv")
# df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\Income Prediction\adult train.csv")

while True :

    choice = 0 
    try :
        choice = int(input("Enter Your Choice : "))
        print()
    except ValueError :
        print("INVALID CHOICE")
        print()

    match choice :

        case 1 :
            analyze_basic(df)
            print()
            print()
        case 2 :
            analyze_ml(df , "Survived")
            print()
            print()
        case 3 :
            print("SUCCESFULLY EXITED")
            print()
            break 
        case _ :
            print("INVALID CHOICE")