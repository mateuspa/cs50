# testando rotinas de treinamentos Python

# implementando recursos em phyton
"""
# implementando loops
agenda = ["mateus", "marcela", "fernanda", "joana","maria"]

for n in range (len(agenda)):
    print(n,":",agenda[n])

"""

# implementando dicionário e loops
"""
pessoas = {
    "mateus": "Uberaba",
    "marcela": "Boston",
    "fernanda": "Minneapolis",
    "joana": "terra de ninguem",
    "maria": "qualquer lugar",
}

for pessoa in pessoas:
    print(pessoa,":",pessoas[pessoa])
"""

# implementando dicionário e loops
import time

print("")
pessoas = [
    {"nome": "mateus", "cidade": "Uberaba", "estado": "Minas Gerais"},
    {"nome": "marcela", "cidade": "Boston","estado": "MA"},
    {"nome": "fernanda", "cidade": "Minneapolis","estado": "MN"},
    {"nome": "joana", "cidade": "terra de ninguem","estado": None},
    {"nome": "maria", "cidade": "qualquer lugar","estado": None}
]

print("nome", "cidade", "estado", "\n", sep=" | ", )
for pessoa in pessoas:
    print(pessoa["nome"], pessoa["cidade"], pessoa["estado"], sep=" | ")
print("")
timer(3)
