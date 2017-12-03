# Funktion Fakultät:

# Eingabe:
zahl = int(input('Bitte gib eine Zahl ein: '))

# Berechnung iterativ:
def fakultät_i(n):
    if n == 0:
        return 1
    else:
        j=1
        for i in range(1, n+1):
            j = j * i
        return j
# Ausgabe:
print('Fakultät iterativ:', fakultät_i(zahl))

# Berechnung rekursiv:
def fakultät_r(n):
    if n == 0:
        return 1
    else:
        return (n * fakultät_r(n-1))
# Ausgabe:
print('Fakultät rekursiv:', fakultät_r(zahl))
