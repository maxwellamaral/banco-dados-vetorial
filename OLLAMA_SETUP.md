# 🚀 Setup do Ollama com Modelos Pré-instalados

## 📦 Modelos Incluídos

A imagem customizada `ollama-embeddings-custom:latest` vem com os seguintes modelos de embeddings pré-instalados:

| Modelo | Dimensões | Tamanho | Uso Recomendado |
|--------|-----------|---------|-----------------|
| **all-minilm:latest** | 384 | ~23 MB | Mobile, edge, prototipagem rápida |
| **nomic-embed-text:latest** | 768 | ~274 MB | RAG, busca semântica geral |
| **mxbai-embed-large:latest** | 1024 | ~670 MB | Máxima qualidade, produção |

**Tamanho total dos modelos:** ~967 MB

## 🔨 Build da Imagem

### Primeira vez (build inicial):

```bash
# Com GPU (NVIDIA)
docker-compose build ollama

# Ou CPU-only
docker-compose -f docker-compose-cpu.yaml build ollama
```

**⏱️ Tempo estimado de build:**
- Download da imagem base: ~2-3 min
- Download dos modelos: ~5-10 min (depende da internet)
- **Total: ~10-15 minutos**

### Verificar se a imagem foi criada:

```bash
docker images | grep ollama-embeddings-custom
```

Deve retornar:
```
ollama-embeddings-custom   latest   abc123def456   5 minutes ago   2.1GB
```

## 🚀 Iniciar Serviços

### Stack completa (GPU):

```bash
docker-compose up -d
```

### Stack CPU-only:

```bash
docker-compose -f docker-compose-cpu.yaml up -d
```

### Verificar se Ollama está rodando:

```bash
docker-compose logs ollama
```

Deve mostrar:
```
✅ Ollama está online!
📋 Modelos disponíveis:
- all-minilm:latest
- nomic-embed-text:latest
- mxbai-embed-large:latest
```

## 🧪 Testar Modelos

### Via linha de comando:

```bash
# Listar modelos instalados
docker exec ollama-embeddings ollama list

# Testar embedding com all-minilm
docker exec ollama-embeddings ollama run all-minilm "Hello world"

# Testar embedding com nomic-embed-text
docker exec ollama-embeddings ollama run nomic-embed-text "Hello world"

# Testar embedding com mxbai-embed-large
docker exec ollama-embeddings ollama run mxbai-embed-large "Hello world"
```

### Via API (curl):

```bash
# Health check
curl http://localhost:11434/api/tags

# Gerar embedding com nomic-embed-text
curl http://localhost:11434/api/embed -d '{
  "model": "nomic-embed-text",
  "input": "O gato é um animal doméstico"
}'
```

### Via Python (notebook):

```python
import requests

OLLAMA_API_URL = "http://localhost:11434"

# Verificar modelos disponíveis
response = requests.get(f"{OLLAMA_API_URL}/api/tags")
print(response.json())

# Gerar embedding
response = requests.post(f"{OLLAMA_API_URL}/api/embed", json={
    "model": "nomic-embed-text",
    "input": "O gato é um animal doméstico"
})
embedding = response.json()["embeddings"][0]
print(f"Dimensões: {len(embedding)}")
print(f"Primeiros 5 valores: {embedding[:5]}")
```

## 🔄 Atualizar Modelos

Se novos modelos forem lançados, você pode adicioná-los sem rebuild:

```bash
# Acessar container
docker exec -it ollama-embeddings bash

# Dentro do container, baixar novo modelo
ollama pull <nome-do-modelo>

# Sair
exit
```

Para tornar permanente, adicione o modelo no `Dockerfile.ollama` e faça rebuild.

## 🐛 Troubleshooting

### Problema: "Model not found"

**Causa:** Modelos não foram baixados durante o build.

**Solução:**
```bash
# Rebuild forçado
docker-compose build --no-cache ollama
docker-compose up -d ollama
```

### Problema: Build muito lento

**Causa:** Download dos modelos (~1GB) leva tempo.

**Solução:** Use cache do Docker. Se já fez build antes, o Docker reutiliza as layers.

### Problema: Erro de memória durante build

**Causa:** Docker sem recursos suficientes.

**Solução:** Aumente memória do Docker:
- Docker Desktop → Settings → Resources → Memory → 8GB+

### Problema: Modelo não responde

**Causa:** Ollama pode estar sobrecarregado ou travado.

**Solução:**
```bash
# Reiniciar serviço
docker-compose restart ollama

# Ver logs
docker-compose logs -f ollama
```

## 📊 Comparação: Build vs Pull Manual

### Opção 1: Build (atual)
✅ Modelos prontos imediatamente  
✅ Desenvolvimento/curso mais rápido  
✅ Reprodutível  
❌ Build inicial demorado (~15 min)  
❌ Imagem maior (~2.1GB)

### Opção 2: Pull manual (alternativa)
✅ Build instantâneo  
✅ Imagem menor (~500MB)  
❌ Precisa baixar modelos manualmente  
❌ Estudantes podem esquecer de baixar  
❌ Primeiro uso mais lento

**Recomendação:** Use a **Opção 1 (build)** para ambiente de curso/educacional.

## 🎓 Uso nos Notebooks

Os notebooks do curso já estão configurados para usar estes modelos:

- `lab_1.3_comparativos_ollama.ipynb` - Compara os 3 modelos
- `lab_1.5_buscas_local.ipynb` - Usa nomic-embed-text
- `lab_1.6_buscas_local_comparativo.ipynb` - Compara todos

Basta executar as células e os modelos estarão disponíveis! 🚀

## 📚 Recursos

- **Ollama Docs:** https://github.com/ollama/ollama/tree/main/docs
- **Model Library:** https://ollama.ai/library
- **API Reference:** https://github.com/ollama/ollama/blob/main/docs/api.md
