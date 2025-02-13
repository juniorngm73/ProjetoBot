import socket

HOST_IP   = 'localhost'    # Definindo o IP do servidor
HOST_PORT = 50000          # Definindo a porta do servidor
PAGE_CODE = 'utf-8'        # Definindo o código da página


# Criando o socket TCP
socketCliente = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Endereço e porta do servidor
addressServer = (HOST_IP, HOST_PORT)

# Conectando ao servidor
socketCliente.connect(addressServer)

print('\nServidor TCP Inicializado ...\nPressione Ctrl+C para interromper...\n')

while True:
   try:
      mensagem = socketCliente.recv(1024)   # Digitando a mensagem a ser enviada
      if not mensagem:
         break

      # Se a Conexão for fechada pelo servidor
      print(f'Mensagem do Servidor:{mensagem.decode(PAGE_CODE)}')

      # Enviando resposta para o servidor
      resposta = ' Lista : On line, Hostname, IP e Usuário logado. '
      if resposta.lower() == 'exit':
         break

      socketCliente.send(resposta.encode(PAGE_CODE))

   except KeyboardInterrupt:
      print('\nCliente encerrado pelo Usuário....')
      break

# Fechando Conexão com o Servidor
socketCliente.close()