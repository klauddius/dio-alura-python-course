print('********************************')
print("Bem vindo ao jogo de Adivinhação")
print('********************************')

numero_secreto = 42
rodada = 1
total_tentativas = 3

while (rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada=rodada+1

print("Fim do Jogo")
