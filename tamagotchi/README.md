🐾 Tamagotchi em Python

Um jogo de **Tamagotchi desenvolvido em Python**, utilizando **Programação Orientada a Objetos (POO)** e executado pelo terminal.

O jogador pode criar e cuidar de um mascote virtual, alimentá-lo, fazê-lo dormir, limpá-lo, brincar com ele, acompanhar seus atributos, utilizar itens do inventário e salvar o progresso da partida em um arquivo JSON.


# 🎮 Sobre o projeto

O projeto consiste em um jogo de Tamagotchi no qual o jogador é responsável por manter seu mascote em boas condições.

O Tamagotchi possui quatro atributos principais:

* ⚡ Energia
* 🍖 Fome
* 😊 Alegria
* 🧼 Higiene

Esses atributos possuem valores entre **0 e 100**.

O jogador precisa realizar diferentes ações para manter o mascote saudável e evitar que seus atributos cheguem a valores que provoquem sua morte.

O sistema também possui:

* Inventário de alimentos e brinquedos;
* Controle de idade;
* Histórico de ações;
* Sistema de salvamento em JSON;
* Sistema de carregamento de partidas;
* Validação do nome do Tamagotchi;
* Controle de limites dos atributos;
* Arquitetura baseada em orientação a objetos.

---

# 💻 Tecnologias utilizadas

O projeto foi desenvolvido utilizando:

* **Python 3.10 ou superior**
* Programação Orientada a Objetos
* `dataclasses`
* JSON
* Biblioteca `pathlib`
* Biblioteca `typing`
* Biblioteca `json`

Não são necessárias bibliotecas externas.

---

# 📁 Estrutura do projeto

```text
projeto_tamagotchi/
│
├── main.py
├── tamagotchi.py
├── itens.py
├── inventario.py
├── tempo_vida.py
├── save_manager.py
├── requirements.txt
├── README.md
└── save_pet.json
```

O arquivo `save_pet.json` é criado automaticamente quando o jogador salva a partida.

---

# 📄 Descrição dos arquivos

## `main.py`

É o ponto de entrada do programa.

Responsável por:

* iniciar o jogo;
* carregar uma partida existente;
* criar um novo Tamagotchi;
* mostrar o status;
* mostrar o menu;
* receber as opções do jogador;
* executar as ações;
* mostrar o inventário;
* mostrar o histórico;
* salvar a partida.

---

## `tamagotchi.py`

Contém a classe principal:

```python
Tamagotchi
```

Essa classe controla:

* nome;
* energia;
* fome;
* alegria;
* higiene;
* estado de vida;
* histórico;
* inventário;
* idade;
* ações do jogador;
* condições de morte;
* conversão para dicionário;
* reconstrução a partir de dados salvos.

---

## `itens.py`

Contém as classes:

```python
Alimento
Brinquedo
```

Essas classes representam os objetos que podem ser armazenados no inventário.

---

## `inventario.py`

Contém a classe:

```python
Inventario
```

Responsável por:

* armazenar alimentos;
* armazenar brinquedos;
* controlar a capacidade máxima;
* adicionar itens;
* retirar itens;
* listar itens;
* converter o inventário para dicionário;
* reconstruir o inventário a partir de dados salvos.

---

## `tempo_vida.py`

Contém a classe:

```python
TempoVida
```

Responsável pelo controle da idade do Tamagotchi.

A idade é contabilizada em **turnos**.

---

## `save_manager.py`

Responsável pela persistência dos dados.

Possui duas funções principais:

```python
salvar_pet()
carregar_pet()
```

Os dados são armazenados no arquivo:

```text
save_pet.json
```

---

## `requirements.txt`

O projeto não possui dependências externas.

Todas as funcionalidades utilizadas pertencem à biblioteca padrão do Python.

---

## `README.md`

Arquivo de documentação do projeto.

---

# ⚙️ Como executar

## 1. Instalar o Python

Instale o Python 3.10 ou superior.

Depois, verifique a instalação:

```bash
python --version
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 --version
```

---

## 2. Abrir o projeto

Abra a pasta do projeto no Visual Studio Code ou em outro editor de código.

---

## 3. Abrir o terminal

No VS Code:

```text
Terminal → New Terminal
```

---

## 4. Executar o programa

Utilize:

```bash
python main.py
```

Ou:

```bash
python3 main.py
```

---

# 🎮 Como jogar

Ao executar o programa pela primeira vez, será solicitado o nome do Tamagotchi.

Exemplo:

```text
Digite o nome do Tamagotchi (3 a 20 caracteres): Bidu
```

O nome precisa possuir entre:

```text
3 e 20 caracteres
```

Após a criação, o Tamagotchi será inicializado.

---

# 📊 Atributos do Tamagotchi

Os atributos possuem valores entre `0` e `100`.

| Atributo | Valor inicial | Descrição                     |
| -------- | ------------: | ----------------------------- |
| Energia  |           100 | Energia disponível para ações |
| Fome     |            50 | Nível de fome                 |
| Alegria  |           100 | Nível de alegria              |
| Higiene  |           100 | Nível de higiene              |
| Idade    |             0 | Quantidade de turnos          |
| Vivo     |           Sim | Estado atual do Tamagotchi    |

Os valores são controlados pelas propriedades da classe `Tamagotchi`.

Por exemplo:

```python
pet.energia = 150
```

O sistema limita o valor para:

```text
100
```

Da mesma forma:

```python
pet.energia = -10
```

resulta em:

```text
0
```

Portanto:

```text
0 <= atributo <= 100
```

---

# 🕹️ Ações disponíveis

O menu principal possui as seguintes opções:

```text
1 - Alimentar
2 - Dormir
3 - Limpar
4 - Brincar
5 - Exibir inventário
6 - Passar um turno
7 - Ver histórico
8 - Salvar e sair
0 - Reiniciar Tamagotchi
```

---

## 🍖 1 - Alimentar

Ao alimentar o Tamagotchi:

* um alimento é retirado do inventário;
* a fome é reduzida de acordo com o alimento;
* a energia aumenta de acordo com o alimento;
* o sistema registra a ação no histórico;
* as condições de morte são verificadas.

O alimento padrão criado pelo sistema é:

```text
Ração
Energia: +20
Redução da fome: 20
```

Depois da ação, o `main.py` também executa:

```python
pet.passar_tempo()
```

Portanto, alimentar o Tamagotchi também faz o jogo avançar um turno.

---

## 😴 2 - Dormir

Ao dormir:

```text
Energia: +10
Fome: +10
```

A ação também é registrada no histórico e, depois, o programa avança um turno.

---

## 🧼 3 - Limpar

Ao limpar:

```text
Higiene: +20
```

A ação é registrada no histórico e o programa avança um turno.

---

## ⚽ 4 - Brincar

Ao brincar:

```text
Alegria: +10
Energia: -10
Fome: +10
```

O brinquedo padrão é:

```text
Bola
Alegria: +10
Custo de energia: 10
Aumento da fome: 10
```

Caso o Tamagotchi não tenha energia suficiente para brincar, o brinquedo retorna ao inventário.

Depois da ação, o programa também avança um turno.

---

## 🎒 5 - Exibir inventário

Mostra todos os alimentos e brinquedos disponíveis.

Exemplo:

```text
=== Inventário ===
- Alimento: Ração
- Brinquedo: Bola
==================
```

---

## ⏳ 6 - Passar um turno

Avança o tempo em um turno.

A cada turno:

```text
Fome      +10
Energia   -10
Alegria   -5
Higiene   -5
Idade     +1
```

Os valores continuam limitados entre `0` e `100`.

---

## 📜 7 - Ver histórico

O sistema registra as principais ações realizadas durante o jogo.

Exemplo:

```text
=== Histórico ===
- Tamagotchi criado.
- Bidu foi alimentado com Ração.
- Tempo atualizado: 1 turno(s).
- Bidu brincou com Bola.
- Tempo atualizado: 1 turno(s).
=================
```

O programa exibe os **10 eventos mais recentes**.

---

## 💾 8 - Salvar e sair

Salva o estado atual do Tamagotchi no arquivo:

```text
save_pet.json
```

Depois encerra o programa.

---

## 🔄 0 - Reiniciar Tamagotchi

Reinicia o Tamagotchi utilizando o mesmo nome.

Os atributos retornam aos valores iniciais:

```text
Energia: 100
Fome: 50
Alegria: 100
Higiene: 100
Idade: 0
Vivo: Sim
```

Um novo inventário também é criado contendo:

```text
Ração
Bola
```

---

# 🎒 Inventário

O inventário possui capacidade máxima de:

```text
10 itens
```

Ele pode armazenar dois tipos de objetos:

```text
Alimentos
Brinquedos
```

A quantidade total é calculada pela soma:

```text
quantidade de alimentos + quantidade de brinquedos
```

Quando a capacidade máxima é atingida, novos itens não são adicionados.

---

# 🍎 Classe Alimento

A classe `Alimento` possui os seguintes atributos:

| Atributo       | Tipo  |      Padrão |
| -------------- | ----- | ----------: |
| `nome`         | `str` | obrigatório |
| `energia`      | `int` |          20 |
| `reducao_fome` | `int` |          20 |

Exemplo:

```python
Alimento(
    nome="Ração",
    energia=20,
    reducao_fome=20
)
```

---

# 🧸 Classe Brinquedo

A classe `Brinquedo` possui:

| Atributo          | Tipo  |      Padrão |
| ----------------- | ----- | ----------: |
| `nome`            | `str` | obrigatório |
| `aumento_alegria` | `int` |          10 |
| `custo_energia`   | `int` |          10 |
| `aumento_fome`    | `int` |          10 |

Exemplo:

```python
Brinquedo(
    nome="Bola",
    aumento_alegria=10,
    custo_energia=10,
    aumento_fome=10
)
```

---

# ⏳ Sistema de tempo

A classe `TempoVida` controla a idade do Tamagotchi.

A idade começa em:

```text
0 turnos
```

Quando um turno passa:

```python
tempo_vida.avancar_dia()
```

a idade aumenta em `1`.

Também é possível avançar vários turnos:

```python
tempo_vida.avancar_dia(5)
```

Nesse caso:

```text
idade +5
```

Valores negativos são rejeitados:

```python
tempo_vida.avancar_dia(-1)
```

gera:

```text
ValueError
```

---

# ☠️ Condições de morte

O Tamagotchi morrerá quando qualquer um dos seguintes atributos chegar a `0`:

```text
Energia <= 0
Fome <= 0
Alegria <= 0
Higiene <= 0
```

A verificação é realizada pelo método:

```python
_verificar_morte()
```

Quando o Tamagotchi morre:

```text
vivo = False
```

e o sistema registra uma mensagem no histórico.

Exemplo:

```text
Bidu morreu aos 8 turnos.
```

Enquanto o Tamagotchi estiver morto, as ações não são executadas.

---

# 📜 Sistema de histórico

O Tamagotchi possui uma lista:

```python
historico
```

Ela armazena os eventos importantes do jogo.

Exemplos:

```text
Tamagotchi criado.
Bidu foi alimentado com Ração.
Bidu dormiu.
Bidu foi limpo.
Bidu brincou com Bola.
Tempo atualizado: 1 turno(s).
Bidu morreu aos 10 turnos.
```

---

# 💾 Salvamento e carregamento

O sistema utiliza o formato **JSON** para armazenar a partida.

O arquivo utilizado é:

```text
save_pet.json
```

---

## Salvar

A função:

```python
salvar_pet(pet)
```

converte o objeto `Tamagotchi` para um dicionário usando:

```python
pet.to_dict()
```

Depois os dados são gravados no arquivo JSON.

---

## Carregar

A função:

```python
carregar_pet()
```

verifica se existe um arquivo de salvamento.

Caso exista:

1. abre o arquivo;
2. lê o JSON;
3. transforma os dados em um dicionário;
4. cria um `Tamagotchi` usando `Tamagotchi.from_dict()`.

Caso o arquivo não exista:

```python
carregar_pet()
```

retorna:

```python
None
```

e o programa solicita a criação de um novo Tamagotchi.

---

# 🏗️ Orientação a objetos

O projeto utiliza diversos conceitos de Programação Orientada a Objetos.

## Encapsulamento

Os atributos:

```text
_energia
_fome
_alegria
_higiene
```

são protegidos e controlados por propriedades:

```python
@property
```

Isso permite controlar os valores antes de armazená-los.

---

## Composição

A classe `Tamagotchi` possui objetos das classes:

```text
TempoVida
Inventario
```

Representação:

```text
Tamagotchi
   │
   ├── TempoVida
   │
   └── Inventario
```

Esses objetos fazem parte da estrutura interna do Tamagotchi.

---

## Associação

O `Inventario` mantém coleções de:

```text
Alimento
Brinquedo
```

Representação:

```text
Inventario
   │
   ├── Alimento
   └── Brinquedo
```

---

## Abstração

Cada classe possui uma responsabilidade específica.

| Classe         | Responsabilidade             |
| -------------- | ---------------------------- |
| `Tamagotchi`   | Regras e estado do mascote   |
| `Inventario`   | Controle dos itens           |
| `Alimento`     | Representação dos alimentos  |
| `Brinquedo`    | Representação dos brinquedos |
| `TempoVida`    | Controle da idade            |
| `save_manager` | Persistência                 |
| `main`         | Interface e fluxo do jogo    |

---

## Persistência

O sistema utiliza serialização para transformar os objetos em estruturas compatíveis com JSON.

O processo é:

```text
Objeto Tamagotchi
       ↓
    to_dict()
       ↓
   Dicionário
       ↓
     JSON
       ↓
save_pet.json
```

Para carregar:

```text
save_pet.json
       ↓
     JSON
       ↓
  Dicionário
       ↓
  from_dict()
       ↓
Objeto Tamagotchi
```

---

# 📐 Diagrama UML

O sistema possui um diagrama UML representando as principais classes e seus relacionamentos.

Principais relacionamentos:

```text
Tamagotchi
    │
    ├── composição ──> Inventario
    │                       │
    │                       ├── Alimento
    │                       └── Brinquedo
    │
    └── composição ──> TempoVida
```

O módulo principal utiliza o `Tamagotchi`:

```text
main
  │
  └──> Tamagotchi
```

E o sistema de persistência trabalha com:

```text
save_manager
      │
      └──> Tamagotchi
```

---

# 🧪 Testes

Um teste simples pode verificar o controle dos limites dos atributos:

```python
from tamagotchi import Tamagotchi

pet = Tamagotchi("Bidu")

pet.energia = 150
assert pet.energia == 100

pet.energia = -10
assert pet.energia == 0

pet.fome = 80
assert pet.fome == 80

print("Testes aprovados!")
```

Para executar:

1. Crie um arquivo:

```text
testes.py
```

2. Coloque o código acima no arquivo.

3. Execute:

```bash
python testes.py
```

Resultado esperado:

```text
Testes aprovados!
```

---

# 🔧 Possíveis melhorias

O projeto pode receber novas funcionalidades no futuro, como:

* 🖥️ Interface gráfica com Tkinter;
* 🎮 Interface com Pygame;
* 🐾 Diferentes tipos de mascotes;
* 🍎 Mais tipos de alimentos;
* 🧸 Mais tipos de brinquedos;
* 📈 Sistema de evolução;
* 🏆 Sistema de conquistas;
* 🔊 Sons;
* 🎨 Animações;
* 👥 Suporte a múltiplos mascotes;
* 👤 Sistema de usuários;
* 🗄️ Banco de dados;
* 📊 Estatísticas da partida;
* 🌐 Interface web.

---

# 📚 Organização arquitetural

O projeto pode ser dividido em três partes principais:

```text
┌──────────────────────────┐
│     Interface / App      │
│                          │
│        main.py           │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│         Domínio          │
│                          │
│      Tamagotchi          │
│      Inventario          │
│      Alimento            │
│      Brinquedo           │
│      TempoVida           │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│       Persistência       │
│                          │
│     save_manager.py      │
│                          │
│     save_pet.json        │
└──────────────────────────┘
```

Essa separação facilita a manutenção e permite que cada parte do sistema tenha uma responsabilidade específica.

---

# 🎓 Finalidade acadêmica

O projeto foi desenvolvido para fins acadêmicos e educacionais, com o objetivo de praticar conceitos de:

* Programação Orientada a Objetos;
* Encapsulamento;
* Composição;
* Abstração;
* Organização de responsabilidades;
* Serialização;
* Persistência de dados;
* Arquitetura de software;
* Diagramas UML.

---

# 📜 Licença

Projeto desenvolvido para fins acadêmicos e educacionais.

Centro Universitário IESB.

---
