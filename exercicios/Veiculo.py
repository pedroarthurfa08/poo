class Veiculo:
    def __init__(self, placa, marca, modelo, ano, cor = "não especifica", proprietário = "não especifica", quilometragem = 0):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

        self.cor = cor
        self.proprietário = proprietário
        self.quilometragem = quilometragem
    
    def exibir_informacoes(self):
        print(f'Placa: {self.placa}')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Cor: {self.cor}')
        print(f'Proprietário: {self.proprietário}')
        print(f'Quilometragem: {self.quilometragem}')

    def atualizar_quilometragem(self, nova_quilometragem):
        if nova_quilometragem >= self.quilometragem:
            self.quilometragem = nova_quilometragem
            print("Quilometragem atualziada.")
        else:
            return "Erro, tente novamente mais tarde, obrigado."

placa = input("Digite a placa do veículo: ")
marca = input("Digite a marca do veículo: ")
modelo = input("Digite o modelo do veículo: ")
ano = int(input("Digite o ano de fabricação do veículo: "))
cor = input("Digite a cor do veículo (ou deixe em branco para 'Não especificada'): ") or "Não especificada"
proprietario = input("Digite o nome do proprietário (ou deixe em branco para 'Não especificado'): ") or "Não especificado"
quilometragem = int(input("Digite a quilometragem atual (ou deixe em branco para 0): ") or 0)

def main():
    veiculo = Veiculo(placa, marca, modelo, ano, cor, proprietario, quilometragem)

    veiculo.exibir_informacoes()

    nova_quilometragem = int(input("Digite a nova quilometragem para atualizar: "))
    veiculo.atualizar_quilometragem(nova_quilometragem)
    veiculo.exibir_informacoes()
main()