import hid
import time
import psutil  # Biblioteca para acessar sensores de temperatura

# Encontre o dispositivo HID conectado
for d in hid.enumerate():
    print(d)

# Conecte ao dispositivo pelo path (no caso, pelo Vendor ID e Product ID)
device = hid.Device(path=hid.enumerate(0xaa88, 0x8666)[0]['path'])

# Função para pegar a temperatura da CPU
def get_cpu_temp():
    # Pegando a temperatura do sensor 'coretemp' (pode variar dependendo do sistema)
    try:
        # 'coretemp' ou o nome do sensor pode variar. Vamos procurar por 'coretemp' no dicionário de temperaturas
        temperatures = psutil.sensors_temperatures()
        if 'coretemp' in temperatures:
            core_temp = temperatures['coretemp']
            # Retorna a primeira temperatura registrada no 'coretemp'
            return core_temp[0].current
        else:
            print("Sensor 'coretemp' não encontrado!")
            return 0  # Se não encontrar, retorna uma temperatura padrão
    except Exception as e:
        print(f"Erro ao obter temperatura: {e}")
        return 0  # Retorna 0 em caso de erro

# Função para enviar os dados para o dispositivo
def send_data():
    # Obtém a temperatura da CPU
    temp = get_cpu_temp()
    # Garante que a temperatura esteja dentro do intervalo de 0-255
    temp = max(0, min(255, int(temp)))  # Converte para inteiro e limita entre 0 e 255

    # Cria o buffer de dados (temperatura + 62 bytes de preenchimento)
    data = bytes([0, temp] + [0] * 62)  # 64 bytes no total
    try:
        # Envia os dados para o dispositivo HID
        device.write(data)
        print(f"Temperatura: {temp}°C - Dados enviados: {data}")
    except Exception as e:
        print(f"Erro ao enviar dados: {e}")

# Loop para enviar os dados a cada 1 segundo
while True:
    send_data()
    time.sleep(1)  # Aguarda 1 segundo antes de enviar novamente
