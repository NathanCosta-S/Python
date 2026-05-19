nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"
print(f"Aluno: {nome}")
print(f"Média: {media}")
print(f"Situação: {situacao}")