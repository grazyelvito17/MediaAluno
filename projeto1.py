# -*- coding: utf-8 -*-
"""projeto1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I2qYx5zN3h36h5-tr0IVFtwRyjEB0Xdh
"""

nota1 = float(input("informe sua primeira nota: "))
nota2 = float(input("informe sua segunda nota: "))
nota3 = float(input("informe sua terceira nota: ")) 

media = (nota1 + nota2 + nota3)/3
    
 
if (media >= 7):
    s= "aprovado"

elif (media >= 4):
    s= "Prova final"

else: 
    s= "Reprovado"

print(f"A situação do aluno é {s}, com a media de {media}")

