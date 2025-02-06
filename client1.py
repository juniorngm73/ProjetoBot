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

print('\nCliente TCP conectado ao servidor...\n')

while True:
   try:
      # Recebendo a pergunta do servidor
      pergunta = socketCliente.recv(1024).decode(PAGE_CODE)
      print(f'Pergunta do servidor: {pergunta}')

      # Respondendo à pergunta
      resposta = input('Responda ao Servidor: ')
      socketCliente.send(resposta.encode(PAGE_CODE))

      # Recebendo mensagem de volta do servidor
      mensagem_volta = socketCliente.recv(1024).decode(PAGE_CODE)
      print (f'Mensagem do servidor: {mensagem_volta} ')

   except KeyboardInterrupt:
      socketCliente.send('SAIR'.encode(PAGE_CODE))
      print('\nCliente encerrado pelo usuário...')
      break
   except ConnectionResetError:
       print("\nConexão com o servidor foi perdida.")
       break
   except Exception as e:
       print(f"\nOcorreu um erro: {e}")
       break

# Fechando o socket
socketCliente.close()