nome = input("digite seu nome: ")
anonas = input("digite sua a data e, que nasceu: ")
anoatual = input("digite sua data de nascimento atual: ")

idade = anoatual - anonas

if idade >= 18:
    print("Você tem 18 anos ou mais e pode fazer a carteira")
if idade < 18 and idade >= 16:
    print("Você tem 16 anos ou mais e pode votar.")