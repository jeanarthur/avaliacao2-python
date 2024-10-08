amostras = [
    ("Cidade A", [12, 14, 18, 22, 35, 23, 24]),
    ("Cidade B", [23, 43, 12, 34, 12, 32, 12]),
    ("Cidade C", [33, 23, 32, 31, 23, 43, 35]),
    ("Cidade D", [20, 20, 20, 20, 20, 20, 20]),
]

def calcular_media(lista):
    return sum(lista) / len(lista)

def calcular_temperatura_media(amostras):
    resultado = []

    for amostra in amostras:
        resultado.append((amostra[0], calcular_media(amostra[1])))

    return resultado

print(calcular_temperatura_media(amostras))