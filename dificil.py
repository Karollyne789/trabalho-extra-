conta = float(input("Insira sua conta:"))#999
senha = float(input("Insira sua senha:"))#456
saque = float(input("Insira seu saque:"))#100

if conta == 999 and senha == 456:
	print("BEM VINDO")
else:
	print("Conta e/ou senha incorretas")

dinheiro = 100 - saque

if saque > 100:
	print("SALDO INSUFICIENTE")
else:
	print("SEU SALDO È DE:","R$", dinheiro,"REAIS")
	print("VOCÊ TIROU:","R$", saque, "REAIS")
 








