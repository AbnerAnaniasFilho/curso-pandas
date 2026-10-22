# Quantos clientes tem um saldo de pontos maior que 1000?

# %%

import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep = ";")
df

# %%

filtro = df["qtdePontos"] > 1000
df[filtro].shape[0]

# %%
