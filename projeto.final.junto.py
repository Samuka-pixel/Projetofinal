import random
from time import sleep
print("\n"
 " ___                   _         _                   ___  _ _  ___  ___  _ __ ___  _ _  _ _  ___   ___  ___  _ _  ___\n" 
"| . > ___ ._ _ _  _ _ <_>._ _  _| | ___  ___  ___  / __>| | || . || . \| / /| . \| | || \ |/  _> | __>| . || \ |/ __>\n"
"| . \/ ._>| ' ' || | || || ' |/ . |/ . \<_> |/ . \ \__ \|   ||   ||   /|  \ | | || ' ||   || <_/\| _> | | ||   |\__ \ \n"
"|___/\___.|_|_|_||__/ |_||_|_|\___|\___/<___|\___/ <___/|_|_||_|_||_\_\|_\_\|___/`___'|_\_|`____/|___>`___'|_\_|<___/")
sleep(2)
print("______________________________________________________________________________________________________________________\n"
      "|Oh não! Parece que quando visistaste o museu dos tubarões extintos, na loja de recordações compraste um ovo de      |\n"
      "| um tubarão mutante. Mas afinal o tubarão não está extinto, e não ficou nada feliz ao descobrir que alguém ficou    |\n"
      "| com o seu ovo...Então decidiu raptar-te para as suas masmorras no fundo do oceno. Está tudo bem porque tens uma    |\n"
      "| poção de respiração subaquática, mas a poção não é infinita... Tens de escapar o mais rápido possível. Boa sorte!  |\n"
      "|____________________________________________________________________________________________________________________|")
sleep(5)
utilizador = input("Como gostarias de chamar o teu personagem?\n>")
def Player():
    return {
        "hp": 100,
        "ouro": 50,
        "attack": 10,
        "xp": 0,
        "inventory": []
    }

def Enemy(nome, hp, ataque, recompensa_ouro, recompensa_xp):
    return {
        "nome": nome,
        "hp": hp,
        "attack": ataque,
        "ouro": recompensa_ouro,
        "xp": recompensa_xp
    }


def Status(jogador):
    print(f"\n{'-'*3}HP: {jogador['hp']} | Gold: {jogador['ouro']} | Attack: {jogador['attack']} | XP: {jogador['xp']}{'-'*3}")
    print(f"{'-'*3}Inventory: {', '.join(jogador['inventory']) if jogador['inventory'] else 'Empty'}{'-'*3}")


def lutar(jogador, inimigo):
    print(f"\n{inimigo['nome']} apareceu!")
    sleep(1)
    while jogador["hp"] > 0 and inimigo["hp"] > 0:
        acao = int(input(f"\nO que fazer? \n1- Golpe forte\n2- Ataque rápido\n>"))
        if acao == 1:
            dano = random.randint(20, 50)
        elif acao == 2:
            dano = random.randint(10, 40)
        else:
            dano = 0

        inimigo["hp"] -= dano
        print(f"\n{utilizador} atacou com {dano} de dano! {inimigo['nome']} ficou com {inimigo['hp']} HP.")
        sleep(1)

        if inimigo["hp"] <= 0:
            print(f"{utilizador} derrotou o oponente!")
            jogador["ouro"] += inimigo["ouro"]
            jogador["xp"] += inimigo["xp"]
            print(f"{utilizador} ganhou {inimigo['ouro']} ouro e {inimigo['xp']} XP!")
            break

        dano_inimigo = random.randint(10, 40)
        jogador["hp"] -= dano_inimigo
        print(f"\nO inimigo atacou e causou {dano_inimigo} de dano! {utilizador} ficou com {jogador['hp']} HP.")
        sleep(1)

        if jogador["hp"] <= 0:
            print(f"{utilizador} morreu, tente novamente!")
            break


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


def bau(jogador):
        chance = random.randint(1, 100)

        if chance <= 60:  # 60% de chance
            ouro_ganho = random.randint(25, 60)
        elif chance <= 85:  # 25% de chance (60 + 25)
            ouro_ganho = random.randint(60, 80)
        else:  # 15% de chance (85 + 15)
            ouro_ganho = random.randint(80, 100)

        print(f"\nEncontraste um baú de tesouro! Ele contém {ouro_ganho} ouro!")
        return ouro_ganho
        jogador["ouro"] += "ouro_ganho"

def boss_final(jogador):
    boss = Enemy("Dragon Shark", 120, 20, 100, 100)
    print("\n CHEGOU A HORA DA BATALHA FINAL! ")
    sleep(1)
    lutar(jogador, boss)

    if jogador["hp"] > 0:
        print(f"\n PARABÉNS! {utilizador} derrotou o chefe final e venceu o jogo! ")
    else:
        print(f"\n {utilizador} foi derrotado pelo chefe final. Fim de jogo.")


def jogo():
    jogador = Player()
    num_salas = 12


    print(f"{'-'*10}Bem-vindo ao jogo de exploração {utilizador}! ⚔{'-'*10}")


    for n_sala in range(num_salas):
        Status(jogador)
        direcao = int(input("""\nVocê quer ir para a esquerda ou para a direita?
1 - Direita
2 - Esquerda
3 - Sair
> """))
        if direcao == 3:
            print(f"Obrigada por jogar {utilizador}!")
            return


        if n_sala == num_salas/2:
            evento = "Loja"
        else:
            evento = random.choice(["Loja", "Luta", "Tesouro"])

        if evento == "Loja":
            loja(jogador)
        elif evento == "Luta":
            nomes_inimigos = ["Uma alforreca", "Um tubarão", "Uma sereia", "Uma lula gigante"]
            nome_inimigo = random.choice(nomes_inimigos)
            inimigo = Enemy(nome_inimigo, random.randint(40, 60), random.randint(5, 10), random.randint(10, 20),
                            random.randint(5, 15))
            lutar(jogador, inimigo)
            if jogador["hp"] <= 0:
                print(f"\n {utilizador} foi derrotado. Fim de jogo.")
                return
        elif evento == "Tesouro":
            bau(jogador)


    loja(jogador)
    print(f"\n{utilizador} sente a sala a aquecer...\n")
    sleep(1)
    voltar = int(input(f"""E de repente ve uma sombra... parece um dragao.. ou um tubarao... deseja avancar?
1- Sim!
>"""))
    if voltar == 1:
        boss_final(jogador)


    fim = int(input("Quer repetir?\n1- Sim\n2- Nao\n>"))
    if fim == 1:
        print("O jogo vai reiniciar!\n\n")
        sleep(2)
        jogo()
    else:
        print(f"Obrigada por jogar {utilizador}!")
        sleep(2)
        return



jogo()
