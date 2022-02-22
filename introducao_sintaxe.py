"""
Como Bootcamps - Stone - /código[s]
Data: 17/02/2022
Autor: Viviane Araujo Vieira
Enunciado: Introdução aos tipos de dados (string)
"""

aluna = "Viviane Araujo Vieira da costa"

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

media_arred = round(media, 2)

print(f"\nA aluna {aluna} ficou com a média {media_arred}")