def dec2bin(decimal):
    return bin(decimal)[2:]

def bin2dec(binario):
    return int(binario, 2)

def dec2hex(decimal):
    return hex(decimal)[2:]

def hex2dec(hexadecimal):
    return int(hexadecimal, 16)

def bin2hex(binario):
    decimal = bin2dec(binario)
    return dec2hex(decimal)

def hex2bin(hexadecimal):
    decimal = hex2dec(hexadecimal)
    return dec2bin(decimal)

def text2bin(texto):
    binario = ""
    for char in texto:
        binario += format(ord(char), '08b')
    return binario

def bin2text(binario):
    texto = ""
    for i in range(0, len(binario), 8):
        byte = binario[i:i+8]
        decimal = bin2dec(byte)
        texto += chr(decimal)
    return texto

def text2hex(texto):
    hexadecimal = ""
    for char in texto:
        hexadecimal += format(ord(char), '02x')
    return hexadecimal

def hex2text(hexadecimal):
    texto = ""
    for i in range(0, len(hexadecimal), 2):
        byte = hexadecimal[i:i+2]
        decimal = hex2dec(byte)
        texto += chr(decimal)
    return texto

# Exemplo de uso
opcao = input("Escolha uma opção:\n1. Decimal para binário\n2. Binário para decimal\n3. Decimal para hexadecimal\n4. Hexadecimal para decimal\n5. Binário para hexadecimal\n6. Hexadecimal para binário\n7. Texto para binário\n8. Binário para texto\n9. Texto para hexadecimal\n10. Hexadecimal para texto\n")

if opcao == "1":
    decimal = int(input("Digite o número decimal: "))
    binario = dec2bin(decimal)
    print("Binário:", binario)
elif opcao == "2":
    binario = input("Digite o número binário: ")
    decimal = bin2dec(binario)
    print("Decimal:", decimal)
elif opcao == "3":
    decimal = int(input("Digite o número decimal: "))
    hexadecimal = dec2hex(decimal)
    print("Hexadecimal:", hexadecimal)
elif opcao == "4":
    hexadecimal = input("Digite o número hexadecimal: ")
    decimal = hex2dec(hexadecimal)
    print("Decimal:", decimal)
elif opcao == "5":
    binario = input("Digite o número binário: ")
    hexadecimal = bin2hex(binario)
    print("Hexadecimal:", hexadecimal)
elif opcao == "6":
    hexadecimal = input("Digite o número hexadecimal: ")
    binario = hex2bin(hexadecimal)
    print("Binário:", binario)
elif opcao == "7":
    texto = input("Digite o texto: ")
    binario = text2bin(texto)
    print("Binário:", binario)
elif opcao == "8":
    binario = input("Digite o número binário: ")
    texto = bin2text(binario)
    print("Texto:", texto)
elif opcao == "9":
    texto = input("Digite o texto: ")
    hexadecimal = text2hex(texto)
    print("Hexadecimal:", hexadecimal)
elif opcao == "10":
    hexadecimal = input("Digite o número hexadecimal: ")
    texto = hex2text(hexadecimal)
    print("Texto:", texto)
else:
    print("Opção inválida.")
