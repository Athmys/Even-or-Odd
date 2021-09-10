n = 0
pair = []
impair = []

for n in range(100):
    if (n % 2) == 0:
        pair.append(n)
    else:
        impair.append(n)
    n += 1

print("Nombres Pairs : " + str(pair), "Nombres Impairs : " + str(impair), sep='\n')