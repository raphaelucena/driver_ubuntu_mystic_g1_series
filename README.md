# CPU Cooler - Projeto

Este projeto tem como objetivo o controle de um cooler de CPU através de um dispositivo USB. Para rodar e compilar a aplicação, siga os passos abaixo.

## Requisitos

Antes de rodar o projeto, instale as dependências necessárias utilizando o `pip`:

```bash
pip3 install hid
pip3 install psutil
```

## Execução

Siga os passos abaixo para executar o projeto:

    Executar como superusuário: Certifique-se de estar executando os comandos com permissões de superusuário. Use sudo su para obter permissões administrativas:

```bash
sudo su
```

Configurar as regras do udev: Adicione a regra para permitir o acesso ao dispositivo USB. Isso é necessário para garantir que o dispositivo seja reconhecido corretamente pelo sistema.


```bash
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0xaa88", ATTR{idProduct}=="0x8666", MODE="0666"' > /etc/udev/rules.d/50-usb-scale.conf
```

Reiniciar o sistema: Reinicie o sistema para que as mudanças de configuração tenham efeito.


```bash
reboot
```

Criar um ambiente virtual: Crie e ative um ambiente virtual Python para isolar as dependências do projeto:

```bash
python3 -m venv venv
source venv/bin/activate
```

Executar o script: Após ativar o ambiente virtual, execute o script principal para controlar o cooler:

```bash
python3 cpu_cooler.py
```

## Compilação

Para compilar o projeto em um arquivo executável, siga os passos abaixo:

    Instalar o PyInstaller: O PyInstaller é utilizado para gerar o arquivo executável a partir do código Python. Instale-o com o comando abaixo:

```bash
pip install pyinstaller
```

Compilar o projeto: Execute o PyInstaller com as opções apropriadas para gerar o arquivo executável. A opção --onefile cria um único arquivo, e as opções --hidden-import e --collect-all garantem que as dependências necessárias sejam incluídas no executável.

```bash
pyinstaller --onefile --hidden-import=psutil --hidden-import=hid --collect-all=psutil --collect-all=hid cpu_cooler.py
```

Após a compilação, o arquivo executável será gerado na pasta dist.
Contribuindo

## Instalação

Copie o executavel para /opt

Copie o arquivo cpu_cooler.service para /etc/systemd/system

Execute os comandos

```bash
systemctl start cpu_cooler.service
systemctl enable cpu_cooler.service
```

Se desejar contribuir para o projeto, faça um fork, crie uma branch para suas alterações e envie um pull request com suas modificações.
Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.


Agora, você tem o conteúdo do `README.md` sem a formatação extra, pronto para copiar e colar diretamente no seu arquivo.
