import pandas as pd

df = pd.DataFrame.from_csv("test_data.csv", index_col=False)
for i in df.iterrows():
    dicter = i[1].to_dict()
    print dicter
