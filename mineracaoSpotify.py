import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import scipy

# ================== CONFIGURAÇÃO DA API DO SPOTIFY ==================
CLIENT_ID = 'SEU_CLIENT_ID'
CLIENT_SECRET = 'SEU_CLIENT_SECRET'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
))

# ================== DEFINIR ID DO ARTISTA BASE ==================
artista_id = 'artista_id_do_artista_base'  
artista_info = sp.artist(artista_id)
artista_nome = artista_info['name']

# ================== CONSTRUÇÃO DA REDE ==================
G = nx.Graph()

def adicionar_artistas_e_relacoes(artist_id, depth=1):
    fila = [(artist_id, 0)]
    visitados = set()

    while fila:
        atual, nivel = fila.pop(0)
        if atual in visitados or nivel > depth:
            continue
        visitados.add(atual)

        try:
            artista = sp.artist(atual)
            G.add_node(atual, name=artista['name'])

            relacionados = sp.artist_related_artists(atual)['artists']
            for rel in relacionados:
                rel_id = rel['id']
                G.add_node(rel_id, name=rel['name'])
                G.add_edge(atual, rel_id)
                fila.append((rel_id, nivel + 1))
        except Exception as e:
            print(f"Erro ao processar {atual}: {e}")
            continue

adicionar_artistas_e_relacoes(artista_id, depth=1)

# ================== PROPRIEDADES BÁSICAS ==================
num_vertices = G.number_of_nodes()
num_arestas = G.number_of_edges()
graus = dict(G.degree())
clustering = nx.average_clustering(G)

# ================== CENTRALIDADES ==================
centralidade_grau = nx.degree_centrality(G)
centralidade_eigen = nx.eigenvector_centrality_numpy(G)

nx.set_node_attributes(G, centralidade_grau, 'centralidade_grau')
nx.set_node_attributes(G, centralidade_eigen, 'centralidade_eigen')

# ================== PLOTAGEM DA REDE ==================
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42)

sizes = [1000 * centralidade_eigen[n] for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color='skyblue', alpha=0.8)
nx.draw_networkx_edges(G, pos, alpha=0.4)
nx.draw_networkx_labels(G, pos, {n: G.nodes[n]['name'] for n in G.nodes()}, font_size=8)
plt.title("Rede de Artistas Relacionados - Spotify")
plt.axis('off')
plt.savefig("rede_artistas.png")
plt.close()

# ================== RELATÓRIO EM PDF ==================
pdf_path = "relatorio_spotify.pdf"
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter

c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 50, "Análise de Rede: Artistas Relacionados no Spotify")

c.setFont("Helvetica", 12)
c.drawString(50, height - 80, f"Artista base: {artista_nome}")
c.drawString(50, height - 100, f"Número de vértices (artistas): {num_vertices}")
c.drawString(50, height - 120, f"Número de arestas (relações): {num_arestas}")
c.drawString(50, height - 140, f"Coeficiente de clustering médio: {clustering:.4f}")

c.drawString(50, height - 180, "Centralidade de Grau (top 5):")
top_grau = sorted(centralidade_grau.items(), key=lambda x: x[1], reverse=True)[:5]
for i, (node, val) in enumerate(top_grau):
    nome = G.nodes[node]['name']
    c.drawString(70, height - 200 - i * 15, f"{nome}: {val:.4f}")

c.drawString(50, height - 290, "Centralidade de Vetor Próprio (top 5):")
top_eigen = sorted(centralidade_eigen.items(), key=lambda x: x[1], reverse=True)[:5]
for i, (node, val) in enumerate(top_eigen):
    nome = G.nodes[node]['name']
    c.drawString(70, height - 310 - i * 15, f"{nome}: {val:.4f}")

c.drawImage("rede_artistas.png", 50, 50, width=500, preserveAspectRatio=True)
c.save()

print("Relatório gerado com sucesso:", pdf_path)
