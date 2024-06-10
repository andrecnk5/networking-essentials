
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
    octetos = binario.split('.')
    decimal = []
    for octeto in octetos:
        decimal.append(str(int(octeto, 2)))
    return '.'.join(decimal)

def decimal_para_binario(decimal):
    octetos = decimal.split('.')
    binario = []
    for octeto in octetos:
        binario.append(format(int(octeto), '08b'))
    return '.'.join(binario)

# Exemplos de uso
ip_binario = "11000000.10101000.00000001.00000001"
ip_decimal = "192.168.1.1"

print(f"Binário para Decimal: {binario_para_decimal(ip_binario)}")
print(f"Decimal para Binário: {decimal_para_binario(ip_decimal)}")
```

## Implementação em JavaScript

Para automatizar essas conversões, você pode usar o seguinte script JavaScript:

```javascript
function binarioParaDecimal(binario) {
    const octetos = binario.split('.');
    const decimal = octetos.map(octeto => parseInt(octeto, 2).toString());
    return decimal.join('.');
}

function decimalParaBinario(decimal) {
    const octetos = decimal.split('.');
    const binario = octetos.map(octeto => ('00000000' + parseInt(octeto, 10).toString(2)).slice(-8));
    return binario.join('.');
}

// Exemplos de uso
const ipBinario = "11000000.10101000.00000001.00000001";
const ipDecimal = "192.168.1.1";

console.log(`Binário para Decimal: ${binarioParaDecimal(ipBinario)}`);
console.log(`Decimal para Binário: ${decimalParaBinario(ipDecimal)}`);
```

Com esses scripts, você pode facilmente converter endereços IPs entre os formatos binário e decimal.
