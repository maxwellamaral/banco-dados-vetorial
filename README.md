# Banco de Dados Vetorial 🧠

Este repositório contém exemplos práticos e implementações de **Bancos de Dados Vetoriais**, demonstrando como armazenar, indexar e recuperar dados baseados em similaridade semântica (Vector Search).

O projeto é ideal para quem deseja entender os fundamentos por trás de aplicações modernas de IA, como **RAG (Retrieval-Augmented Generation)**, sistemas de recomendação e busca semântica.

## 🚀 Funcionalidades

  * **Geração de Embeddings:** 
    - APIs cloud (OpenAI, Google Gemini)
    - Modelos locais (Ollama: nomic-embed-text, mxbai-embed-large, all-minilm)
    - Suporte a Matryoshka Embeddings (redução de dimensões)
  * **Armazenamento Vetorial:** 
    - FAISS (desenvolvimento e prototipação)
    - Qdrant (produção e escalabilidade)
  * **Busca Semântica:** 
    - Similaridade de cosseno
    - Distância euclidiana (L2)
    - Conversão para ângulos
  * **RAG (Retrieval-Augmented Generation):** 
    - Com APIs cloud (OpenAI GPT-3.5/4, Google Gemini)
    - Com modelos locais (Ollama)
    - Implementações com LangChain e LCEL
  * **Estratégias de Chunking:**
    - Análise de tokens vs chunks
    - Chunking recursivo com separadores hierárquicos
    - Otimização de tamanho e overlap
  * **Comparativos:** Benchmarks de performance e qualidade entre modelos de embeddings

## 🛠️ Tecnologias Utilizadas

  * **Linguagem:** Python 3.10+
  * **Bancos Vetoriais:** 
    - FAISS (Facebook AI Similarity Search) - Para desenvolvimento e prototipação
    - Qdrant - Para aplicações em produção
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
│   ├── lab_1.1_espaços.ipynb                # Visualização de vetores em 3D
│   ├── lab_1.2_similaridade_cosseno.ipynb   # Fundamentos de similaridade de cosseno
│   ├── lab_1.3_matrioska.ipynb              # Embeddings Matryoshka (redução de dimensões)
│   ├── lab_1.4_comparativos.ipynb           # Comparativo OpenAI vs Google Gemini
│   └── lab_1.5_comparativos_ollama.ipynb    # Comparativo com modelos locais (Ollama)
│
├── 2_buscas/                   # Busca semântica com FAISS
│   ├── lab_2.0_ollama_testes.ipynb          # Testes e configuração do Ollama
│   ├── lab_2.1_buscas_nuvem.ipynb           # FAISS + APIs cloud (OpenAI/Gemini)
│   ├── lab_2.2_buscas_local.ipynb           # FAISS + Ollama (modelos locais)
│   └── lab_2.3_buscas_local_comparativo.ipynb  # Benchmarks de performance
│
├── 3_rag_persistencia/         # RAG e Persistência de Vetores
│   ├── lab_3.1_persistencia_nuvem.ipynb     # Persistência FAISS com APIs cloud
│   ├── lab_3.2_persistencia_ollama.ipynb    # Persistência FAISS com Ollama
│   ├── lab_3.3_chunks_tokens.ipynb          # Estratégias de chunking e tokenização
│   ├── lab_3.4_microrag_chain.ipynb         # Mini RAG com LangChain (básico)
│   ├── lab_3.5_microrag_chain_lcel.ipynb    # Mini RAG com LCEL (LangChain Expression Language)
│   └── utils_pdf_generator.py               # Utilitário para gerar PDFs de teste
│
└── 4_producao/                 # RAG em Produção
    └── lab_4.1_rag_qdrant.ipynb             # RAG com Qdrant (banco vetorial em produção)
```

## 🤝 Contribuição

Sinta-se à vontade para abrir **Issues** ou enviar **Pull Requests** com melhorias, novos exemplos de uso ou correções.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](https://www.google.com/search?q=LICENSE) para mais detalhes.

-----

## Para citações

```bibtex
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
