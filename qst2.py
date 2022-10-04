# Questão 2

num = int(input("Adicione a sua média: "))

while num < 1 or num > 10:
  print(num, " — O dado informado não é válido")
  num = int(input("Adicione a sua média: "))
else:
  print("O valor inserido foi:", num)
