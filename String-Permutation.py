# Permutation:

# Eingabe:
zeichenkette = list(input('Bitte gib eine Zeichenkette ein: '))

# Funktion Fakultät:
def fakultät_r(n):
    if n == 0:
        return 1
    else:
        return (n * fakultät_r(n-1))

# Funktion Permutation:
def permutation(zeichenkette):
    if len(zeichenkette) == 1:
        return zeichenkette
    else:
        neueliste = []
        for i in range(0, len(zeichenkette)):
            element = list(zeichenkette[i])
            restliste = list(zeichenkette[:i] + zeichenkette[i + 1 : len(zeichenkette) + 1])
            längerest = fakultät_r(len(restliste))
            xliste = permutation(restliste)
            for j in range(0, längerest):
                permutation1 = list(element + list(xliste[j]))
                neueliste.append(permutation1)
        return neueliste

# Permutationen ermitteln:
permutationen = permutation(zeichenkette)
anzahlPermutationen = len(permutationen)

# Permutationen zusammensetzen:
permutationsliste = []
for i in range(0, anzahlPermutationen):
    pstring = ''
    permutation = permutationen[i]
    for j in range(0, len(zeichenkette)):
        pstring = pstring + permutation[j]
    permutationsliste.append(pstring)

# Ausgabe:
print()
print('Anzahl Permutationen:', anzahlPermutationen)
print('Ermittelte Permutationen:')
for i in range(0, anzahlPermutationen):
    print(permutationsliste[i], end=' ')
print()
