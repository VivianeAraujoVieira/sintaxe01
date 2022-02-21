

from tkinter import N



"""
Data: 17/02/2022
Autor: Viviane Araujo 
Enunciado: Introdução a sintaxe e tipos de dados"""



Aluno = "Viviane Araujo"


nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input ("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

media_arred = round(media)

print(f"\no aluno {Aluno} ficou com a média {media_arred}")

