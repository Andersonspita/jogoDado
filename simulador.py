from random import randint

print("{:=^40}" .format(" JOGO DE DADOS "))

dado = randint(1, 7)
opcao = 1

print('''VOCÊ GOSTARIA DE JOGAR O DADO?
[ 1 ] SIM
[ 2 ] NÃO''')
opcao = int(input("Escolha sua opção: "))

while opcao != 1 and opcao != 2:
    print("OPÇÃO INVÁLIDA! Escolha uma nova opção!")
    opcao = int(input("Escolha sua opção: "))
if opcao == 1:
    while opcao == 1:
        print("Você jogou o dado e seu número é {}" .format(dado))
        opcao = int(input("Escolha uma nova opção: "))
elif opcao == 2:
    print("Você escolheu sair, obrigado e volte sempre!")