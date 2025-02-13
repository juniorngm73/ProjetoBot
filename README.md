INTRODUÇÃO

O projeto trata da criação de um BOT no TELEGRAM, com a finalidade de realizar uma comunicação com Hosts através de um Servidor. Basicamente o comando será ativado no TELEGRAM e segue para o Servidor, onde será tratado afim de identificar o destino; para em seguida realizar o envio, seja para um ou mais Hosts. A conexão entre cliente e servidor será através de um Socket TCP, tendo em vista o mesmo ser orientado a conexão. Serão implementados os seguintes Comandos:

COMANDOS

#HOSTS = Será encaminhado aos HOSTS. Os Hosts responderão enviando situação on line, hostname, IP e Usuário logado.

#HOST:IP = Será encaminhado ao HOST correspondente ao IP. O Host responderá enviando situação on line, hostname, IP e Usuário logado.

#SISTEM = Será encaminhado aos HOSTS. Os Hosts responderão enviando informações do Hardware como: CPU, Memória, Disco, Sistema Operacional.

#SISTEM:IP = Será encaminhado ao HOST correspondente ao IP. O Host responderá enviando informações do Hardware como: CPU, Memória, Disco, Sistema Operacional.

#PROGR = Será encaminhado aos HOSTS. Os Hosts responderão enviando listagem dos programas instalados.

#PROGR:IP = Será encaminhado ao HOST correspondente ao IP. O Host responderá enviando a listagem dos programas instalados.

#NAVEG = Será encaminhado aos HOSTS. Os Hosts responderão enviando o histórico de navegação nos navegadores Chrome, Firefox, Microsoft Edge, Opera e Safari.

#NAVEG:IP = Será encaminhado ao HOST correspondente ao IP. O Host responderá enviando o histórico de navegação nos navegadores Chrome, Firefox, Microsoft Edge, Opera e Safari.

#LOGIN = Será encaminhado aos HOSTS solicitando informações detalhadas do usuário que está logado.  Os Hosts responderão (Home, UID,GID e Shell Padrão)

#LOGIN:IP = Será encaminhado ao HOST correspondente ao IP solicitando informações detalhadas do usuário que está logado.  O Host responderá (Home, UID,GID e Shell Padrão).

#ONLINE = Lista agentes on line, trazendo as informações: IP, nome do HOST, usuário logado e o tempo que o agente está on-line.

#INIT = Apresenta a msg_inicial com os Comandos Válidos.
