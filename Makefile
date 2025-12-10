.PHONY: init features training inference backfill frontend-app monitoring-app lint format

# Cria o ambiente e instala todas as dependências via uv
init:
	uv sync --all-extras --group dev

# Gera novas features e persiste no feature store
features:
	uv run python scripts/feature_pipeline.py

# Treina um novo modelo e registra no model registry
training:
	uv run python scripts/training_pipeline.py

# Gera predições e envia para o feature store
inference:
	uv run python scripts/inference_pipeline.py

# Backfill do feature group com dados históricos
backfill:
	uv run python scripts/backfill_feature_group.py

# Inicia a aplicação Streamlit
frontend-app:
	uv run streamlit run src/frontend.py

monitoring-app:
	uv run streamlit run src/frontend_monitoring.py

# Lint e format com ruff (instalado via uv add --dev)
lint:
	@echo "Fixing lint issues..."
	uv run ruff check --fix .

format:
	@echo "Formatting Python code..."
	uv run ruff format .
