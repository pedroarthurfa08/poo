class Veiculo:
    def __init__(self, placa, marca, modelo, ano, cor = "não especifica", proprietário = "não especifica", quilometragem = 0):
        # Atributos obrigatório
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        # Atributos não obrigatórios
        self.cor = cor
        self.proprietário = proprietário
        self.quilometragem = quilometragem
    
    def exibir_infomacoes(self):
        # Mostra informações do veículo
        print(f'Placa: {self.placa}')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Cor: {self.cor}')
        print(f'Proprietário: {self.proprietário}')
        print(f'Quilometragem: {self.quilometragem}')

    def atualiar_quilometragem(self, nova_quilometragem):
        # Atualiza a quilometragem do veículo
        self.nova_quilometragem = nova_quilometragem

def main():
    cadastro = Veiculo()
    while True:
        placa = input(f'Insira placa do veículo: ')
        marca = input(f'Insira marca do veículo: ')
        modelo = input(f'Insira modelo do veículo: ')
        ano = int(input(f'Insira ano do veículo: '))
        cor = input(f'Insira cor do veículo (ou pressione ENTER para não especificar): ')
        proprietario = input(f'Insira proprietário do veículo (ou pressione ENTER para não especificar): ')
        quilometragem = int(input(f'Insira quilometragem do veículo (ou pressione ENTER para não especificar): '))
        cadastro = Veiculo(placa, marca, modelo, ano, cor, proprietario, quilometragem)
main()