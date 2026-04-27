soma = 0

while True:
    n = input('Digite um número: ')
    if(n == ''):
        break
    else:
        n = float(n)
        soma += n

print(f"{soma:.2f}")

