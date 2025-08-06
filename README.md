# Mineração de Dados do Spotify: Análise de Features de Áudio

![Spotify Logo](https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png)

##  Visão Geral do Projeto

Este projeto utiliza a API do Spotify para coletar dados sobre as faixas de um artista e analisa suas características de áudio. O script implementa um pipeline que:
1.  Autentica-se na API do Spotify.
2.  Busca por um artista específico (neste caso, Taylor Swift).
3.  Coleta todos os seus álbuns e respectivas faixas.
4.  Extrai as *features* de áudio de cada faixa (como `danceability`, `energy`, `valence`, `acousticness`).
5.  Estrutura os dados em uma lista de dicionários e exibe os resultados diretamente no console.

## 🛠️ Principais Técnicas e Ferramentas

* **Linguagem:** Python
* **Bibliotecas:**
    * **API:** Spotipy (Wrapper Python para a API do Spotify)
* **Conceitos:**
    * Consumo de APIs REST
    * Coleta e Extração de Dados
    * Engenharia de Features
    * Estruturação de Dados (em listas e dicionários)

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

* Python 3.8 ou superior
* Credenciais de desenvolvedor para a API do Spotify ([link para o dashboard](https://developer.spotify.com/dashboard/))

### 2. Instalação

O único pré-requisito principal é a biblioteca Spotipy:
```bash
pip install spotipy
```

### 3. Configuração

No script `mineracaoSpotify.py`, insira suas credenciais da API diretamente no código:
```python
# Configure suas credenciais
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="SEU_CLIENT_ID",
                                                           client_secret="SEU_CLIENT_SECRET"))
```

### 4. Execução

Execute o script Python. A saída será impressa no terminal (console).
```bash
python mineracaoSpotify.py
```

## 📈 Resultados

O resultado final é uma **saída de dados no console**, contendo uma lista de dicionários onde cada dicionário representa uma faixa do artista com suas respectivas features de áudio. Este formato de saída pode ser facilmente redirecionado para um arquivo (`.json`, `.txt`) ou copiado para ser utilizado em outros scripts e ferramentas de análise, como Jupyter Notebooks, para projetos de Machine Learning.

A estrutura de cada dicionário na saída é a seguinte:

| Chave | Descrição | Exemplo |
| :--- | :--- | :--- |
| `nome_faixa` | Nome da música. | "Cruel Summer" |
| `artista` | Nome do artista principal. | "Taylor Swift" |
| `album` | Nome do álbum de origem. | "Lover" |
| `id_faixa` | ID único da faixa no Spotify. | "1BxfuPKGuaTgP7aM0Bbdwr" |
| `danceability`| Nível de "dançabilidade" da música (0.0 a 1.0). | 0.552 |
| `energy` | Nível de energia da música (0.0 a 1.0). | 0.702 |
| `valence` | A positividade musical da faixa (0.0 a 1.0). | 0.564 |
| `...` | *...outras features de áudio...* | ... |


## 👤 Autor

* **[Luis Felipe Marques Silva]**
* **LinkedIn:** [www.linkedin.com/in/luisfelipemsilva]
* **GitHub:** [https://github.com/Felipao98]
