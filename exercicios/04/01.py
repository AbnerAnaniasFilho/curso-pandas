# %%
# Quantos clientes tem vínculo com a Twitch?
import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep = ";")
df

# %%

filtro = df["flTwitch"] == 1
df[filtro].shape[0]

# %%
