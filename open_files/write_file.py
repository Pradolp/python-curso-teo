# %%
txt = "adicionando mais alguma coisa"
file_name = "historinha.txt"

with open(file_name, mode="a") as open_file:
    open_file.write(txt)
