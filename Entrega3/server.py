import threading, socket, requests,function

##########################################################################
HOST_SERVER = 'localhost'
PORT = 55000
PROMPT = 'insira sua mensagem >> '
SERVER = '0.0.0.0'
CODE_PAGE = 'utf-8'
############################################################################

clients = []

def main():
    telegram_thread = threading.Thread(target=telegrambot)
    telegram_thread.start()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((SERVER, PORT))
        server.listen(5)
        print("Recebendo conexões em: ", (SERVER, PORT))
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept()
        print(f"\nConexão de: {addr}\n")
        clients.append(client)

        # Inicia uma thread para interação com o cliente
        thread = threading.Thread(target=cliInteraction, args=[client, addr])
        thread.start()

def cliInteraction(client, addr):
    while True:
        try:
            msg = client.recv(512)
            broadcast(msg, client, addr)
        except:
            print(f"\nUsuário {addr} desconectado.\n")
            deleteClient(client)
            break

def broadcast(msg, client, addr):
    msg = f"{addr}: {msg.decode('utf-8')}"
    print(msg)
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg.encode('utf-8'))
            except:
                deleteClient(clientItem)

def deleteClient(client):
    clients.remove(client)

def telegrambot():
    token = "6731238648:AAF0nfYufZRsi9MgkGor1AcCoaxol8jJ9tk"
    strURL = f"https://api.telegram.org/bot{token}/"
    update_id = None
    arquivo_registros = "registros.json"
    registros = function.carregar_registros(arquivo_registros)

    while True:
        try:
            atualizacao = function.obter_atualizacao(update_id, strURL)
            mensagens = atualizacao["result"]
            for mensagem in mensagens:
                update_id = mensagem['update_id']
                chat_id = mensagem['message']['from']['id']
                try:comando = mensagem['message']['text']
                except:comando = "..."
                resposta = function.criar_resposta(comando, chat_id, registros)
                link_de_envio = f"{strURL}sendMessage?chat_id={chat_id}&text={resposta}"
                requests.get(link_de_envio)
        except OSError:
            print("Ocorreu um erro... ", OSError)
        function.guardar_registros(registros, arquivo_registros)

main()