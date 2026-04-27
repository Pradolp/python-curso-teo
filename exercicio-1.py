# %%
lista_nums = []

while True:
    add_num = input('Digite um número, se quiser sair presione enter')
    if add_num == '':
        break
    lista_nums.append(add_num)



# %%
lista = [1,1,1,3,2,4,5,1,3,2,4,3,2,2]

contagem = {}

for num in lista:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1

print(contagem)
        