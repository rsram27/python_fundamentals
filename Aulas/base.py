import pandas as pd

dt = pd.read_csv('../Arquivos/salarios.csv')

# print(dt.head(10))

# print(dt.iloc[[0,1,2,3]]) imprime pelo indice da linha
print(dt.loc[[1000]])
