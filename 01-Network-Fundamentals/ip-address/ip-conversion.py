def binario_para_decimal(binario):
    try:
        return int(binario, 2)
    except ValueError:
        return "Erro: Por favor, insira um número binário válido."

def decimal_para_binario(decimal):
    try:
        decimal = int(decimal)
        return bin(decimal)[2:]
    except ValueError:
        return "Erro: Por favor, insira um número decimal válido."

def main():
    print("Escolha a operação:")
    print("1) Conversão Binário para Decimal")
    print("2) Conversão Decimal para Binário")
    
    operacao = input("Digite o número da operação desejada: ")
    
    if operacao not in ["1", "2"]:
        print("Erro: Selecione uma operação válida.")
        return
    
    numero = input("Insira o número a ser convertido: ")
    
    if operacao == "1":
        resultado = binario_para_decimal(numero)
    elif operacao == "2":
        resultado = decimal_para_binario(numero)
    
    print("Resultado: ", resultado)

if __name__ == "__main__":
    main()
