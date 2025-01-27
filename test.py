# Créé par rodetf, le 20/01/2025 en Python 3.7



lst =  [(1,1),(1,2),(3,2),(2,4)]
for i in range(5):
    for j in range(5):
        if (i,j) in lst:
            print(i,j)