class Calculadora:
    n1 = 0
    n2 = 0
    op = None

def calcular(self, n1, n2, op):

    self.n1 = n1
    self.n2 = n2
    self.op = op


    if self.op == "+":
        return self.n1 + self.n2
    elif self.op == "-":
        return self.n1 - self.n2
    elif self.op == "*":
        return self.n1 * self.n2
    elif self.op == '/':
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
             return("Erro, operação por zero não permitida")
    else:
            return "Operação Inválida"

def main():
    while True:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        op = (input("Digite a operação: "))
        
        if op == 'q':
            print("Encerrando")
            break
        resultado = calcular(n1, n2, op)
        print(f'{n1} {op} {n2} = {resultado}')
        resp = str.upper(input("Continua S/N"))
        if resp == 'N':
            break
main()