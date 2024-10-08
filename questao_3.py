def verificar_primos(lista):
    for num in lista:
        primo = True

        if num < 2:
            continue

        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
        
        if primo:
            print(f"{num} é primo!")

verificar_primos([1, 2, 3, 9, 12, 13, 21, 91, 211, 1024])