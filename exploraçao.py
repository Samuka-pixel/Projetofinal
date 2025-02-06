import random
utilizador = input(f"Qual é o nome do seu personagem?\n>")
dif = int(input(f'Qual é a dificuldade que queres jogar? (1 = facil; 2 = normal; 3 = dificl)'))
if dif == 1:
    num_salas = 7
elif dif == 2:
    num_salas = 10
elif dif == 3:
    num_salas = 15
name = utilizador
hp = 100
g = 50
xp = 0
inventory = []

def Player():
    name = utilizador
    hp = 100
    g = 50
    xp = 0
    inventory = []

def stats(jogador):
    print(f'O teu nome é {utilizador}\n'
          f'Tens {hp} de vida\n'
          f'Tens {g} de ouro\n'
          f'Tens {xp} de xp')
    print(f'Inventario:{inventory}')
def luta():
    print("Luta!")
    #Para Maria: Isto é para trocar com o teu codigo!

def bau():
    print("bau!!")
    #Para Laura: isto é para trocar com o teu codigo!

def loja():
    print("Loja!!")
    # Para Laura: isto é para trocar com o teu codigo!

def game():
    jogador = Player()

    #Para laura: depois adiciona o centexto da historia neste print embaixo ⬇️
    print('Bem vindo a SHARK DUNGEON')

    for _ in range(num_salas):
        stats(jogador)
        direcao = input("\nVocê quer ir para a esquerda (1) ou para a direita (2)? ")
        evento = random.choice(["Loja", "Luta", "Tesouro"])
        if evento == "Loja":
            print("loja")
            loja()
        elif evento == "Tesouro":
            print("bau")
            bau()
        elif evento == "Luta":
            print("luta")
            luta()
game()

