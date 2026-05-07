# %%
idades = [12, 15, 25, 35, 36, 54]
for i in idades:
    print(i)
# %%
print(idades)
# %%
# Alguns metodos 
print(sum(idades))
print(len(idades))
print(f"avg: {sum(idades)/len(idades)}")

# %%
#Utilizando Map e Filter
def maior_de_idade(n):
    return n > 18

def multiplicar(n):
    return n * 2

#estrtura => OBJETO = ferramenta(funcao_regra, fonte_de_dados)
#filter para filtrar um objeto iteravel
maiores_de_idade = list(filter(maior_de_idade, idades))
print(maiores_de_idade)

#map para transformar os dados em algo novo
valores_multiplicados = list(map(multiplicar, maiores_de_idade))
print(valores_multiplicados)
# %%
#Só pra lembrar: para pegar o último elemento:
print(idades[-1])
# %%
lucas = [
    ["Neve", "Andy", "Ziggs", "Ozzy"],
    ["Davi", "Nilda", "Carlos", "Laura"]
]
lucas.__len__
primeira_lista = lucas[0]
print(f"Tamanho da lista: {len(primeira_lista)}")
#lista[start : stop] stop - não está incluso
#caso não coloque valores ele vai interpretar que é do inicio ou até fim
print(primeira_lista[0:2])
print(primeira_lista[0:])
print(primeira_lista[:-1])


# %%
# [::] start stop step
# isso é o slice

def nome(nome1):
    nome_lower1 = nome1.lower()
    if (nome_lower1[::-1]) == nome_lower1:
        return True
    return False

print(nome("ovo"))



# %%
# Para caso de frase, pode-se fazer utilizando 
# filter:

def teste_palindromo(text):
    texto_filtrado = "".join(filter(str.isalnum, text)).lower()
    return texto_filtrado == texto_filtrado[::-1]

print(teste_palindromo("Socorram-me, subi no onibus em Marrocos"))
# %%
