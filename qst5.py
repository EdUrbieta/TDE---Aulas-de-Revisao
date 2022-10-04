# Questão 5

prime = int(input("Insira o limite superior da checagem de números primos: "))
i = 1

for num in range(1, prime + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
