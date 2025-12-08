import requests
import time
import statistics

OLLAMA_URL = 'http://localhost:11434/api/embed'
TEST_TEXT = 'Banco de dados vetorial é uma tecnologia para armazenar e buscar embeddings de forma eficiente usando similaridade de cosseno'

models = ['all-minilm', 'nomic-embed-text', 'mxbai-embed-large']
results = {}

for model in models:
    print(f'\n🔄 Testando {model}...')
    times = []
    
    for i in range(5):
        start = time.time()
        response = requests.post(OLLAMA_URL, json={'model': model, 'input': TEST_TEXT})
        end = time.time()
        
        if response.status_code == 200:
            data = response.json()
            times.append(end - start)
            if i == 0:
                embedding_size = len(data['embeddings'][0])
                print(f'  ✅ Dimensão: {embedding_size}')
        else:
            print(f'  ❌ Erro: {response.status_code}')
            break
    
    if times:
        results[model] = {
            'avg_time': statistics.mean(times),
            'min_time': min(times),
            'max_time': max(times),
            'embedding_size': embedding_size
        }
        print(f'  ⏱️  Tempo médio: {results[model]["avg_time"]:.3f}s')
        print(f'  ⚡ Tempo mínimo: {results[model]["min_time"]:.3f}s')
        print(f'  🐌 Tempo máximo: {results[model]["max_time"]:.3f}s')

print('\n📊 RESUMO COMPARATIVO:')
print('-' * 70)
for model, data in sorted(results.items(), key=lambda x: x[1]['avg_time']):
    print(f'{model:20} | {data["embedding_size"]:4d}D | Avg: {data["avg_time"]:.3f}s')
print('-' * 70)
