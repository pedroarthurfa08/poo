def cal(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "Erro, divisão por zero não permitida"
    else:
        return "Operação Invalida"
def main():

    while True:
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            op = input("Digite a operação: ")
            if op =='q':
                print("")
                break
            
            resultado = cal(op, n1, n2)
            print(f'')
        except ValueError:
            print("")
            
if __name__ == '__main__':
    main()