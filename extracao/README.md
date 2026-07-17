# FIA - Sinal de Mão

## Instalação da versão do Python

Para inicializar com pyenv, rode os seguintes comandos dentro do diretório principal do projeto:

```bash
pyenv install 3.14.6
python -m venv .venv
source .venv/bin/activate
```

## Pacotes

É necessário baixar o OpenCV para rodar o `extrair_frames.py`:

```bash
pip install opencv-python
```

## Extração de fotos

Para extrair fotos com base em um vídeo, você deve criar uma pasta qualquer dentro de `videos/`:

```bash
mkdir videos/nome_da_subpasta
```

Após isso, você deve adicionar o vídeo à subpasta criada acima. A fim de exemplo, vamos supor que a subpasta criada foi `'eu'` e o nome do arquivo é `'sinal.mp4'`. Dessa forma, o caminho relativo do arquivo fica `'videos/eu/sinal.mp4'`.

Com isso, só resta alterar os valores das constantes `AUTHOR`, `VIDEO_NAME` e `HAND_SIGNAL` conforme as instruções a seguir:

1. `AUTHOR` -> nome da subpasta escolhida dentro de videos, ex: `'eu'`.
2. `VIDEO_NAME` -> nome do arquivo de vídeo, ex: `'sinal.mp4'`.
3. `HAND_SIGNAL` -> nome do sinal de mão (em inglês) presente no vídeo conforme as subpastas de `../dataset/`, ex: `'horse'`.

Finalmente, você pode rodar o script:

```bash
python extrair_frames.py
```

As fotos resultantes serão adicionadas em `../dataset/[HAND_SIGNAL]/` com o nome: `autor-sinal-contador.jpg`.

> ⚠️ É recomendado que você analise cada uma das fotos geradas para evitar alimentar o modelo com imagens borradas ou algo do gênero.