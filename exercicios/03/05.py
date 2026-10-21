# Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?

# %%

import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep = ";")
df.head(15)

# %%

df.loc[9]["qtdePontos"]

# %%