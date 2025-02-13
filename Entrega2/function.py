import json
import sys, requests

# Função para retornar o comando que foi Digitado.

def retornar(comando):

    if comando == '#HOSTS': return 'Os Hosts enviarão situação on line, hostname, IP e Usuário logado.'
    elif comando == '#HOST:IP': return ' O Host correspondente ao IP enviará situação on line, hostname, IP e Usuário logado.'
    elif comando == '#SISTEM': return ' Os Hosts enviarão Informações de Hardware: CPU, Memória,Disco,Sistema Operacional.'
    elif comando == '#SISTEM:IP': return 'O Host correspondente ao IP enviará Informações de Hardware:CPU, Memória,Disco,Sistema Operacional.'
    elif comando == '#PROGR': return 'Os Hosts enviarão listagem dos programas instalados.'
    elif comando == '#PROGR:IP': return 'O Host correspondente ao IP envigará listagem dos programas instalados.'
    elif comando == '#NAVEG': return 'Os Hosts enviarão histórico de naveação nos navegadores Chrome, Firefox, Microsoft Edge, Opera e Safari.'
    elif comando == '#NAVEG:IP': return 'O Host correspondente ao IP enviará histórico de navegação nos navegadores Chrome, Firefox, Microsoft Edge, Opera e Safari.'
    elif comando == '#LOGIN': return 'Os Hosts enviarão (Home, UID, GID e Shell Padrão).'
    elif comando == '#LOGIN:IP': return 'O Host correspondente ao IP enviará (Home, UID, GID e Shell Padrão).'
    elif comando == '#ONLINE': return ' Lista agentes on line, trazendo as informações: IP, nome do HOST, usuário logado e o tempo que o agente está on-line.'
    elif comando == '#INIT': return ' Apresenta a msg_inicial com os Comandos Válidos'



# Função para verificar o texto que foi digitado e dar um retorno correspondente na def retornar()

def verificar(mensagem, chat_id, url_base):
    msg_inicial = ('Olá, seja bem vindo ao Juniorngm_Bot !\n\n'
                            'O que você deseja? comandos:\n\n'
                    
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

    try:
        digitado = mensagem['message']['text']; digitado = digitado.lower()
        if digitado in ['#HOSTS', '#HOST:IP', '#SISTEM', '#SISTEM:IP', '#PROGR', '#PROGR:IP','#NAVEG','#NAVEG:IP','#LOGIN','#LOGIN:IP','#ONLINE']:
            return retornar(digitado)
        elif digitado == '#INIT': return msg_inicial
        else: return 'Oops . . . !   \n\n  Comando Inválido, digite "#INIT" para ver os Comandos Válidos.'
    except KeyError:
        return 'Comando Inválido: (\n insira um comando válido ou digite "#INIT" para visualizar os Comandos Válidos'



# Função para Obter as Mensagens Enviadas ao Bot.

def recv_mensagens(update_id, url_base):
    link = f'{url_base}getUpdates?timeout=100'
    if update_id:
        link = f'{link}&offset={update_id + 1}'
    resultado = requests.get(link)
    try:
        data = json.loads(resultado.content); return data.get('result', [])
    except json.JSONDecodeError: return []



# Funçãp para responder as mensagens recebidas.

def respondendo(resposta,chat_id,url_base):
     link_envio = f'{url_base}sendMessage?chat_id={chat_id}&text={resposta}'
     requests.get(link_envio)
