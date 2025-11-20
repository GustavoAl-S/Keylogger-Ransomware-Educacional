from cryptography.fernet import Fernet
import os

def carregarChave():
    return open("chave.key", "rb").read()

def descriptografarArquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    
    dadosDescriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dadosDescriptografados)

def encontrarArquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ran.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
    chave = carregarChave()
    arquivos = encontrarArquivos("test_files")
    for arquivo in arquivos:
        descriptografarArquivo(arquivo, chave)
    print("Arquivos restaurados")

if __name__=="__main__":
    main()