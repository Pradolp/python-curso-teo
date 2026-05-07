# %%
file = "dados.csv"
# Abrindo o arquivo e criando uma lista
with open(file) as open_file:
    data = open_file.readlines()

print(data)
# %%
# Tratando a primera linha dessa lista
data_header = data[0]
keys = data_header.strip("\n").split(";")


# %%
# Criando um dicionario para colocar chaves e valores

dados = dict()
for key in keys:
    dados[key] = []

for linha in data[1:]:
    args = linha.strip("\n").split(";")
    for colunas in range(len(args)):   
        dados[keys[colunas]].append(args[colunas])

dados

# %%
