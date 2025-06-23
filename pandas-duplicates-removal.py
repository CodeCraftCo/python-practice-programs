#A Python program that creates a DataFrame and removes duplicate rows using pandas.
import pandas as pd
dat={"Name": ["Ajay", "Vijay", "Sanjay", "Sujay", "Vijay"],"Age": [25,27,22,31,27]}
df=pd.DataFrame(dat)
df_NoDuplicates=df.drop_duplicates()
print(df_NoDuplicates)