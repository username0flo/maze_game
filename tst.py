# Créé par rodetf, le 20/01/2025 en Python 3.7

def print_map(grille):
    for i in grille:
        for j in i:
            print("#" if j else "0" , end = " ")
        print()
    print("\n")

lst = [1,2,3,4,5]
print(lst.index(3))
print(lst.index(10))

"""lst =  [(1,1),(1,2),(3,2),(2,4)]
for i in range(5):
    for j in range(5):
        if (i,j) in lst:
            print(i,j)
"""


'''
0 0 0 0 0
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
'''