# 📓 CHANGELOG

## [1.2.0] - 11/04/2026
### Funcionalidades
- **Configuração Externa:** Agora os hábitos são carregados de um arquivo `habits.txt`, permitindo personalização sem mexer no código.  Implementada lista de hábitos padrão (fallback) caso o arquivo de configuração não seja encontrado.

## [1.1.0] - 11/04/2026
### Funcionalidades
- **Validação:** Atualizado o formato de data aceito para `dd-mm-YYYY` em `planner.py` e `test_planner.py`.

### Arquitetura e Refatoração
- **Pathlib:** Migração do antigo `os.path` para `pathlib.Path`, para caminhos de arquivo mais robustos e portáveis entre sistemas.
- **Persistência:** Movimentação do arquivo de histórico para uma pasta dedicada `/data/`, melhorando a organização do projeto.

### Higiene e Manutenção
- **Gitignore:** Adicionada a pasta `/data/` e os caches do Ruff ao `.gitignore` para manter o repositório limpo e focado no código-fonte.

## [1.0.0] - 10/04/2026
###  Lançamento Inicial
- **CLI Habit Tracker:** Versão inicial funcional com registro e visualização de hábitos em JSON.
- **Qualidade e Testes:** Implementação de suíte de testes unitários com `unittest` e análise estática via `Ruff`.
- **Automação (CI):** Configuração de pipeline no GitHub Actions para validação automática de cada commit.
- **Documentação:** Criação de `README.md` detalhado com instruções de instalação, execução e testes.