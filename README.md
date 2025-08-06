# Mineração de Dados do Spotify: Análise de Features de Áudio

![Spotify Logo](https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png)

##  Visão Geral do Projeto

Este projeto utiliza a API do Spotify para coletar dados sobre as faixas de um artista e analisa suas características de áudio. O script implementa um pipeline que:
1.  Autentica-se na API do Spotify.
2.  Busca por um artista específico (neste caso, Taylor Swift).
3.  Coleta todos os seus álbuns e respectivas faixas.
4.  Extrai as *features* de áudio de cada faixa (como `danceability`, `energy`, `valence`, `acousticness`).
5.  Estrutura os dados em um DataFrame do Pandas e os salva em um arquivo CSV para futuras análises.

## 🛠️ Principais Técnicas e Ferramentas

* **Linguagem:** Python
* **Bibliotecas:**
    * **API:** Spotipy (Wrapper Python para a API do Spotify)
    * **Manipulação de Dados:** Pandas
* **Conceitos:**
    * Consumo de APIs REST
    * Coleta e Extração de Dados (Web Scraping)
    * Engenharia de Features
    * Estruturação de Dados

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

* Python 3.8 ou superior
* Credenciais de desenvolvedor para a API do Spotify ([link para o dashboard](https://developer.spotify.com/dashboard))

### 2. Instalação

```bash
pip install spotipy pandas
```

### 3. Configuração

No script `mineracaoSpotify.py`, insira suas credenciais da API nas variáveis de ambiente ou diretamente no código:
```python
# Configure suas credenciais
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="SEU_CLIENT_ID",
                                                           client_secret="SEU_CLIENT_SECRET"))
```

### 4. Execução

Execute o script Python. Ele irá gerar um arquivo `spotify_audio_features.csv` no mesmo diretório.
```bash
python mineracaoSpotify.py
```

## 📈 Resultados

O resultado final é um dataset estruturado em formato CSV contendo as faixas do artista e suas respectivas features de áudio, pronto para ser utilizado em projetos de Machine Learning, como sistemas de recomendação, classificação de gênero musical ou análise de sentimentos.

## 👤 Autor

* **[Seu Nome Completo]**
* **LinkedIn:** [link para o seu LinkedIn]
