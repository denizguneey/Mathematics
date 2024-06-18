import numpy as np
from sympy import Rational

def mod_29_rational(num):
    numerator = num.numerator
    denominator = num.denominator
    
    # Paydada tam bölünecek ilk sayıyı bulma
    while numerator % denominator != 0:
        numerator += 29
    
    mod_29_value = (numerator // denominator) % 29
    return mod_29_value

def matrix_mod_29(matrix):
    mod_29_matrix = np.vectorize(mod_29_rational)(matrix)
    return mod_29_matrix

def get_rational_input():
    n = int(input("Matris boyutunu girin (n): "))
    matrix = []
    
    for i in range(n):
        row = []
        for j in range(n):
            while True:
                try:
                    num = input(f"Matrisin ({i+1},{j+1}) elemanını rasyonel sayı olarak girin (a/b): ")
                    a, b = map(int, num.split('/'))
                    if b == 0:
                        raise ValueError("Payda 0 olamaz.")
                    row.append(Rational(a, b))
                    break
                except ValueError as e:
                    print(f"Hata: {e}. Lütfen tekrar deneyin.")
        matrix.append(row)
    
    return np.array(matrix)

# Kullanıcıdan matrisi al
matrix = get_rational_input()

# Mod 29'da matrisin karşılıklarını hesapla
mod_29_matrix = matrix_mod_29(matrix)

print("Orijinal Matris:")
print(matrix)

print("Mod 29 Matris:")
print(mod_29_matrix)
