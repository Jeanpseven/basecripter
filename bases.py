from cryptography.fernet import Fernet
import hashlib

def encrypt_text(text, algorithm):
    if algorithm == "aes":
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(text.encode())
        return encrypted_text.decode()
    elif algorithm == "md5":
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        return md5_hash
    elif algorithm == "sha1":
        sha1_hash = hashlib.sha1(text.encode()).hexdigest()
        return sha1_hash
    elif algorithm == "sha256":
        sha256_hash = hashlib.sha256(text.encode()).hexdigest()
        return sha256_hash
    else:
        return "Algoritmo de criptografia inválido"

def decrypt_text(text, algorithm):
    if algorithm == "aes":
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        decrypted_text = cipher_suite.decrypt(text.encode())
        return decrypted_text.decode()
    else:
        return "Algoritmo de criptografia inválido"

# Menu de escolha
print("Escolha uma opção:")
print("1. Criptografar")
print("2. Descriptografar")
choice = input("Digite o número da opção desejada: ")

if choice == "1":
    text = input("Digite o texto a ser criptografado: ")
    algorithm = input("Escolha o algoritmo (aes, md5, sha1, sha256): ")
    encrypted_text = encrypt_text(text, algorithm)
    print("Texto criptografado:", encrypted_text)
elif choice == "2":
    text = input("Digite o texto a ser descriptografado: ")
    algorithm = input("Escolha o algoritmo (aes): ")
    decrypted_text = decrypt_text(text, algorithm)
    print("Texto descriptografado:", decrypted_text)
else:
    print("Opção inválida")
