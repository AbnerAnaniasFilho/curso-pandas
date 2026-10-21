# Quantas colunas do tipo object há no arquivo produtos.csv ?

# %%

import pandas as pd

df = pd.read_csv("../../data/produtos.csv", sep = ";")
df

# %%

(df.dtypes == "str").sum()

# %%
