# 🚀 Quick Start - Ollama com Modelos Pré-instalados

## ⚡ Início Rápido (3 passos)

### 1️⃣ Build da imagem (primeira vez apenas)

```powershell
# Opção A: Script interativo (recomendado)
.\manage-ollama.ps1

# Opção B: Manual com GPU
docker-compose build ollama

# Opção C: Manual CPU-only
docker-compose -f docker-compose-cpu.yaml build ollama
```

**⏱️ Tempo:** ~10-15 minutos (download de 1GB de modelos)

### 2️⃣ Iniciar serviços

```powershell
# Com GPU
docker-compose up -d

# CPU-only
docker-compose -f docker-compose-cpu.yaml up -d
```

### 3️⃣ Verificar modelos instalados

```powershell
docker exec ollama-embeddings ollama list
```

**Resultado esperado:**
```
NAME                       ID           SIZE    MODIFIED
all-minilm:latest          abc123       23 MB   2 minutes ago
nomic-embed-text:latest    def456       274 MB  2 minutes ago
mxbai-embed-large:latest   ghi789       670 MB  2 minutes ago
```

## 🎯 Modelos Incluídos

| Modelo | Dimensões | Tamanho | Uso |
|--------|-----------|---------|-----|
| `all-minilm:latest` | 384 | 23 MB | Rápido, prototipagem |
| `nomic-embed-text:latest` | 768 | 274 MB | RAG geral |
| `mxbai-embed-large:latest` | 1024 | 670 MB | Máxima qualidade |

## 🧪 Testar no Notebook

```python
import requests

# Verificar conexão
response = requests.get('http://localhost:11434/api/tags')
print(f"Modelos disponíveis: {len(response.json()['models'])}")

# Gerar embedding
payload = {
    "model": "nomic-embed-text",
    "input": "Teste de embedding"
}
response = requests.post('http://localhost:11434/api/embed', json=payload)
embedding = response.json()['embeddings'][0]
print(f"Dimensões: {len(embedding)}")
```

## 📁 Arquivos Criados

- `Dockerfile.ollama` - Imagem customizada com modelos
- `OLLAMA_SETUP.md` - Documentação completa
- `manage-ollama.ps1` - Script de gerenciamento
- `.dockerignore` - Otimização de build

## 🔄 Mudanças nos Docker Compose

### Antes:
```yaml
ollama:
  image: ollama/ollama:latest
```

### Depois:
```yaml
ollama:
  build:
    context: .
    dockerfile: Dockerfile.ollama
  image: ollama-embeddings-custom:latest
```

## ⚠️ Importante

1. **Primeira build é demorada** (~15 min) - Downloads de modelos
2. **Imagem fica maior** (~2.1GB vs ~500MB)
3. **Benefício:** Modelos prontos para usar imediatamente!

## 🐛 Problemas Comuns

### "Connection refused"
```powershell
# Verificar se está rodando
docker ps | Select-String ollama

# Se não estiver, iniciar
docker-compose up -d ollama
```

### "Model not found"
```powershell
# Rebuild forçado
docker-compose build --no-cache ollama
docker-compose up -d ollama
```

### Build travou
```powershell
# Cancelar (Ctrl+C) e tentar novamente
docker-compose build --progress=plain ollama
```

## 📚 Próximos Passos

1. ✅ Abrir Jupyter: http://localhost:8888
2. ✅ Executar `lab_1.3_comparativos_ollama.ipynb`
3. ✅ Testar os 3 modelos de embeddings
4. ✅ Comparar performance e qualidade

## 🆘 Ajuda

- **Documentação completa:** `OLLAMA_SETUP.md`
- **Script interativo:** `.\manage-ollama.ps1`
- **Ollama docs:** https://github.com/ollama/ollama
