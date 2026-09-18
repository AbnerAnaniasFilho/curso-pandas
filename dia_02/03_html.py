# %%

import pandas as pd
import requests
from io import StringIO

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

dfs = pd.read_html(StringIO(response.text))
dfs

# %%

df_uf = dfs[1]
df_uf.to_csv("ufs.csv", sep = ";", index = False)

# %%
