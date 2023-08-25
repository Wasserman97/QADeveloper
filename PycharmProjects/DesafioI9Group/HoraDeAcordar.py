import time
import datetime
import ctypes
import configparser


def exibir_mensagem(mensagem):
    ctypes.windll.user32.MessageBoxW(0, mensagem, "Alarme", 1)


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    horario_config = config['hora']['horario']
    mensagem = config['mensagem']['texto']

    while True:
        horario_atual = datetime.datetime.now().time()
        horario = datetime.datetime.strptime(horario_config, '%H:%M').time()

        if horario_atual.hour == horario.hour and horario_atual.minute == horario.minute:
            exibir_mensagem(mensagem)

        time.sleep(10)


if __name__ == "__main__":
    main()

