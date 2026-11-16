# Nombre del archivo: Numeros arabigos a numeros romanos.py
# Descripcion: Este programa permite al usuario convertir un número arábigo a su equivalente en números romanos.

n = int(input('Número (1-4000): '))

if 1 <= n <= 4000:
    miles    = n // 1000
    centenas = n // 100 % 10
    decenas  = n // 10 % 10
    unidades = n % 10

    # Unidades (I, V, X)
    if unidades == 9:
        r_unidades = 'IX'
    elif unidades >= 5:
        r_unidades = 'V' + 'I' * (unidades - 5)
    elif unidades == 4:
        r_unidades = 'IV'
    else:
        r_unidades = 'I' * unidades

    # Decenas (X, L, C)
    if decenas == 9:
        r_decenas = 'XC'
    elif decenas >= 5:
        r_decenas = 'L' + 'X' * (decenas - 5)
    elif decenas == 4:
        r_decenas = 'XL'
    else:
        r_decenas = 'X' * decenas

    # Centenas (C, D, M)
    if centenas == 9:
        r_centenas = 'CM'
    elif centenas >= 5:
        r_centenas = 'D' + 'C' * (centenas - 5)
    elif centenas == 4:
        r_centenas = 'CD'
    else:
        r_centenas = 'C' * centenas

    romano = 'M' * miles + r_centenas + r_decenas + r_unidades
    print(romano)
else:
    print('Datos inválidos')