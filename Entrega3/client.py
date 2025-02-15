import threading, socket, time
########################################################################
HOST_SERVER = 'localhost'
PORT = 55000
PROMPT = 'insira sua mensagem >> '
SERVER = '0.0.0.0'
CODE_PAGE = 'utf-8'
#######################################################################


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST_SERVER, PORT))
    except:
        return '\nnão foi possível se conectar ao servidor!\n'

    print('conexão bem sucedida\n')
    username = input('insira um nome de usuário pelo qual você vai ser identificado: ');
    print()

    recebendo = threading.Thread(target=receber_msg, args=[client])
    enviando = threading.Thread(target=enviar_msg, args=[client, username])

    recebendo.start();
    enviando.start()
    recebendo.join();
    enviando.join()


def receber_msg(client):
    while True:
        try:
            msg = client.recv(1024).decode(CODE_PAGE)
            print('\n' + msg);
            print('\n' + PROMPT, end='')
        except:
            print('\nnão foi possível permanecer conectado no servidor!\n')
            client.close();
            break


def enviar_msg(client, username):
    while True:
        try:
            msg = input(PROMPT)
            if msg == '!exit':
                print('\na conexão será encerrada . . .\n')
                client.send(f'@{username} encerrou a conexão . . .\n'.encode(CODE_PAGE))
                time.sleep(10)
                client.close();
                break
            else:
                client.send(f'@{username}: {msg}'.encode(CODE_PAGE))
        except:
            return


main()