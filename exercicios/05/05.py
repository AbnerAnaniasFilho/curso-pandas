# Selecione a primeira transação diária de cada cliente.

# %%

import pandas as pd

df = pd.read_csv("../../data/transacoes.csv", sep = ";")
df

# %%

df["data"] = pd.to_datetime(df["DtCriacao"]).dt.date
df = df.sort_values("DtCriacao")
df.head()

# %%

primeira = df.drop_duplicates(keep="first", subset=["IdCliente", "data"])
primeira

# %%
