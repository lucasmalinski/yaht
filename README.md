# 📝 YAHT - Yet Another Habit Tracker

## Tracker de hábitos CLI

![Versão](https://img.shields.io/badge/version-1.0.0-blue)
[![CI YAHT](https://github.com/lucasmalinski/yaht/actions/workflows/ci.yml/badge.svg)](https://github.com/lucasmalinski/yaht/actions/workflows/ci.yml)

## 🎯 Sobre o Projeto

**Problema Real:** A dificuldade de manter a consistência em pequenas rotinas diárias (como tomar remédios, exercícios ou estudos) pode prejudicar a saúde e a organização pessoal.
**Solução Proposta:** Uma aplicação simples de interface via linha de comando (CLI) que permite registrar e visualizar o acompanhamento de hábitos diários, definidos pelo usuário, funcionando como um *tracker* minimalista.
**Público-Alvo:** Estudantes, profissionais e qualquer pessoa que precise de uma ferramenta rápida e sem distrações visuais para monitorar sua rotina.

## ✨ Funcionalidades Principais

* Registro diário (sim ou não) de uma lista de hábitos pré-definida.
* Visualização do histórico completo de hábitos armazenados.
* Salvamento automático e local dos dados em formato JSON.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Armazenamento:** Arquivo JSON local
* **Qualidade e Automação:** `unittest` (Testes), `flake8` (Linting) e GitHub Actions (CI)

## 🚀 Como Executar

**1. Instalação / Preparação do Ambiente**
Certifique-se de ter o Python 3 instalado. Clone este repositório e configure o ambiente:

```bash
# Clone o repositório
git clone https://github.com/lucasmalinski/yaht
cd yaht

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # No Windows use: .venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

**2. Execução**
Para iniciar o tracker interativo via terminal, rode:

```Bash
python src/planner.py
```

## 🧪 Testes e Linting

Para garantir a confiabilidade e o padrão de código exigidos, este projeto utiliza testes automatizados e check's de linting.

**Executar os Testes Automatizados (unittest):**

```Bash
python -m unittest tests/test_planner.py
```

**Executar o teste de Linting (Ruff):**

```Bash
python -m ruff check src/ tests/
```

## 📦 Informações do Projeto

Versão Atual: `1.0.0`
Autor: `Lucas P. Malinski`
Disciplina: `Bootcamp II`
Repositório Público: [YAHT - Yet Another Habit Tracker](https://github.com/lucasmalinski/yaht)
