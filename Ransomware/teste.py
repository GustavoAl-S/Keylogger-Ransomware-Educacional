from cryptography.fernet import Fernet
import os

# Gerar uma chave
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Criptografar e descriptografar
texto = b"Minha mensagem secreta"
texto_criptografado = cipher_suite.encrypt(texto)
texto_descriptografado = cipher_suite.decrypt(texto_criptografado)

print(f"Original: {texto}")
print(f"Criptografado: {texto_criptografado}")
print(f"Descriptografado: {texto_descriptografado}")