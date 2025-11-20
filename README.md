# Keylogger-Ransomware-Educacional

ESTES SCRIPTS SÃO APENAS PARA FINS EDUCACIONAIS E DE PESQUISA

Este projeto foi desenvolvido para fins totalmente educacionais, com o intuito de aprender como funcionam um ransomware e um keylogger na pratica e assim obter conhecimento sobre como se proteger e se conscientizar sobre seugrança cibernetica. Todos os malwares foram testados em um ambiente totalmente controlado e utilizados em dados ficticios para testes. No keylogger alem da sua implementação basica de capturar a entrada do teclado, o modificamos para rodar em segundo plano e adicionamos um envio desses logs capturados para um e-mail.

# Ransomware

Testes do ransomware:

Arquivo de teste antes da criptografia:


<img width="418" height="153" alt="Image" src="https://github.com/user-attachments/assets/ff7eafd7-8b38-4cc5-b92e-2ef33eb2dffc" />

Após criptografar:

<img width="1608" height="155" alt="Image" src="https://github.com/user-attachments/assets/c11eefa9-be56-4269-9ad8-9a9d43d13f19" />

# Keylogger Educacional

Keylogger é um malware que tem como objeto capturar toda entrada do teclado do alvo. Entradas que podem ser letras, espaços, numeros, etc.
E atraves dessa ferramentas, se for utilizada de forma maliciosa, o atacante pode capturar logins de senhas, e-mails, dados confidenciais e diversas outras informações importantes que forem digitadas no teclado da vitima.

Meu objetivo foi criar um keylogger de forma educacional para entender como funciona esse malware e como se proteger na pratica dele. 

Para preparar seu ambiente, instale a biblioteca pynput, para monitorar o teclado e assim reaja quando uma determinado tecla for clicada.

Cada interação do usuário sera salva em um arquivo .txt na ordem sequencial que foi digitada. 
Para uma melhor organização e leitura do arquivo .txt usamos o conjunto IGNORAR que recebe algumas teclas que serão ignoradas durante a gravação, isso faz com o texto nao fique quebrado e confuso quando formos realizar a sua leitura.

Após a implementação do keylogger basico funcionando, utilizei a biblioteca secure-smtlib e configurei para que logs das entradas fossem enviadados por e-mail a cada 60 segundos.

Logs recebidos pelo e-mail:

<img width="927" height="187" alt="Image" src="https://github.com/user-attachments/assets/1a1aa90d-80d5-468f-acce-b946e293d220" />


# Como se Proteger

Por mais que seja a coisa mais basica a se fazer, e justamente por isso as vezes é deixado de lado, é manter os firewall e antivirus atualizados.
Inclusive, pode acontecer de caso voce for tentar rodar os codigos do repositorio, o antivirus do seu computador bloquea-los. Ou seja por mais que seja simples é muito eficaz verificar e manter seus antivirus atualizados porque eles sao a primeira camada de segurança do seu sistema.

Porem o antivirus nao faz tudo sozinho, por isso outra medidas é utilizar ferramnatas para monitorar processos suspeitos, bloqueando atividades suspeitas que estejam criptografando dados por exemplo.

Outro metodo, e um dos mais importantes é a concientização sobre phishing. O ponto mais fraco da segurança é o ser humano, por isso deve se educar as pessoas sobre a engenharia social e ensina-las a não clicar em links suspeitos, pdfs falsos, e-mails chamativos, etc.

Contra o Ransonware, além das praticas acima, busque manter um backups autaticos e testar sua recuperação reguralamente.

