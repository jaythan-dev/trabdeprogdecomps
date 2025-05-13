import time
import threading
from datetime import datetime, timedelta

# Função para mostrar o relógio continuamente
def relogio():
    try:
        while True:
            agora = datetime.now()
            print(f"\r🕒 {agora.strftime('%d/%m/%Y %H:%M:%S')}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nVoltando ao menu...")

# Função do cronômetro
def cronometro():
    segundos = 0
    rodando = True

    print("\nIniciando cronômetro (pressione Ctrl+C para parar)")
    try:
        while True:
            print(f"\r⏱️ {segundos//3600:02}:{(segundos//60)%60:02}:{segundos%60:02}", end="")
            time.sleep(1)
            segundos += 1
    except KeyboardInterrupt:
        print("\nCronômetro pausado.")

# Função do timer
def timer():
    try:
        minutos = int(input("Digite o tempo em minutos para o timer: "))
        segundos = minutos * 60
        print(f"⏳ Timer iniciado por {minutos} minutos.")
        while segundos:
            print(f"\r⏳ Restando: {segundos//60:02}:{segundos%60:02}", end="")
            time.sleep(1)
            segundos -= 1
        print("\n⏰ Tempo finalizado!")
    except ValueError:
        print("Entrada inválida.")

# Função do despertador
def despertador():
    horario = input("Digite o horário do alarme (HH:MM): ")
    try:
        agora = datetime.now()
        hora_alarme = datetime.strptime(horario, "%H:%M").replace(
            year=agora.year, month=agora.month, day=agora.day
        )

        # Se o horário já passou, programa para o próximo dia
        if hora_alarme < agora:
            hora_alarme += timedelta(days=1)

        print(f"⏰ Despertador programado para {hora_alarme.strftime('%H:%M')}")
        while datetime.now() < hora_alarme:
            time.sleep(1)
        print("\n⏰ Alarme tocando! Acorda!!")
    except ValueError:
        print("Formato de horário inválido. Use HH:MM.")

# Menu principal
def menu():
    while True:
        print("\n\n=== Menu do Relógio ===")
        print("1. Ver relógio em tempo real")
        print("2. Cronômetro")
        print("3. Timer (temporizador)")
        print("4. Despertador")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relogio()
        elif opcao == "2":
            cronometro()
        elif opcao == "3":
            timer()
        elif opcao == "4":
            despertador()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()