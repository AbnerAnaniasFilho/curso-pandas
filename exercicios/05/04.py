# Qual é o id de cliente que tem maior saldo de pontos? E o menor?

# %%

import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep = ";")
df

# %%

df.sort_values(by="qtdePontos", ascending=False).head(1)["idCliente"]

# %%

df.sort_values(by="qtdePontos", ascending=True).head(1)["idCliente"]

# %%
