from datetime import datetime

numer0_cartao = {}

class CartaoEstacionamento:
    def __init__(self, numero_cartao, data_hora_entrada, status_cartao, data_hora_saida, valor_total):
        self.numero_cartao = numero_cartao
        