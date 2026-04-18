# Keylogger-Ransomware-Educacional

ESTES SCRIPTS SÃO APENAS PARA FINS EDUCACIONAIS E DE PESQUISA

Este projeto foi desenvolvido para fins totalmente educacionais, com o intuito de aprender como funcionam um ransomware e um keylogger na prática e, assim, obter conhecimento sobre como se proteger e se conscientizar sobre segurança cibernética. Todos os malwares foram testados em um ambiente totalmente controlado e utilizados em dados fictícios para testes. No keylogger, além da sua implementação básica de capturar a entrada do teclado, o modificamos para rodar em segundo plano e adicionamos o envio desses logs capturados para um e-mail.

## Ransomware

Testes do ransomware:

Arquivo de teste antes da criptografia:


<img width="418" height="153" alt="Image" src="https://github.com/user-attachments/assets/ff7eafd7-8b38-4cc5-b92e-2ef33eb2dffc" />

Após criptografar:

<img width="1608" height="155" alt="Image" src="https://github.com/user-attachments/assets/c11eefa9-be56-4269-9ad8-9a9d43d13f19" />

# Keylogger Educacional

Um Keylogger é tipo de malware que tem como objetivo capturar toda entrada do teclado do alvo, incluindo letras, números e caracteres especiais. Através dessa ferramenta, caso utilizada de forma maliciosa, um atacante pode capturar credenciais de acesso, e-mails, dados confidenciais e diversas outras informações importantes que forem digitadas pela vítima.

Este projeto foi desenvolvido com fins estritamente educacionais para entender como funciona esse malware e como proteger-se contra essa ameaça na prática

## Preparação do ambiente:
Para preparar o ambiente, é necessário instalar a biblioteca pynput, utilizada para monitorar e reagir a cada tecla pressionada. Cada interação do usuário é salva em um arquivo .txt na ordem sequencial da digitação.
Para uma melhor organização e leitura do arquivo .txt, usamos o conjunto IGNORAR. Ele filtra teclas de controle (como comandos do sistema) que poderiam poluir o arquivo, garantindo que o texto final seja claro e contínuo.

Após a implementação do keylogger básico funcionando, utilizei a biblioteca secure-smtlib e a configurei para que logs das entradas fossem enviados por e-mail a cada 60 segundos.

# Como se Proteger

Uma das melhores praticas é manter a primeira camada de segurança do seu computador (antivirus e firewalls) sempre atualizados e ativos.
Inclusive, pode acontecer de caso voce for tentar rodar os codigos do repositorio, o antivirus do seu computador pode bloquea-los. 

No entanto, o antivírus não resolve tudo sozinho. É recomendável utilizar ferramentas complementares que monitorem o comportamento do sistema. Elas servem para identificar e interromper atividades estranhas em tempo real, como um programa tentando criptografar seus arquivos sem autorização.

Outro ponto crucial é a conscientização sobre o fator humano. Muitas vezes, a maior vulnerabilidade não está na máquina, mas em quem a utiliza. Por isso, é essencial treinar as equipes para identificar tentativas de "engenharia social", ensinando-as a desconfiar de links urgentes, arquivos em PDF de fontes desconhecidas ou e-mails com promessas excessivas.

