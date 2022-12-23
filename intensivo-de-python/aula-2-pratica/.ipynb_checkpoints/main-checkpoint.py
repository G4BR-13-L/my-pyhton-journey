import pandas as panda

dados = panda.read_csv("vendasteste.csv")
# dados = panda.drop(["Unnamed: 0"], axis=1)
display(dados)

dados = dados.dropna(how="all", axis=1)
dados = dados.dropna()
print(dados.info())

display(dados['Forma de Pagamento'].value_counts())
display(dados['Forma de Pagamento'].value_counts(normalize=True).map('{:.1%}'.format))