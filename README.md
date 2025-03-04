# Git Auto Update Service

Este script cria um servidor HTTP simples que escuta requisições POST em `/gitpull` e executa `git pull` no repositório especificado. Ele pode ser configurado para rodar como um serviço no sistema.

## Pré-requisitos

### Python 3
- Verifique se o Python 3 está instalado:
  ```sh
  python3 --version
  ```
- Caso não esteja instalado, instale com:
  ```sh
  sudo apt update && sudo apt install python3
  ```

### Git
- Verifique se o Git está instalado:
  ```sh
  git --version
  ```
- Caso não esteja instalado, instale com:
  ```sh
  sudo apt install git
  ```

## Instalação e Configuração

### Clone o repositório ou crie o script manualmente
```sh
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### Torne o script executável
```sh
chmod +x server.py
```

## Executando manualmente

Para rodar o script manualmente, use:
```sh
python3 server.py
```

## Configurando como um serviço no Linux (Systemd)

Para garantir que o script inicie automaticamente junto com o sistema, crie um serviço systemd.

### Criar o arquivo de serviço
```sh
sudo nano /etc/systemd/system/git-auto-update.service
```

### Adicionar o seguinte conteúdo (ajuste os caminhos conforme necessário)
```ini
[Unit]
Description=Git Auto Update Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /caminho/para/server.py
WorkingDirectory=/caminho/para/
Restart=always
User=seu_usuario
Group=seu_grupo

[Install]
WantedBy=multi-user.target
```

### Recarregar os serviços do systemd e habilitar o serviço para iniciar automaticamente
```sh
sudo systemctl daemon-reload
sudo systemctl enable git-auto-update
sudo systemctl start git-auto-update
```

### Verificar o status do serviço
```sh
sudo systemctl status git-auto-update
```

Se precisar parar ou reiniciar o serviço, use:
```sh
sudo systemctl stop git-auto-update
sudo systemctl restart git-auto-update
```

## Testando o script

Para testar, envie uma requisição POST para o servidor:
```sh
curl -X POST http://localhost:8001/gitpull
```
Se configurado corretamente, o comando `git pull` será executado no repositório definido no script.

## Logs
Os logs podem ser verificados com:
```sh
sudo journalctl -u git-auto-update -f
```

## Segurança
Para evitar acessos indesejados, considere restringir as requisições ao IP desejado e adicionar autenticação.

---

## Habilitar no GITHUB
Basta entrar na sessão de configuração do seu repositorio, ir em webhooks e colocar a url do seu repositorio.



Agora seu script estará rodando continuamente e pronto para receber requisições para atualizar o repositório automaticamente!
