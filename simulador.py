from random import randint

print("{:=^40}" .format(" JOGO DE DADOS "))

dado = randint(1, 7)

print('''VOCÊ GOSTARIA DE JOGAR O DADO?
[ 1 ] SIM
[ 2 ] NÃO''')
opcao = int(input("Escolha sua opção: "))

if opcao == 1:
    print("Você jogou o dado e seu número é {}" .format(dado))
elif opcao == 2:
    print("Você escolheu sair, obrigado e volte sempre!")
else:
    print("OPÇÃO INVÁLIDA! Escolha uma nova opção!")

