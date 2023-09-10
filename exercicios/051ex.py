primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo_termo = primeiro_termo + (11-1) * razao
for c in range(primeiro_termo, decimo_termo, razao):
    print(c, end="-")
print("ACABOU !")
