import pandas as pd
from analyze import analyze_basic , analyze_ml
from data_preprocessing import handle_missing

df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\Titanic-Dataset.csv")
# df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\Income Prediction\adult train.csv")
# df = pd.read_csv(r"G:\My Drive\Codes\Learning\Python\Sample\Fashion MNIST\fashion-mnist_train.csv")

while True :

    print("Choice        Action")
    print("  1 : Basic Analysis of Dataset")
    print("  2 : ML Analysis of Dataset")
    print("  3 : Handle Missing Values ")
    print("  4 : EXIT")
    print()

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
            analyze_ml(df , "")
            print()
            print()
        case 3 :
            df = handle_missing(df)
            print()
            print()
        case 4 :
            print("SUCCESFULLY EXITED")
            print()
            break 
        case _ :
            print("INVALID CHOICE")