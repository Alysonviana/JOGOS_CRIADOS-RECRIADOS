# Tamagotchi em Python (VS Code)

Um jogo simples de Tamagotchi rodando no terminal, feito em Python puro.

## Estrutura do projeto

- `pet.py` – lógica do bichinho (atributos, ações, tempo, vida/morte)
- `save_manager.py` – salvar/carregar estado em JSON
- `main.py` – loop do jogo e interface no terminal
- `requirements.txt` – dependências (vazio)
- `README.md` – esta documentação

## Requisitos

- Python 3.10+ recomendado
- Visual Studio Code (opcional, mas recomendado)

## Como rodar no VS Code

1. Instale Python: https://python.org (marque “Add to PATH” no Windows).
2. Instale o VS Code: https://code.visualstudio.com
3. No VS Code, instale a extensão “Python” (Microsoft).
4. Abra a pasta do projeto no VS Code (`File > Open Folder`).
5. Abra o terminal integrado: `Terminal > New Terminal` (ou `Ctrl+``).
6. (Opcional) Crie ambiente virtual:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```
7. Rode o jogo:
   ```bash
   python main.py
   ```
   Ou abra `main.py` e clique no botão “Run Python File in Terminal” (play no topo direito). [11][12][13]

## Regras básicas do jogo

- Atributos: fome, sono, higiene, felicidade (0–100).
- Ações:
  - Alimentar: reduz fome, aumenta levemente felicidade.
  - Dormir: reduz sono, aumenta felicidade.
  - Limpar: reduz higiene, aumenta felicidade.
  - Brincar: aumenta fome e sono, reduz felicidade (diversão cansa).
- A cada turno:
  - Fome, sono e higiene aumentam.
  - Felicidade varia conforme estado geral.
- Condições de morte:
  - Qualquer atributo (fome, sono, higiene) ≥ 100
  - Felicidade ≤ 0

## Salvamento

- O jogo salva automaticamente ao escolher “Salvar e sair”.
- O arquivo `save_pet.json` guarda o estado atual.
- Ao reiniciar, o jogo carrega automaticamente se existir save.

## Extensões possíveis

- Interface gráfica com `pygame` ou `tkinter`.
- Mais ações (comprar itens, evoluir, mini-games).
- Sistema de conquistas e estatísticas.

## Licença

Use como quiser (código de exemplo educacional).