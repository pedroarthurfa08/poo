'''import random

class Jogo:

    escolha = None
    usuario = None
    computador = None

    def __init__(self, escolha, usuario, computador):
        self.escolha = escolha
        self.usuario = usuario
        self.computador = computador

    def escolha_usuario(self):
        if self.escolha in ["pedra", "papel", "tesoura"]:
            return self.escolha
        elif self.escolha == "sair":
            return None
        else:
            print("Resposta Inválida!")
            return None

    def escolha_computador(self):
        return random.choice(["pedra", "papel", "tesoura"])

    def vencedor(self, usuario, computador):
        if usuario == computador:
            return "Empate!"
        elif (usuario == "pedra" and computador == "tesoura") or \
             (usuario == "tesoura" and computador == "papel") or \
             (usuario == "papel" and computador == "pedra"):
            return "Você venceu!"
        else:
            return "Você perdeu e o PC ganhou!"

def main():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    while True:
        escolha = input("Escolha entre 'pedra', 'papel', 'tesoura' ou 'sair' para encerrar: ")
        mi_joguinho = Jogo(escolha, usuario, computador)
        
        usuario = mi_joguinho.escolha_usuario()
        if usuario is None:
            print("Encerrando o jogo...")
            break

        computador = mi_joguinho.escolha_computador()
        print(f"Computador escolheu: {computador}")
        
        resultado = mi_joguinho.vencedor(usuario, computador)
        print(resultado)

main()
'''

import random

class Jogo:
    def __init__(self, escolha=None, usuario=None, computador=None):
        self.escolha = escolha
        self.usuario = usuario
        self.computador = computador

    def escolha_usuario(self):
        if self.escolha in ["pedra", "papel", "tesoura"]:
            return self.escolha
        elif self.escolha == "sair":
            return None
        else:
            print("Resposta Inválida!")
            return None

    def escolha_computador(self):
        return random.choice(["pedra", "papel", "tesoura"])

    def vencedor(self, usuario, computador):
        if usuario == computador:
            return "Empate!"
        elif (usuario == "pedra" and computador == "tesoura") or \
             (usuario == "tesoura" and computador == "papel") or \
             (usuario == "papel" and computador == "pedra"):
            return "Você venceu!"
        else:
            return "Você perdeu e o PC ganhou!"

def main():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    while True:
        escolha = input("Escolha entre 'pedra', 'papel', 'tesoura' ou 'sair' para encerrar: ")
        mi_joguinho = Jogo(escolha)
        
        usuario = mi_joguinho.escolha_usuario()
        if usuario is None:
            print("Encerrando o jogo...")
            break

        computador = mi_joguinho.escolha_computador()
        print(f"Computador escolheu: {computador}")
        
        resultado = mi_joguinho.vencedor(usuario, computador)
        print(resultado)

main()
