#!/bin/bash
# ===============================================
# Script de inicialização do Apache Airflow via Docker Compose
# ===============================================
# Uso:
#   chmod +x start-airflow.sh
#   ./start-airflow.sh
# ===============================================

set -e  # Interrompe o script se ocorrer algum erro

echo "🚀 Iniciando setup do Apache Airflow..."

# -----------------------------------------------
# 1️⃣ Criar diretórios necessários
# -----------------------------------------------
echo "📁 Criando diretórios..."
mkdir -p ./dags ./logs ./plugins ./scripts

# -----------------------------------------------
# 2️⃣ Configurar permissões (UID do usuário atual)
# -----------------------------------------------
echo "⚙️ Configurando permissões..."
echo -e "AIRFLOW_UID=$(id -u)" > .env
echo "Arquivo .env criado com AIRFLOW_UID=$(id -u)"

# -----------------------------------------------
# 3️⃣ Inicializar banco de dados e criar usuário admin
# -----------------------------------------------
echo "🧩 Inicializando banco de dados e usuário do Airflow..."
docker compose up airflow-init

# -----------------------------------------------
# 4️⃣ Iniciar todos os serviços (em background)
# -----------------------------------------------
echo "🧠 Subindo serviços do Airflow..."
docker compose up -d

# -----------------------------------------------
# 5️⃣ Verificar status dos containers
# -----------------------------------------------
echo "📊 Verificando status dos serviços..."
docker compose ps

# -----------------------------------------------
# 6️⃣ Exibir logs do scheduler
# -----------------------------------------------
echo "📜 Exibindo logs do scheduler (CTRL+C para sair)..."
docker compose logs -f airflow-scheduler

# -----------------------------------------------
# 7️⃣ Informações de acesso
# -----------------------------------------------
echo ""
echo "🌐 Interface Web disponível em: http://localhost:8080"
echo "👤 Usuário: airflow"
echo "🔑 Senha: airflow"
echo ""
echo "✅ Setup concluído com sucesso!"
