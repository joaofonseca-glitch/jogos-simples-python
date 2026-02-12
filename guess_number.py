import random

print("Seja muito bem vindo ao Guess Number do João!")
erro_teto = 0
erro_num = 0

while True:
    choice_number = input("Digite o número teto do desafio: ")

    if choice_number.isdigit(): #.isdigit() é uma função que analisa a string e vê se é um número, mas em formato de string. se a variavel não for uma string essa função vai dar erro.
        choice_number = int(choice_number)
        break
    else:
        erro_teto = erro_teto + 1
        if erro_teto >= 3:
            print(
                f"Porra aí tu ta de marola ja errou o bglh {erro_teto} vezes menó vtnc vai jogar mais porra nenhuma mais não")
            break
        elif erro_teto > 1:
            print("crlh cara ja te falei q é número porraaa")
        else:
            print("Não cara... é número. Tu tem que digitar um número...")

if isinstance(choice_number, int): #isinstance é um função que analisa se a variável é um inteiro. Pode analisar se é outra coisa, dependendo do que você colocar no lado direito do parênteses.
    random_number = random.randint(0, choice_number)
    tentativas = 1

    while True:

        answer_user = input("Adivinhe o número: ")
        if answer_user.isdigit():
            answer_user = int(answer_user)
        else:
            erro_num = erro_num + 1
            if erro_num >= 3:
                print(
                    f"Porra aí tu ta de marola ja errou o bglh {erro_num} vezes menó vtnc vai jogar mais porra nenhuma mais não")
                break
            elif erro_num > 1 and erro_teto == 2:
                print("Tu é burrin pacaralho mrm kkkkkk escaralhando o bglh")
                continue
            elif erro_num > 1 and erro_teto == 1:
                print("De novo paizão ? é número que vc tem que digitar.")
                continue
            else:
                print("É número que tu tem q digitar aí meu padrin")
                continue

        if answer_user == random_number:
            print("Acertou!")
            if tentativas >= 5:
                print(
                    f"Pqp tu é horrível !!! Você conseguiu só na {tentativas}° tentativa KKKK")
            elif tentativas > 1:
                print(
                    f"BOA mlkk !!! Você conseguiu na {tentativas}° tentativa")
            else:
                print(
                    f"Aí tu deu aula, namoral. Tu conseguiu de primeira, brabo dms slc")
                break
        elif answer_user > random_number:
            print("Chutou alto, o número é menor que isso...")
            tentativas = tentativas + 1
        else:
            print("Chutou baixo, o número é maior que isso...")
            tentativas = tentativas + 1
else:
    print("FIM DO JOGO")
