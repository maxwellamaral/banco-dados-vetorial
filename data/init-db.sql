-- Script de inicialização do PostgreSQL
-- Cria extensões e tabelas básicas para armazenar metadados dos embeddings

-- Habilitar extensão para trabalhar com vetores (se disponível)
-- CREATE EXTENSION IF NOT EXISTS vector;

-- Tabela de metadados dos embeddings
CREATE TABLE IF NOT EXISTS embeddings_metadata (
    id SERIAL PRIMARY KEY,
    document_name VARCHAR(255) NOT NULL,
    embedding_model VARCHAR(100) NOT NULL,
    vector_dimension INTEGER NOT NULL,
    chunk_index INTEGER,
    total_chunks INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB
);

-- Índice para buscar por documento
CREATE INDEX IF NOT EXISTS idx_document_name ON embeddings_metadata(document_name);

-- Índice para buscar por modelo
CREATE INDEX IF NOT EXISTS idx_embedding_model ON embeddings_metadata(embedding_model);

-- Tabela para armazenar logs de operações
CREATE TABLE IF NOT EXISTS operation_logs (
    id SERIAL PRIMARY KEY,
    operation_type VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    details JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserir registro de inicialização
INSERT INTO operation_logs (operation_type, status, details)
VALUES ('database_init', 'success', '{"message": "Database initialized successfully"}');
