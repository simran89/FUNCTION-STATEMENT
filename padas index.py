import pandas as pd
import matplotlib.pyplot as plt
def load_and_inspect_data():
    df=pd.read_csv("C:/Users/GCS-3.29/Downloads/table_20260930 (4).csv")
    print(df.head())
    return df
df=load_and_inspect_data()
