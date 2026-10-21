# Quantas colunas do tipo int há no arquivo transacoes.csv ?

# %%

import pandas as pd

df = pd.read_csv("../../data/transacoes.csv", sep = ";")
df

# %%

(df.dtypes == "int64").sum()

# %%
