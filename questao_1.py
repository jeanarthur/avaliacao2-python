def eh_palindromo(string):
    lista = []
    for c in string:
        lista.append(c)
    lista.reverse()

    palindromo = True
    for i, c in enumerate(lista):
        if c != string[i]:
            palindromo = False
            break

    return palindromo

print("- Verificador de Palindromos -")
while (True):
    try:
        entrada = input("Digite uma palavra (ou 0 para sair): ")
        if entrada == "0":
            break
        print(f"É palindromo? {eh_palindromo(entrada)}")
    except:
        print("Valor inválido, tente novamente")