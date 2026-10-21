# Qual o id do cliente no índice 4 no arquivo clientes.csv ?

# %%

import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep = ";")
df

# %%

df.loc[4]["idCliente"]

# %%
