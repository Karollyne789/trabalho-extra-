num1 = float(input("Digite o primeiro numero:"))
print(num1)
num2 = float(input("Digite o segundo numero:"))
print(num2)
num3 = float(input("Digite o terceiro numero:"))
print(num3)

if num1 < num2  < num3 :
	print(num1, "É O MENOR")

if num2 < num1  < num3:
	print(num2, "É O MENOR")

if num3 < num1  < num2:
	print(num3, "É O MENOR")



if num1 > num2 and num1 > num3 :
	print(num1, "É O MAIOR")

if num2 > num1 and num2 > num3:
	print(num2, "É O MAIOR")

if num3 > num1 and num3 > num2:
	print(num3, "É O MAIOR")