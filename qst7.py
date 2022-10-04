# Questão 7

num = int(input("Informe o número que deseja reverter: "))  
  
revNum = 0  
  
  
while (num > 0):  
    resto = num % 10  
    revNum = (revNum * 10) + resto  
    num = num // 10  
  
print("O número revertido é : {}".format(revNum)) 
