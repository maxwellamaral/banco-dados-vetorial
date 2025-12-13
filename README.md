# Banco de Dados Vetorial 🧠

Este repositório contém exemplos práticos e implementações de **Bancos de Dados Vetoriais**, demonstrando como armazenar, indexar e recuperar dados baseados em similaridade semântica (Vector Search).

O projeto é ideal para quem deseja entender os fundamentos por trás de aplicações modernas de IA, como **RAG (Retrieval-Augmented Generation)**, sistemas de recomendação e busca semântica.

## 🚀 Funcionalidades

  * **Geração de Embeddings:** 
    - APIs cloud (OpenAI, Google Gemini)
    - Modelos locais (Ollama: nomic-embed-text, mxbai-embed-large, all-minilm)
  * **Armazenamento Vetorial:** Persistência e indexação com FAISS (Facebook AI Similarity Search)
  * **Busca Semântica:** 
    - Similaridade cosseno
    - Distância euclidiana (L2)
    - Conversão para ângulos
  * **Exemplos de RAG:** 
    - Com APIs cloud (OpenAI GPT-3.5/4)
    - Com modelos locais (Ollama)
  * **Comparativos:** Benchmarks de performance e qualidade entre modelos de embeddings

## 🛠️ Tecnologias Utilizadas

  * **Linguagem:** Python 3.10+
  * **Banco Vetorial:** FAISS (Facebook AI Similarity Search)
  * **Embeddings:** OpenAI / Google Gemini / Ollama (local)
  * **Frameworks:** LangChain
  * **Containerização:** Docker / Docker Compose

## 📦 Como Usar

### 1\. Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/maxwellamaral/banco-dados-vetorial.git
cd banco-dados-vetorial
pip install -r requirements.txt
```

### 2\. Configuração

Crie um arquivo `.env` para suas chaves de API (se necessário):

```env
OPENAI_API_KEY=sua-chave-aqui
```

### 3\. Executando os Notebooks

#### Opção 1: Com Docker (Recomendado)

```bash
# Iniciar todos os serviços (Jupyter + Ollama)
docker-compose up -d

# Acessar Jupyter Lab
# http://localhost:8888

# Acessar Ollama API
# http://localhost:11434
```

Para mais detalhes sobre configuração do Ollama, consulte:
- [OLLAMA_SETUP.md](OLLAMA_SETUP.md)
- [QUICKSTART_OLLAMA.md](QUICKSTART_OLLAMA.md)

#### Opção 2: Localmente

```bash
# Iniciar Jupyter Lab
jupyter lab

# Ou Jupyter Notebook
jupyter notebook
```

## 📂 Estrutura do Projeto

```
src/
├── 1_fundamentos/              # Conceitos básicos de embeddings e vetores
│   ├── espaco_3d.ipynb                      # Visualização de vetores em 3D
│   ├── lab_1.0_similaridade_cosseno.ipynb   # Fundamentos de similaridade
│   ├── lab_1.1_matrioska.ipynb              # Embeddings matryoshka
│   ├── lab_1.2_comparativos.ipynb           # OpenAI vs Google Gemini
│   └── lab_1.3_comparativos_ollama.ipynb    # Comparação com modelos locais
│
├── 2_buscas/                   # Busca semântica com FAISS
│   ├── lab_2.0_ollama.ipynb                 # Configuração Ollama
│   ├── lab_2.1_buscas_nuvem.ipynb           # FAISS + APIs cloud
│   ├── lab_2.2_buscas_local.ipynb           # FAISS + Ollama
│   └── lab_2.3_buscas_local_comparativo.ipynb  # Benchmarks
│
└── 3_rag_persistencia/         # RAG (Retrieval-Augmented Generation)
    ├── lab_3.1_mini_rag.ipynb               # RAG com OpenAI
    └── lab_3.2_mini_rag_ollama.ipynb        # RAG com Ollama (local)
```

## 🤝 Contribuição

Sinta-se à vontade para abrir **Issues** ou enviar **Pull Requests** com melhorias, novos exemplos de uso ou correções.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](https://www.google.com/search?q=LICENSE) para mais detalhes.

-----

## Para citações

```bib
@software{amaral_bancodadosvetorial,
  author = {Anderson, Maxwell},
  title = {Banco de Dados Vetorial},
  url = {https://github.com/maxwellamaral/banco-dados-vetorial},
  year = {2025},
  version = {1.0},
  note = {GitHub repository},
  urldate = {2025-05-10}
}
```
