
def dictToList(d):
    lista = []
    for key in "0123456789BCEGHIJKLNOPQSTUWYZ":
        lista.append(d[key])
    return lista

#dict 0123456789BCEGHIJKLNOPQSTUWYZ
dictionary = {
    '0': 10,
    '1': 20,
    '2': 30,
    '3': 40,
    '4': 50,
    '5': 60,
    '6': 70,
    '7': 80,
    '8': 90,
    '9': 100,
    'B': 110,
    'C': 120,
    'E': 130,
    'G': 140,
    'H': 150,
    'I': 160,
    'J': 170,
    'K': 180,
    'L': 190,
    'N': 200,
    'O': 210,
    'P': 220,
    'Q': 230,
    'S': 240,
    'T': 250,
    'U': 260,
    'W': 270,
    'Y': 280,
    'Z': 290,
}

print(dictToList(dictionary))
