import requests

# Get chat ID
def get_chat_id(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['result']:
            for update in reversed(data['result']):
                if 'message' in update and 'chat' in update['message']:
                    return update['message']['chat']['id']
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error getting updates: {e}")
        return None
    except (KeyError, TypeError) as e:
        print(f"Error parsing updates: {e}. Raw data: {data}")
        return None

# Send a message
def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, data)
        response.raise_for_status()
        print("Message sent successfully!")

    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")


token = "7216647399:AAEF9mZLGifbRIq3vRE08FUK-L2em_bI8y4"
msg = ('Olá, Seja Bem Vindo ao Juniorngm_Bot !\n\n'
                            'O que você deseja? Seguem os Comandos:\n\n'
                    
                            '#HOSTS --> Situação on line, hostname, IP e Usuário logado.\n'
                            '#HOST:IP --> Situação on line, hostname, IP e Usuário logado, correspondente ao IP.\n'
                            '#SISTEM --> Informações de Hardware: CPU, Memória,Disco,Sistema Operacional.\n'
                            '#SISTEM:IP --> Informações de Hardware: CPU, Memória,Disco,Sistema Operacional,correspondente ao IP.\n'
                            '#PROGR --> listagem dos programas instalados.\n' 
                            '#PROGR:IP --> listagem dos programas instalados,correspondente ao IP.\n' 
                            '#NAVEG --> Histórico de navegação nos navegadores Chrome, Firefox, Microsoft Edge, Opera e Safari.\n'
                            '#NAVEG:IP --> Histórico de navegação nos navegadores Chrome, Firefox,  Microsoft Edge, Opera e Safari, correspondente ao IP.\n'
                            '#LOGIN --> lista (Home, UID, GID e Shell Padrão).\n'
                            '#LOGIN:IP --> lista (Home, UID, GID e Shell Padrão), correspondente ao IP.\n'
                            '#ONLINE --> Lista agentes on line (IP, nome do HOST, usuário logado e o tempo que o agente está on-line)\n')


# Função para responder às mensagens
def responder(token, chat_id, mensagem):
    # Aqui você pode adicionar a lógica para interpretar a mensagem
    # e decidir qual resposta enviar.
    # Por exemplo, você pode usar condicionais para verificar
    # se a mensagem contém alguma palavra-chave específica
    # e enviar uma resposta correspondente.

    if "#HOSTS" in mensagem:
        resposta = "Situação on line, hostname, IP e Usuário logado."
    elif "#HOST:" in mensagem:
        ip = mensagem.split(":")[1]
        resposta = f"Situação on line, hostname, IP e Usuário logado para o IP {ip}."
    elif "#SISTEM" in mensagem:
        resposta = "Informações de Hardware: CPU, Memória, Disco, Sistema Operacional."
    elif "#SISTEM:" in mensagem:
        ip = mensagem.split(":")[1]
        resposta = f"Informações de Hardware: CPU, Memória, Disco, Sistema Operacional para o IP {ip}."
    elif "#PROGR" in mensagem:
        resposta = "Listagem dos programas instalados."
    elif "#PROGR:" in mensagem:
        ip = mensagem.split(":")[1]
        resposta = f"Listagem dos programas instalados para o IP {ip}."
    elif "#NAVEG" in mensagem:
        resposta = "Histórico de navegação nos navegadores Chrome, Firefox, Microsoft Edge, Opera e Safari."
    elif "#NAVEG:" in mensagem:
        ip = mensagem.split(":")[1]
        resposta = f"Histórico de navegação nos navegadores Chrome, Firefox, Microsoft Edge, Opera e Safari para o IP {ip}."
    elif "#LOGIN" in mensagem:
        resposta = "Lista (Home, UID, GID e Shell Padrão)."
    elif "#LOGIN:" in mensagem:
        ip = mensagem.split(":")[1]
        resposta = f"Lista (Home, UID, GID e Shell Padrão) para o IP {ip}."
    elif "#ONLINE" in mensagem:
        resposta = "Lista agentes on line (IP, nome do HOST, usuário logado e o tempo que o agente está on-line)."
    else:
        resposta = msg  # Mensagem padrão de boas-vindas

    send_message(token, chat_id, resposta)

# Loop principal para receber e responder mensagens
def main():
    token = "7216647399:AAEF9mZLGifbRIq3vRE08FUK-L2em_bI8y4"
    url = f"https://api.telegram.org/bot{token}/"

    while True:
        updates = requests.get(url + "getUpdates").json()

        if updates['result']:
            for update in updates['result']:
                if 'message' in update and 'text' in update['message']:
                    mensagem = update['message']['text']
                    chat_id = update['message']['chat']['id']

                    responder(token, chat_id, mensagem)

                    # Atualiza o offset para não receber as mesmas mensagens novamente
                    update_id = update['update_id']
                    requests.get(url + f"getUpdates?offset={update_id + 1}")


if __name__ == "__main__":
    main()


chat_id = get_chat_id(token)
if chat_id:
    print(f"Chat ID: {chat_id}")
    send_message(token, chat_id, msg)
else:
    print("Could not find a chat ID.")



