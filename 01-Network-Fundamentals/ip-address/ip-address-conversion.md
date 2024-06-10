
# Conversão de Endereços IPs: Binário para Decimal e Decimal para Binário

Este guia explica como converter endereços IPs entre os formatos binário e decimal, com exemplos e implementações em Python e JavaScript.

## Conversão de Binário para Decimal

Um endereço IP no formato binário é geralmente representado por quatro octetos (grupos de 8 bits). Por exemplo:
```
11000000.10101000.00000001.00000001
```
Para converter esse endereço para o formato decimal, você deve converter cada octeto individualmente.

**Passos:**
1. Divida o endereço IP em quatro octetos: `11000000`, `10101000`, `00000001`, `00000001`.
2. Converta cada octeto de binário para decimal.

### Exemplo de Conversão
Vamos converter o endereço binário `11000000.10101000.00000001.00000001` para decimal.

| Octeto Binário | Conversão   | Decimal |
| -------------- | ----------- | ------- |
| 11000000       | 1×2^7 + 1×2^6 + 0×2^5 + 0×2^4 + 0×2^3 + 0×2^2 + 0×2^1 + 0×2^0 | 192     |
| 10101000       | 1×2^7 + 0×2^6 + 1×2^5 + 0×2^4 + 1×2^3 + 0×2^2 + 0×2^1 + 0×2^0 | 168     |
| 00000001       | 0×2^7 + 0×2^6 + 0×2^5 + 0×2^4 + 0×2^3 + 0×2^2 + 0×2^1 + 1×2^0 | 1       |
| 00000001       | 0×2^7 + 0×2^6 + 0×2^5 + 0×2^4 + 0×2^3 + 0×2^2 + 0×2^1 + 1×2^0 | 1       |

**Resultado Final:**
```
192.168.1.1
```

## Conversão de Decimal para Binário

Para converter um endereço IP no formato decimal para binário, você deve converter cada octeto decimal individualmente em um octeto binário.

### Exemplo de Conversão
Vamos converter o endereço decimal `192.168.1.1` para binário.

**Passos:**
1. Divida o endereço IP em quatro octetos: `192`, `168`, `1`, `1`.
2. Converta cada octeto de decimal para binário.

| Octeto Decimal | Conversão       | Binário   |
| -------------- | --------------- | --------- |
| 192            | 192/2 = 96 (resto 0), 96/2 = 48 (resto 0), 48/2 = 24 (resto 0), 24/2 = 12 (resto 0), 12/2 = 6 (resto 0), 6/2 = 3 (resto 0), 3/2 = 1 (resto 1), 1/2 = 0 (resto 1)  | 11000000 |
| 168            | 168/2 = 84 (resto 0), 84/2 = 42 (resto 0), 42/2 = 21 (resto 0), 21/2 = 10 (resto 1), 10/2 = 5 (resto 0), 5/2 = 2 (resto 1), 2/2 = 1 (resto 0), 1/2 = 0 (resto 1) | 10101000 |
| 1              | 1/2 = 0 (resto 1)                                                                                                 | 00000001 |
| 1              | 1/2 = 0 (resto 1)                                                                                                 | 00000001 |

**Resultado Final:**
```
11000000.10101000.00000001.00000001
```

## Exemplos de Conversão

**1. Binário para Decimal**
- Binário: `11000000.10101000.00000001.00000001`
- Decimal: `192.168.1.1`

**2. Decimal para Binário**
- Decimal: `10.0.0.1`
- Binário: `00001010.00000000.00000000.00000001`

## Implementação em Python

Para automatizar essas conversões, você pode usar o seguinte script Python:

```python
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

```

## Implementação em JavaScript

Para automatizar essas conversões, você pode usar o seguinte script JavaScript:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor Binário/Decimal</title>
    <script>
        function convert() {
            const operation = document.getElementById("operation").value;
            const number = document.getElementById("number").value;
            let result = '';

            if (operation === "1") {
                // Binário para Decimal
                result = parseInt(number, 2);
                if (isNaN(result)) {
                    result = "Por favor, insira um número binário válido.";
                }
            } else if (operation === "2") {
                // Decimal para Binário
                const decimalNumber = parseInt(number, 10);
                if (isNaN(decimalNumber)) {
                    result = "Por favor, insira um número decimal válido.";
                } else {
                    result = decimalNumber.toString(2);
                }
            } else {
                result = "Selecione uma operação válida.";
            }

            document.getElementById("result").textContent = "Resultado: " + result;
        }
    </script>
</head>
<body>
    <h1>Conversor Binário/Decimal</h1>
    <label for="operation">Escolha a operação:</label>
    <select id="operation">
        <option value="">Selecione</option>
        <option value="1">Conversão Binário para Decimal</option>
        <option value="2">Conversão Decimal para Binário</option>
    </select>
    <br><br>
    <label for="number">Insira o número:</label>
    <input type="text" id="number">
    <br><br>
    <button onclick="convert()">Converter</button>
    <br><br>
    <p id="result">Resultado: </p>
</body>
</html>

```

Com esses scripts, você pode facilmente converter endereços IPs entre os formatos binário e decimal.
