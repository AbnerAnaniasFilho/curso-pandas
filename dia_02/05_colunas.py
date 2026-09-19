# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep = ";")
df

# %%

df.shape

# %%

df.info(memory_usage="deep")

# %%

df.dtypes

# %%

renamed_columns = {
    "QtdePontos":"QtPontos",
    "DescSistemaOrigem":"SistemaOrigem"
}
df.rename(columns=renamed_columns, inplace=True)
df

# %%

colunas = ["IdCliente", "QtPontos"]
df[colunas]

# %%
# SELECT * FROM df

df

# %%
# SELECT IdCliente FROM df

df[["IdCliente"]]

# %%
# SELECT IdCliente, QtPontos FROM df LIMIT 5

df[["IdCliente", "QtPontos"]].tail(5)

# %%

# SELECT IdCliente, IdTransacao, QtPontoa
# FROM df
# LIMIT 5

df[["IdCliente","IdTransacao", "QtPontos"]].head(5)

# %%

colunas = df.columns.to_list()
colunas.sort()
colunas

df = df[colunas]
df
# %%
