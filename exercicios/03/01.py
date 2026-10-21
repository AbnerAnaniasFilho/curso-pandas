# Quantas linhas há no arquivo clientes.csv ?

# %%

import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep = ";")
df

# %%

linhas = df.shape[0]
linhas

# %%
