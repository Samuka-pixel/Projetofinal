from random import choice
from random import randint

utilizador = input(f"Qual é o nome do seu personagem?\n>")
moedas = 0

loja = {
    "Poção de Vida": 20,
    "Espada": 50,
    "Armadura": 75}

while True:
    e1 = int(input(f"\nEscolha para onde ir:\n1- Direita \n2- Esquerda \n3- Frente \n>"))
    if e1 == 1:
        ganho = randint(5, 30)
        moedas += ganho
        print(f"Você ganhou {ganho} moedas. Agora tem {moedas} moedas.")
    elif e1 == 2:
        print("\nUm oponente apareceu!\n")
        vida = 100
        lut = 100
        while vida > 0 and lut > 0:
            soco = int(input(f"\n\nO que fazer? \n1- Soco\n2- Empurrão\n>"))
            if soco == 1:
                s1 = randint(20,50)
                lut -= s1
                print(f"\n{utilizador} deu um soco de {s1} de dano e o oponente ficou com {lut} de vida.")
                if lut <= 0:
                    print("Você matou o oponente!")
                    break
                s2 = randint(20, 40)
                vida -= s2
                print(f"\nO oponente deu um soco de {s2} de dano e {utilizador}  ficou com {vida} de vida.")
                if vida <= 0:
                    print("Você morreu, tente novamente!")
                    break
            elif soco == 2:
                s1 = randint(10, 40)
                lut -= s1
                print(f"\n{utilizador} deu um empurrão de {s1} de dano e o oponente ficou com {lut} de vida.")
                if lut <= 0:
                    print("Você matou o oponente!")
                    break
                s2 = randint(10, 40)
                vida -= s2
                print(f"\nO oponente deu um empurrão de {s2} de dano e {utilizador} ficou com {vida} de vida.")
                if vida <= 0:
                    print("Você morreu, tente novamente!")
                    break
            else:
                s2 = randint(20, 40)
                vida -= s2
                print(f"\nO oponente deu um soco de {s2} de dano e {utilizador}  ficou com {vida} de vida.")
                if vida <= 0:
                    print("Você morreu, tente novamente!")
                    break


    elif e1 == 3:
        print(f"Você encontrou uma loja e tem {moedas} moedas. Quer comprar algo?")
        print("Itens disponíveis:")
        print("1- Poção de Vida (20 moedas)\n2- Espada (50 moedas)\n3- Armadura (75 moedas)\n4- Sair")

        escolha = input("Escolha um número para comprar ou '4' para sair:\n>")

        opcoes = {"1": "Poção de Vida", "2": "Espada", "3": "Armadura"}

        if escolha in opcoes:
            item = opcoes[escolha]
            if moedas >= loja[item]:
                moedas -= loja[item]
                print(f"Você comprou {item} por {loja[item]} moedas. Agora tem {moedas} moedas.")
            else:
                print("Você não tem moedas suficientes para comprar esse item.")
        elif escolha == "4":
            print("Você saiu da loja.")
        else:
            print("Opção inválida.")