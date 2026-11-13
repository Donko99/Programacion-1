"""
Grupo 8
Nombre del archivo: Figuras.py
Descripcion: Este programa permite al usuario seleccionar entre varias figuras
Autor: Cesar Osciel Marquez Prado y Santiago Quijada Cecena
"""

while True:
    print("--- MENU ---")
    print("1. Reloj de arena")
    print("2. Rombo")
    print("3. Mono")
    print("4. Copa")
    print("5. Todas las figuras")
    print("6. Salir")
    
    opcion = input("Seleccione una opcion (1-6): ")
    
    if opcion == '6':
        break
        
    if opcion != '1' and opcion != '2' and opcion != '3' and opcion != '4' and opcion != '5':
        continue
        
    simbolo = input("Ingrese el simbolo para las figuras: ")
    if len(simbolo) != 1:
        continue
        
    dimension_str = input("Ingrese la dimension impar (5 a 17): ")
    if not isinstance(int(dimension_str), int):
        continue
        
    n = int(dimension_str)
    if n < 5 or n % 2 == 0 or n > 17:
        continue
        
    print("\n")
    
    for i in range(n):
        if opcion == '1' or opcion == '5':
            d = abs(i - n // 2)
            e = 2 * d + 1
            p = n // 2 - d
            print(" " * p + simbolo * e + " " * p, end="   ")
            
        if opcion == '2' or opcion == '5':
            d = abs(i - n // 2)
            e = n - 2 * d
            p = d
            print(" " * p + simbolo * e + " " * p, end="   ")
            
        if opcion == '3' or opcion == '5':
            fila = ""
            for j in range(n):
                if (j <= i and j <= n - 1 - i) or (j >= i and j >= n - 1 - i):
                    fila += simbolo
                else:
                    fila += " "
            print(fila, end="   ")
            
        if opcion == '4' or opcion == '5':
            if i <= n // 2:
                p = i
                e = n - 2 * i
                print(" " * p + simbolo * e + " " * p, end="   ")
            elif i < n - 1:
                p = n // 2
                print(" " * p + simbolo + " " * p, end="   ")
            else:
                print(simbolo * n, end="   ")
                
        print()
        
    print("\n")
    
    for i in range(n):
        if opcion == '1' or opcion == '5':
            d = abs(i - n // 2)
            e = 2 * d + 1
            p = n // 2 - d
            if e == 1:
                print(" " * p + simbolo + " " * p, end="   ")
            elif e == n:
                print(simbolo * n, end="   ")
            else:
                print(" " * p + simbolo + " " * (e - 2) + simbolo + " " * p, end="   ")
                
        if opcion == '2' or opcion == '5':
            d = abs(i - n // 2)
            e = n - 2 * d
            p = d
            if e == 1:
                print(" " * p + simbolo + " " * p, end="   ")
            else:
                print(" " * p + simbolo + " " * (e - 2) + simbolo + " " * p, end="   ")
                
        if opcion == '3' or opcion == '5':
            fila = ""
            for j in range(n):
                if j == 0 or j == n - 1 or j == i or j == n - 1 - i:
                    fila += simbolo
                else:
                    fila += " "
            print(fila, end="   ")
            
        if opcion == '4' or opcion == '5':
            if i == 0:
                print(simbolo * n, end="   ")
            elif i < n // 2:
                p = i
                e = n - 2 * i
                print(" " * p + simbolo + " " * (e - 2) + simbolo + " " * p, end="   ")
            elif i == n // 2:
                p = n // 2
                print(" " * p + simbolo + " " * p, end="   ")
            elif i < n - 1:
                p = n // 2
                print(" " * p + simbolo + " " * p, end="   ")
            else:
                print(simbolo * n, end="   ")
                
        print()