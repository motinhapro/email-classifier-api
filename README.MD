# 🤖 Email Classifier - AutoU Challenge

Sistema inteligente de classificação de emails corporativos usando IA.

## 📋 Sobre o Projeto

Aplicação web que classifica emails em **Produtivos** (requerem ação) ou **Improdutivos** (não requerem ação) e sugere respostas automáticas adequadas.

**Desafio:** Processo seletivo AutoU - Estágio em Desenvolvimento

## 🚀 Tecnologias

- **Backend:** Python + FastAPI
- **IA:** OpenAI GPT-4o-mini
- **Frontend:** HTML + CSS + JavaScript

## ⚙️ Configuração Local

1. Clone o repositório
```bash
git clone 
cd email-classifier
```

2. Crie o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o .env e adicione sua OPENAI_API_KEY
```

5. Execute a aplicação
```bash
uvicorn app:app --reload
```

## 👨‍💻 Autor

Carlos Eduardo Mota - Desafio AutoU 2025