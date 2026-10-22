# %%

# Quantas transações ocorreram no dia 2025-02-01?

import pandas as pd

df = pd.read_csv("../../data/transacoes.csv", sep = ";")
df.head()

# %%

filtro = (df['DtCriacao'] >= '2025-02-01') & (df['DtCriacao'] < '2025-02-02')
df[filtro].shape[0]

# %%
