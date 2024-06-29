#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/use para `limpar o histórico dos navegadores` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar para `limpar o histórico dos navegadores` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to configure/install/use to `clear browser history` in `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `Navegadores`
# 
# Navegadores, também conhecidos como "web browsers," são aplicativos de software projetados para permitir que os usuários acessem e naveguem pela World Wide Web. Eles desempenham um papel fundamental na experiência de navegação na internet, interpretando e exibindo páginas da web que contêm texto, imagens, vídeos e outros tipos de conteúdo. Além de visualizar sites, os navegadores oferecem recursos como abas de navegação múltiplas, gerenciamento de favoritos, histórico de navegação, pesquisa integrada e a capacidade de instalar extensões e complementos para personalizar a funcionalidade. Alguns dos navegadores mais populares incluem o Google Chrome, Mozilla Firefox, Microsoft Edge, Apple Safari e Opera, cada um com suas próprias características e desempenho para atender às preferências dos usuários. Eles desempenham um papel central na vida online moderna, tornando a internet acessível e explorável para pessoas em todo o mundo.

# ## 1. Como configurar/instalar para `limpar o histórico dos navegadores` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar para `limpar o histórico dos navegadores` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para programar para que sempre que você faça o logon no seu sistema, o navegador seja fechado e, ao fazer o logout, os arquivos do `Chrome` e do `Firefox` sejam excluídos. No entanto, isso envolve a criação de scripts e a configuração de tarefas agendadas (cron jobs) no `Linux`. Vou explicar como fazer isso em etapas:
# 
# 3. **No seu diretório pessoal (`home`):**
# 
#     - Você pode criar uma pasta específica para scripts no seu diretório `home`. Por exemplo, `~/scripts/`.
# 
#     - Para criar esta pasta e os scripts, execute os seguintes comandos no `Terminal Emulator`:
# 
#     ```
#     mkdir ~/scripts
#     touch ~/scripts/close_browsers.sh
#     touch ~/scripts/cleanup_browsers.sh
#     ```

# 4. **Fechar o Navegador ao Fazer o Logon**
# 
#     4.1 **Criar um Script para Fechar os Navegadores:** Crie um script que feche os navegadores. Isso pode ser feito usando o comando `pkill`. Por exemplo, crie um arquivo chamado `close_browsers.sh` e adicione o seguinte:
# 
#     ```
#     #!/bin/bash
#     pkill firefox
#     pkill chrome
#     ```
# 
#     4.2 **Torne o script executável:** `chmod +x close_browsers.sh`

# Para identificar qual desses diretórios é o seu perfil ativo no `Firefox`, você deve verificar o arquivo `profiles.ini`. Este arquivo contém informações sobre todos os perfis existentes no `Firefox`, incluindo qual é o perfil padrão ou ativo.
# 
# 5. Você pode usar o comando `cat` para exibir o conteúdo do arquivo `profiles.ini` e identificar o seu perfil. Execute o seguinte comando no terminal: `cat ~/.mozilla/firefox/profiles.ini`
# 
#     5.1 **Utilizar o `Snap`:** Se o `Firefox` foi instalado via `Snap`, o diretório do perfil será diferente. Tente verificar se o perfil está localizado no diretório de snap: `ls ~/snap/firefox/common/.mozilla/firefox`
#     
#     5.1.1 **ou se estiver instalado como um `snap` clássico:** `ls /snap/firefox/current/.mozilla/firefox`
# 
#     5.1 O conteúdo do arquivo `profiles.ini` será algo semelhante a isto:
# 
#     ```
#     Copy code
#     [Profile0]
#     Name=default
#     IsRelative=1
#     Path=dgpqa6fh.default
#     Default=1
# 
#     [Profile1]
#     Name=default-esr
#     IsRelative=1
#     Path=y3chn979.default-esr
#     ```
# 
#     Neste exemplo, existem dois perfis (`Profile0` e `Profile1`). O perfil marcado com `Default=1` é o perfil padrão. No exemplo acima, o perfil padrão é o `dgpqa6fh.default`.
# 
# Então, baseado no que aparece no seu `profiles.ini`, você poderá identificar qual diretório corresponde ao seu perfil ativo.

# 6. **Excluir Arquivos ao Fazer o Logout**
# 
#     6.1 **Criar um Script de Limpeza:** Crie um script chamado `cleanup_browsers.sh` com os comandos para limpar os dados do Chrome e do Firefox (veja os comandos que mencionei na resposta anterior).
# 
#     ```
#     #!/bin/bash
#     rm -rf ~/.cache/google-chrome
#     rm -rf ~/.config/google-chrome
#     rm -rf ~/.mozilla/firefox/[Profile0]/
#     rm -rf ~/.mozilla/firefox/[Profile1]/
#     ```
# 
#     - Substitua `[SeuPerfil0]`, `[SeuPerfil1]` etc.  pelo seu perfil do Firefox.
# 
#     6.2 **Torne o script executável:** `chmod +x cleanup_browsers.sh`

# Para garantir que o script `cleanup_browsers.sh` seja executado quando o sistema for desligado (`shutdown`) ou reiniciado (`restart`), você precisará criar um script de sistema que seja chamado durante o processo de desligamento ou reinicialização. Em sistemas `Linux` que usam o `systemd` (que é o padrão na maioria das distribuições modernas), você pode fazer isso criando um serviço `systemd`.
# 
# Aqui está um guia passo a passo para criar um serviço `systemd` que execute o seu script `cleanup_browsers.sh` durante o desligamento ou reinicialização:
# 
# 1. Criar um Serviço `systemd`
# 
#     1.1 **Criar um Arquivo de Serviço `systemd`:** Abra um editor de texto para criar um novo arquivo de serviço. Por exemplo, usando o `nano` da seguinte maneira: `sudo nano /etc/systemd/system/cleanup-browsers.service`
# 
#     1.2 **Adicione o seguinte conteúdo ao arquivo:**
# 
#         ```
#         [Unit]
#         Description=Cleanup browsers
#         DefaultDependencies=no
#         Before=shutdown.target reboot.target sleep.target hibernate.target hybrid-sleep.target suspend-then-hibernate.target
# 
#         [Service]
#         ExecStart=/home/edenedfsls/scripts/cleanup_browsers.sh
#         Type=oneshot
#         RemainAfterExit=true
# 
#         [Install]
#         WantedBy=shutdown.target reboot.target sleep.target hibernate.target hybrid-sleep.target suspend-then-hibernate.target
#         # Substitua /home/edenedfsls/scripts/cleanup_browsers.sh pelo caminho real do seu script.
#         ```
# 
#     1.3. **Habilitar o Serviço:** Depois de salvar e fechar o arquivo, habilite o serviço com: `sudo systemctl enable cleanup-browsers.service`
# 
# 2. **Testar o Serviço:** É uma boa ideia testar o serviço para garantir que ele funciona como esperado. Você pode testar reiniciando o sistema ou usando comandos `systemctl` para simular o `start` e o `stop` do serviço.
# 
# **Notas Importantes**
# 
# - Essa abordagem requer privilégios de superusuário (`root`).
# 
# - Tenha cuidado ao criar e habilitar serviços `systemd`, pois erros podem afetar o processo de inicialização do sistema.
# 
# - Lembre-se de que o script será executado com privilégios de superusuário, então certifique-se de que ele seja seguro e não faça alterações indesejadas no sistema.
# 
# Ao seguir esses passos, você cria um serviço que será executado automaticamente quando o sistema for desligado ou reiniciado, realizando a limpeza dos dados dos navegadores conforme definido em seu script `cleanup_browsers.sh`.

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar para `limpar o histórico` dos navegadores no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÂO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Limpeza de navegação no linux.*** Disponível em: <https://chat.openai.com/c/19fe31de-cf8d-48b5-8a9f-5a8bf19bfb27> (texto adaptado). ChatGPT. Acessado em: 24/01/2024 08:16.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 08/01/2024 08:16.
# 
