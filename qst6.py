# Questão 6

idade = []
altura = []

for i in range(5):
  idade.append(int(input("Coloque aqui sua idade: ")))
  altura.append(float(input("Coloque aqui sua altura: ")))

idade.reverse()
altura.reverse()

print(idade)
print(altura)
