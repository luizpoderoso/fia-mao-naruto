# Reconhecimento de 12 Selos de Mão do Anime Naruto

## 1. Objetivo

Desenvolver e avaliar um pipeline de aprendizado de máquina para a identificação automática de 12 diferentes selos de mão baseados no anime Naruto. O projeto tem como foco a comparação de desempenho entre os algoritmos **Stochastic Gradient Descent (SGD) Classifier** e **Random Forest Classifier** (com a inclusão de dois algoritmos adicionais: **KNeighborsClassifier** **SupportVectorClassifier**), analisando suas capacidades de generalização, mapeamento de características bidimensionais em vetores planos e superação de limitações estruturais intrínsecas a dados de imagens brutas.

## 2. Integrantes

- Ivanilton Vieira dos Santos
- Jean Fonseca Santos
- Luiz Cristóvão Rezende Poderoso

## 3. Fonte dos Dados

- Dataset original: https://www.kaggle.com/datasets/vikranthkanumuru/naruto-hand-sign-dataset
- Dataset Incremento da equipe: https://drive.google.com/drive/folders/1dltWyISMGq8yWZkPL9edTsIrClxLt48V?usp=sharing

## 4. Tipo da Tarefa

- **Classificação (Multiclasse)**

## 5. Organização dos Arquivos

O repositório está estruturado da seguinte forma:

```text
fia-mao-naruto/
├── scripts/
│   ├── videos/.gitkeep
│   ├── .gitignore
│   ├── extrair_frames.py
│   └── README.md
├── .gitignore
├── .python-version
├── notebook.ipynb
└── README.md
```

## 6. Instruções para abrir o notebook no Colab

Com o repositório clonado em sua máquina:

1. Acesse o [Google Colab](https://colab.research.google.com/).

2. No menu superior esquerdo, clique em **Arquivo** > **Fazer upload de notebook.**

3. Na janela que abrir, vá na aba `Upload` para carregar o arquivo `.ipynb` da sua máquina.

4. No menu superior, clique em **Executar tudo** para executar as células sequencialmente.

## 7. Modelos Utilizados

- _Dummy Classifier_

- _Stochastic Gradient Descent Classifier_

- _Random Forest Classifier_

- _KNeighborsClassifier_

- _SupportVectorClassifier_

## 8. Principais Resultados

- O _Dataset_ original selecionado pela equipe foi considerado insuficiente para a realização da demonstração. foi possível atestar a baixa variabilidade das imagens disponíveis e o desbalanceamento de dados entre as classes definidas pelo autor.

- O modelo que obteve melhor desempenho em relação à acurácia foi o _Random Forest_, apresentando uma taxa de 63,37%, o qual também em sua matriz de confusão apresentou uma diagonal principal consideravelmente mais densa quando comparado com o _SGD Classifier_. Em comparação com os algoritmos adicionais, o _Random Forest_ persistiu sendo superior. Porém, no processo de adição de novas imagens ao dataset, foi constatado que o _KNeighborsClassifier_ é um algoritmo extremamente promissor para esse tipo de problema, sendo possível visualizar um aumento considerável de sua acurácia.

- Apesar da acurácia superior, o _Random Forest_ ainda apresentou falsos positivos e negativos, ao ponto de classificar erroneamente a classe "rat" como "snake" 6 vezes quando avaliado, além da baixa acurácia de alguns selos como: "dog" - 16 acertos, "hare" - 20 acertos, "horse" - 20 acertos.

- Contudo, mesmo apresentando o maior desempenho entre as alternativas utilizadas, o _Random Forest_ está longe de ser a ferramenta ideal para o serviço proposto, não por uma falha do algoritmo em si, mas pela incompatibilidade entre a forma como ele toma decisões e a natureza visual das entradas, como, por exemplo, na incapacidade de compreender geometria pela necessidade de executar um _flattening_ na matriz dos bits de entrada.

## 9. Divisão das Contribuições

- **Ivanilton Vieira dos Santos:** Responsável pela divisão treino/teste e implementação/ajuste do modelo _SGD Classifier_, análise exploratória das imagens.

- **Jean Fonseca Santos:** Principal operador do script `extrair_frames.py` na conversão de vídeos em imagens, responsável pela escrita do `README.md` principal do projeto, execução de testes do projeto e averiguação da consistência dos resultados apresentados.

- **Luiz Cristóvão Rezende Poderoso:** Responsável pela implementação do script `extrair_frames.py`, pré-processamento, planificação dos dados, treinamento do _Random Forest_ e dos algoritmos adicionais, geração e análise das matrizes de confusão, elaboração das conclusões e organização do repositório.

Além das tarefas específicas, todos os membros da equipe (e amigos) participaram da captação de novos dados para o incremento do _dataset_ original.

## 10. Link do Vídeo

Vídeo disponivél em: video-pogg.com.br

## 11. Declaração de Uso de Ferramentas de Inteligência Artificial

Ferramenta utilizada: _Google Gemini_

#### Finalidades

- Auxílio na formatação e correção ortografica deste arquivo `README.md` e das análises presentes no notebook.
