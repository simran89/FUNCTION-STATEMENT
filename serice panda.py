import pandas as pd
a=pd.Series([90,85,72],index=['a','b','c'])

data={
"name": ["amit","sam","riya"],
"marks": ["90","85","75"],
"city": ["delhi","goa","mumbai"]}
df=pd.DataFrame(data)
print(df)
