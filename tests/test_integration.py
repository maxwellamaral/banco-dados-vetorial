import requests

# Buscar por similaridade
query = 'GPU Nvidia'
print(f'🔍 Busca por: {query}')

# Criar embedding da query
embed_resp = requests.post('http://localhost:11434/api/embed', 
                          json={'model': 'nomic-embed-text', 'input': query})
query_vector = embed_resp.json()['embeddings'][0]

# Buscar no Qdrant
search = {
    'vector': query_vector,
    'limit': 3,
    'with_payload': True
}

result = requests.post('http://localhost:6333/collections/test_collection/points/search',
                      json=search,
                      headers={'api-key': 'abcd1234'}).json()

print('\n📊 Resultados:')
for r in result['result']:
    print(f"  ✅ Score: {r['score']:.4f} - {r['payload']['text']}")

print(f'\n✅ Integração Ollama + Qdrant funcionando perfeitamente!')
