# Questão 1

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
provaFinal = 10 - media
recuperacao = 10 - media + 2

print("A sua média aritmética é: ", round(media, 1))

if media == 10:
    print("Sua média foi:", media, "Você foi aprovado com distinção!")
elif media >= 7:
    print("O aluno foi aprovado por média! Sendo esta:",  media)
else:
    print("O aluno foi reprovado! Tendo a média de:",  media)
