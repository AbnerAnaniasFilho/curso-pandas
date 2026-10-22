# Crie uma coluna que sinalize se a pessoa tem vínculo com alguma 
# (qualquer uma) plataforma de rede social.

# %%
import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep = ";")
df

# %%

df["redesSociais"] = df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head(20)

# %%
