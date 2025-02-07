import time

# introdução
print("\n"
      " ___                   _         _                   ___  _ _  ___  ___  _ __ ___  _ _  _ _  ___   ___  ___  _ _  ___\n"
      "| . > ___ ._ _ _  _ _ <_>._ _  _| | ___  ___  ___  / __>| | || . || . \| / /| . \| | || \ |/  _> | __>| . || \ |/ __>\n"
      "| . \/ ._>| ' ' || | || || ' |/ . |/ . \<_> |/ . \ \__ \|   ||   ||   /|  \ | | || ' ||   || <_/\| _> | | ||   |\__ \ \n"
      "|___/\___.|_|_|_||__/ |_||_|_|\___|\___/<___|\___/ <___/|_|_||_|_||_\_\|_\_\|___/`___'|_\_|`____/|___>`___'|_\_|<___/")
time.sleep(3)
print(
    "______________________________________________________________________________________________________________________\n"
    "| Oh não! Parece que quando visitaste o museu dos tubarões extintos, na loja de recordações compraste um ovo de      |\n"
    "| um tubarão mutante. Mas afinal o tubarão não está extinto, e não ficou nada feliz ao descobrir que alguém ficou    |\n"
    "| com o seu ovo...Então decidiu raptar-te para as suas masmorras no fundo do oceno. Está tudo bem porque tens uma    |\n"
    "| poção de respiração subaquática, mas a poção não é infinita... Tens de escapar o mais rápido possível. Boa sorte!  |\n"
    "|____________________________________________________________________________________________________________________|")
usuario = str(input("Qual vai ser o teu nome?"))
# chegar perto do boss
print("A saída aproxima-se...")
# loja antes da luta final
print(f"Olá {usuario}, sou a Sereia Madrinha e estou aqui para te ajudar a derrotares...")

import random


def bau():
    chance = random.randint(1, 100)  # Gera um número entre 1 e 100

    if chance <= 60:  # 60% de chance
        ouro_ganho = random.randint(25, 60)
    elif chance <= 85:  # 25% de chance (60 + 25)
        ouro_ganho = random.randint(60, 80)
    else:  # 15% de chance (85 + 15)
        ouro_ganho = random.randint(80, 100)

    print(f"\nEncontraste um baú de tesouro! Ele contém {ouro_ganho} ouro!")
    return ouro_ganho


# Exemplo de teste:
jogador_ouro = 0  # Exemplo de um jogador com 0 ouro inicialmente
jogador_ouro += bau()  # Simula abrir um baú e adicionar ouro ao jogador
print(f"Ouro total do jogador: {jogador_ouro}")


def loja(jogador):

    escolha = None
    while escolha!="4":
        if not escolha:
            print(f"\n Bem-vindo à loja {utilizador}! ")
        print(f"O que deseja comprar?")
        itens = {
            "1": ("Espada (+5 ataque)", 30, "Espada"),
            "2": ("Poção (+20 HP)", 20, "Poção"),
            "3": ("Armadura (+10 HP)", 40, "Armadura"),
            "4": ("Sair", 0, "Sair")
        }

        if "Espada" in jogador["inventory"]:
            itens["1"] = ("Refinar espada (+5 ataque)", 30, "Espada")

        for chave, (desc, preco, _) in itens.items():
            print(f"{chave} - {desc} por {preco} ouro")

        escolha = input("Escolha um item para comprar: ")
        if escolha in itens:
            if itens[escolha][2]=="Sair":
                print("Até à próxima")
            elif jogador["ouro"] >= itens[escolha][1]:
                jogador["ouro"] -= itens[escolha][1]
                if itens[escolha][2] == "Espada":
                    jogador["attack"] += 5
                elif itens[escolha][2] == "Poção":
                    if jogador["hp"] +20 > 100:
                        jogador["hp"] = 100
                    else:
                        jogador["hp"] += 20
                elif itens[escolha][2] == "Armadura":
                    jogador["hp"] += 10
                if itens[escolha][2] not in jogador["inventory"]:
                    jogador["inventory"].append(itens[escolha][2])
                print(f" {utilizador} comprou {itens[escolha][2]}!")
            elif escolha in itens:
                print("Ouro insuficiente.")
        else:
            print("Opção inválida.")