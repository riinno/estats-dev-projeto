# Code by Riinno, 2026

# -------------------------------------------------------------------------
# Importação de libs

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# Dicionário de faturamento

dict_faturamento = {
  "data_ref": [
    "2023-01-01", 
    "2020-02-01", 
    "2021-03-01", 
    "2022-04-01", 
    "2023-05-01",
    "2023-06-01", 
    "2020-07-01", 
    "2021-08-01", 
    "2022-09-01", 
    "2023-10-01",
    "2022-11-01", 
    "2023-12-01",
  ],
  "valor": [
    400000, 
    890000, 
    760000, 
    430000, 
    920000,
    340000, 
    800000, 
    500000, 
    200000, 
    900000,
    570000, 
    905000, # valor alterado para grafico se manter correto
  ]
}

# -------------------------------------------------------------------------
# Tratamento de dados

# criando DataFrame
df_faturamento = pd.DataFrame.from_dict(dict_faturamento)
# transformando data
df_faturamento["data_ref"] = pd.to_datetime(df_faturamento["data_ref"])
#print(df_faturamento.info())

# tirando média
media_valor = df_faturamento["valor"].mean()
print(media_valor)

# grafico barras
df_faturamento.sort_values("data_ref").plot.bar(x="data_ref", y="valor")
plt.show()

# grafico linhas
df_faturamento.sort_values("data_ref").plot.line(x="data_ref", y="valor")
plt.show()

# -------------------------------------------------------------------------