# Engenharia Vetorial: Fundamentos e Aplicações de RAG

## Carga Horária

**20 horas**, divididas em 4 módulos principais com 17 laboratórios práticos.

---

## Conteúdo Programático

### **Módulo 1: Fundamentos de Espaços Vetoriais e Embeddings**

Compreensão dos conceitos fundamentais de representação vetorial e similaridade semântica.

**Objetivos de Aprendizagem:**
- Entender como conceitos são representados como vetores em espaços multidimensionais
- Dominar o cálculo de similaridade de cosseno e distância euclidiana
- Compreender embeddings Matryoshka e otimização de dimensionalidade
- Comparar diferentes modelos de embeddings (OpenAI, Google Gemini, Ollama)

**Laboratórios Práticos:**
- **Lab 1.1** - Visualização de Espaços Vetoriais Semânticos 3D
- **Lab 1.2** - Similaridade de Cosseno: Fundamentos da Busca Semântica
- **Lab 1.3** - Embeddings Matryoshka: Economia de Espaço e Performance
- **Lab 1.4** - Comparativo de Modelos de Embeddings (APIs Cloud)
- **Lab 1.5** - Comparativo de Modelos de Embeddings (Ollama Local)

**Ferramentas e Conceitos:**
- Matplotlib, Plotly (visualizações 3D)
- NumPy, scikit-learn (cálculos vetoriais)
- OpenAI API, Google Gemini API
- Ollama (modelos locais)
- Métricas: Similaridade de Cosseno, Distância Euclidiana (L2)

---

### **Módulo 2: Busca Semântica e Bancos Vetoriais**

Implementação de sistemas de busca inteligente usando bancos de dados vetoriais.

**Objetivos de Aprendizagem:**
- Implementar busca semântica com FAISS
- Comparar APIs em nuvem vs. modelos locais (Ollama)
- Entender métricas de similaridade e indexação vetorial
- Realizar análises comparativas de performance e custo

**Laboratórios Práticos:**
- **Lab 2.0** - Testes com Ollama: Setup e Validação
- **Lab 2.1** - Busca Semântica com APIs em Nuvem (OpenAI/Google)
- **Lab 2.2** - Busca Semântica Local com Ollama
- **Lab 2.3** - Comparativo: Busca Local vs. Cloud

**Ferramentas e Conceitos:**
- LangChain (framework de integração)
- FAISS (Facebook AI Similarity Search)
- Ollama (all-minilm, nomic-embed-text, mxbai-embed-large)
- Comparação de custos: APIs pagas vs. modelos gratuitos locais

---

### **Módulo 3: RAG - Retrieval Augmented Generation e Persistência**

Construção de sistemas RAG completos com persistência de dados e técnicas avançadas.

**Objetivos de Aprendizagem:**
- Implementar pipelines RAG do zero (Retrieval + Generation)
- Dominar chunking strategies e tokenização
- Persistir e reutilizar índices vetoriais
- Utilizar LCEL (LangChain Expression Language) para chains
- Aplicar técnicas avançadas: Self-Querying, Memória Conversacional, Reranking

**Laboratórios Práticos:**
- **Lab 3.1** - Persistência de Índices Vetoriais (FAISS + Cloud)
- **Lab 3.2** - Persistência com Ollama Local
- **Lab 3.3** - Chunks vs. Tokens: Estratégias de Divisão de Texto
- **Lab 3.4** - Mini RAG: Abordagem Procedural (PDFs)
- **Lab 3.5** - Mini RAG com LCEL (LangChain Expression Language)
- **Lab 3.6** - RAG Avançado Completo: Integração de Todas as Técnicas
- **Lab 3.7** - Self-Querying e Memória Conversacional

**Ferramentas e Conceitos:**
- PyPDFLoader (carregamento de documentos)
- RecursiveCharacterTextSplitter (chunking inteligente)
- FAISS com persistência (save_local/load_local)
- Prompt Templates e chains
- LCEL: RunnablePassthrough, StrOutputParser
- Filtros de metadados automáticos
- Memória conversacional (histórico de chat)
- Reranking de resultados

---

### **Módulo 4: Bancos Vetoriais em Produção**

Implementação de soluções RAG escaláveis e prontas para ambientes produtivos.

**Objetivos de Aprendizagem:**
- Migrar de FAISS (protótipo) para Qdrant (produção)
- Configurar bancos vetoriais com Docker
- Implementar RAG com persistência distribuída
- Otimizar performance e escalabilidade

**Laboratórios Práticos:**
- **Lab 4.1** - RAG com Qdrant: Banco Vetorial em Produção

**Ferramentas e Conceitos:**
- Qdrant (banco vetorial nativo)
- Docker e Docker Compose
- QdrantClient e QdrantVectorStore
- Configuração de collections e shards
- API REST para integração

---

## O que esperar deste curso

**Formato:** Mentoria prática, com aulas síncronas e suporte via plataforma digital.

**Acesso:** Material do curso, códigos e atividades disponibilizados nesta plataforma.

**Abordagem:**
- Exposição teórica aplicada
- Demonstrações práticas com código executável
- Implementação orientada em Jupyter Notebooks
- Exercícios guiados e construção progressiva de um sistema real
- Análises comparativas de custos e performance

**Ferramentas Utilizadas:**
- **Ambiente:** Python 3.10+, Jupyter Notebooks, Docker
- **Frameworks:** LangChain, LangChain Community
- **Embeddings:** OpenAI, Google Gemini, Ollama (nomic-embed-text, mxbai-embed-large)
- **LLMs:** Ollama (llama3.2, qwen2.5)
- **Bancos Vetoriais:** FAISS (prototipação), Qdrant (produção)
- **Processamento:** PyPDF, RecursiveCharacterTextSplitter
- **Visualização:** Matplotlib, Plotly, Pandas

---

## Regras e Diretrizes

**Desempenho:**
- Conclusão de todos os módulos e execução dos laboratórios práticos
- Participação efetiva nos encontros síncronos
- Entrega dos artefatos solicitados

**Entrega de Artefatos:**
- Envio de códigos executados e testados
- Implementações dos sistemas RAG
- Análises comparativas e relatórios de performance

**Frequência:**
- Participação mínima de **75%** nos encontros síncronos

**Conclusão:**
- Sinalizar a finalização de cada atividade obrigatória no AVA
- Validação dos laboratórios práticos

**Reprovação:**
- Em caso de não cumprimento dos requisitos, será necessário aguardar uma nova oferta para refazer a mentoria

---

## Resultados Esperados

Ao final desta mentoria, você será capaz de:

✅ **Compreender** os fundamentos matemáticos de espaços vetoriais e similaridade semântica

✅ **Implementar** sistemas de busca semântica usando embeddings de última geração

✅ **Construir** pipelines RAG (Retrieval Augmented Generation) completos

✅ **Comparar** soluções cloud vs. local, avaliando custos, performance e privacidade

✅ **Otimizar** estratégias de chunking, tokenização e indexação

✅ **Persistir** e reutilizar índices vetoriais em produção

✅ **Desenvolver** sistemas inteligentes com Self-Querying e memória conversacional

✅ **Implantar** bancos vetoriais em ambientes produtivos (Qdrant)

✅ **Integrar** LLMs locais (Ollama) em aplicações reais

✅ **Analisar** trade-offs entre diferentes arquiteturas e modelos

---

## Certificação

Os concluintes desta mentoria receberão **certificado** contendo informações do curso e de seu conteúdo programático.

**Importante:** Para evitar problemas na certificação, verifique se seus dados pessoais (nome completo e CPF) estão corretos e atualizados nesta plataforma.

---

## Infraestrutura Técnica

**Ambiente de Desenvolvimento:**
- Docker e Docker Compose
- Jupyter Lab containerizado
- Ollama (servidor local de LLMs)
- Qdrant (banco vetorial)

**Requisitos:**
- Python 3.10+
- 8GB RAM mínimo (16GB recomendado)
- Conexão com internet (para APIs cloud)
- Docker instalado (para ambientes isolados)

**APIs Necessárias (opcionais):**
- OpenAI API Key (testes com modelos cloud)
- Google Gemini API Key (comparativos)

---

Aproveite esta oportunidade para aprofundar seus conhecimentos em **sistemas inteligentes**, **busca semântica** e **IA generativa**, capacitando-se para desenvolver soluções modernas baseadas em **RAG** e **bancos vetoriais**.

**Desejamos um excelente aprendizado!** 🚀
