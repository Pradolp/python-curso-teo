# %%
frutas = {
    'Maçã' : 1.50,
    'Peira' : 2.00,
    'Uva' : 3.50,
    }

print(frutas['Maçã'])

# %%
# unpacking 
print(frutas.items())
for key, item in frutas.items():
    print(f"{key} : {item}")
# %%
