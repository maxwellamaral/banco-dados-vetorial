# Script de Build e Gerenciamento do Ollama
# PowerShell script para facilitar operações comuns
# Data: 2025-12-08

# Verificar pré-requisitos
function Test-Prerequisites {
    try {
        $dockerVersion = docker --version 2>$null
        if (-not $dockerVersion) {
            Write-Host "❌ Docker não está instalado ou não está no PATH!" -ForegroundColor Red
            Write-Host "   Instale o Docker Desktop: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
            exit 1
        }
        
        docker ps >$null 2>&1
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ Docker daemon não está rodando!" -ForegroundColor Red
            Write-Host "   Inicie o Docker Desktop primeiro." -ForegroundColor Yellow
            exit 1
        }
        
        return $true
    } catch {
        Write-Host "❌ Erro ao verificar pré-requisitos: $($_.Exception.Message)" -ForegroundColor Red
        exit 1
    }
}

# Função para exibir menu
function Show-Menu {
    Write-Host "`n🚀 Ollama - Gerenciamento de Modelos`n" -ForegroundColor Cyan
    Write-Host "1. Build imagem Ollama (com modelos pré-instalados)" -ForegroundColor Yellow
    Write-Host "2. Iniciar stack completa (GPU)" -ForegroundColor Yellow
    Write-Host "3. Iniciar stack CPU-only" -ForegroundColor Yellow
    Write-Host "4. Parar serviços" -ForegroundColor Yellow
    Write-Host "5. Ver logs (todos os serviços)" -ForegroundColor Yellow
    Write-Host "6. Listar modelos instalados" -ForegroundColor Yellow
    Write-Host "7. Testar API do Ollama" -ForegroundColor Yellow
    Write-Host "8. Status dos serviços" -ForegroundColor Yellow
    Write-Host "9. Limpar tudo (reset completo)" -ForegroundColor Red
    Write-Host "0. Sair`n" -ForegroundColor Yellow
}

# Verificar ambiente
Test-Prerequisites

# Loop principal
do {
    Show-Menu
    $choice = Read-Host "Escolha uma opção"
    
    switch ($choice) {
        "1" {
            Write-Host "`n📦 Iniciando build da imagem Ollama..." -ForegroundColor Green
            Write-Host "⏱️  Isso pode levar 10-15 minutos (download de ~1GB de modelos)`n" -ForegroundColor Yellow
            
            $useGpu = Read-Host "Usar versão com GPU? (s/n) [padrão: n]"
            
            if ($useGpu -eq "s") {
                docker-compose build ollama
            } else {
                docker-compose -f docker-compose-cpu.yaml build ollama
            }
            
            Write-Host "`n✅ Build concluído!" -ForegroundColor Green
            Read-Host "Pressione ENTER para continuar"
        }
        
        "2" {
            Write-Host "`n🚀 Iniciando stack completa (GPU)..." -ForegroundColor Green
            docker-compose up -d
            Write-Host "`n✅ Stack iniciada!" -ForegroundColor Green
            Write-Host "📍 Jupyter Lab: http://localhost:8888" -ForegroundColor Cyan
            Write-Host "📍 Qdrant: http://localhost:6333" -ForegroundColor Cyan
            Write-Host "📍 Ollama API: http://localhost:11434" -ForegroundColor Cyan
            Read-Host "Pressione ENTER para continuar"
        }
        
        "3" {
            Write-Host "`n🚀 Iniciando stack CPU-only..." -ForegroundColor Green
            docker-compose -f docker-compose-cpu.yaml up -d
            Write-Host "`n✅ Stack iniciada!" -ForegroundColor Green
            Write-Host "📍 Jupyter Lab: http://localhost:8888" -ForegroundColor Cyan
            Write-Host "📍 Qdrant: http://localhost:6333" -ForegroundColor Cyan
            Write-Host "📍 Ollama API: http://localhost:11434" -ForegroundColor Cyan
            Read-Host "Pressione ENTER para continuar"
        }
        
        "4" {
            Write-Host "`n🛑 Parando serviços..." -ForegroundColor Yellow
            docker-compose down
            docker-compose -f docker-compose-cpu.yaml down
            Write-Host "✅ Serviços parados!" -ForegroundColor Green
            Read-Host "Pressione ENTER para continuar"
        }
        
        "5" {
            Write-Host "`n📋 Escolha o serviço:`n" -ForegroundColor Cyan
            Write-Host "1. Ollama" -ForegroundColor Yellow
            Write-Host "2. Jupyter Lab" -ForegroundColor Yellow
            Write-Host "3. Qdrant" -ForegroundColor Yellow
            Write-Host "4. Todos" -ForegroundColor Yellow
            
            $service = Read-Host "`nServiço"
            
            Write-Host "`n📋 Logs (Ctrl+C para sair):`n" -ForegroundColor Cyan
            switch ($service) {
                "1" { docker-compose logs -f ollama }
                "2" { docker-compose logs -f jupyter }
                "3" { docker-compose logs -f qdrant }
                "4" { docker-compose logs -f }
                default { 
                    Write-Host "❌ Opção inválida" -ForegroundColor Red 
                    Start-Sleep -Seconds 2
                }
            }
        }
        
        "6" {
            Write-Host "`n📋 Modelos instalados no Ollama:`n" -ForegroundColor Cyan
            
            # Verificar se container está rodando (GPU ou CPU)
            $running = docker ps --filter "name=ollama-embeddings" --format "{{.Names}}"
            
            if ($running) {
                docker exec $running ollama list
            } else {
                Write-Host "❌ Container Ollama não está rodando!" -ForegroundColor Red
                Write-Host "   Use a opção 2 ou 3 para iniciar a stack primeiro." -ForegroundColor Yellow
            }
            
            Read-Host "`nPressione ENTER para continuar"
        }
        
        "7" {
            Write-Host "`n🧪 Testando API do Ollama...`n" -ForegroundColor Cyan
            
            try {
                $response = Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -Method Get
                
                Write-Host "✅ API está online!" -ForegroundColor Green
                Write-Host "`n📦 Modelos disponíveis:" -ForegroundColor Cyan
                
                foreach ($model in $response.models) {
                    $sizeGB = [math]::Round($model.size / 1GB, 2)
                    Write-Host "   - $($model.name) ($sizeGB GB)" -ForegroundColor White
                }
                
                # Teste de embedding
                Write-Host "`n🔬 Testando geração de embedding...`n" -ForegroundColor Cyan
                
                # Usar o primeiro modelo disponível
                $modelName = $response.models[0].name
                
                $embedPayload = @{
                    model = $modelName
                    input = "O gato é um animal doméstico"
                } | ConvertTo-Json
                
                $embedResponse = Invoke-RestMethod -Uri "http://localhost:11434/api/embed" -Method Post -Body $embedPayload -ContentType "application/json"
                
                $embedding = $embedResponse.embeddings[0]
                Write-Host "✅ Embedding gerado com sucesso! (modelo: $modelName)" -ForegroundColor Green
                Write-Host "   Dimensões: $($embedding.Count)" -ForegroundColor White
                Write-Host "   Primeiros 5 valores: $($embedding[0..4] -join ', ')" -ForegroundColor White
                
            } catch {
                Write-Host "❌ Erro ao conectar com API!" -ForegroundColor Red
                Write-Host "   Certifique-se que o Ollama está rodando (opção 2 ou 3)" -ForegroundColor Yellow
                Write-Host "   Erro: $($_.Exception.Message)" -ForegroundColor Red
            }
            
            Read-Host "`nPressione ENTER para continuar"
        }
        
        "8" {
            Write-Host "`n📊 Status dos Serviços:`n" -ForegroundColor Cyan
            docker-compose ps
            Read-Host "`nPressione ENTER para continuar"
        }
        
        "9" {
            Write-Host "`n⚠️  ATENÇÃO: Isso irá remover containers, redes e imagens!" -ForegroundColor Red
            Write-Host "   VOLUMES DE DADOS serão preservados (data/, faiss_indices/)" -ForegroundColor Yellow
            $confirm = Read-Host "Tem certeza? (digite 'CONFIRMAR' para prosseguir)"
            
            if ($confirm -eq "CONFIRMAR") {
                Write-Host "`n🗑️  Removendo containers e redes..." -ForegroundColor Yellow
                docker-compose down
                docker-compose -f docker-compose-cpu.yaml down
                
                Write-Host "🗑️  Removendo imagens customizadas..." -ForegroundColor Yellow
                docker rmi ollama-embeddings-custom:latest -f 2>$null
                docker rmi jupyter-vectordb-custom:latest -f 2>$null
                
                Write-Host "✅ Limpeza concluída!" -ForegroundColor Green
                Write-Host "   Volumes de dados foram PRESERVADOS." -ForegroundColor Cyan
                Write-Host "   Para remover também os dados, use: docker volume prune" -ForegroundColor Yellow
                Write-Host "   Para usar novamente, execute a opção 1 (build) primeiro." -ForegroundColor Yellow
            } else {
                Write-Host "❌ Operação cancelada." -ForegroundColor Yellow
            }
            
            Read-Host "Pressione ENTER para continuar"
        }
        
        "0" {
            Write-Host "`n👋 Até logo!`n" -ForegroundColor Cyan
            return
        }
        
        default {
            Write-Host "`n❌ Opção inválida! Tente novamente.`n" -ForegroundColor Red
            Start-Sleep -Seconds 2
        }
    }
    
} while ($choice -ne "0")
