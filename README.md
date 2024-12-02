# QXD0099 - Desenvolvimento de Software para Persistência

Bem-vindo ao repositório de projetos práticos da disciplina **QXD0099**, oferecida pela Universidade Federal do Ceará, Campus Quixadá, e ministrada pelo Prof. Francisco Victor da Silva Pinheiro. Aqui você encontra informações sobre instalação, execução e descrição do projeto principal.

## Sumário

- [Instalação](#instalação)
- [Execução](#execução)
- [Sobre](#sobre)
- [Descrição da Entidade](#descrição-da-entidade)

## Instalação

### Passo 1: Instale as dependências
Execute o comando abaixo para instalar todas as dependências necessárias:
```bash
pip install -r requirements.txt
```

### Passo 2: Ative o ambiente virtual

#### Linux/macOS:
```bash
source venv/bin/activate
```

#### Windows:
```bash
venv\Scripts\activate
```

## Execução

### Inicie a aplicação
Para iniciar a aplicação, use o seguinte comando:
```bash
uvicorn src.main:app --reload
```

## Sobre

### Magic: The Gathering - Virtual Card Game Database

Este projeto consiste em um banco de dados para gerenciar cartas do jogo Magic: The Gathering, possibilitando organização e consulta rápida de cartas por suas características.

## Descrição da Entidade

### Carta

Cada carta no jogo possui atributos que descrevem suas características e funcionalidade. Veja os detalhes abaixo:

- **id**: Identificador único da carta (int).
- **nome**: Nome da carta (str).
- **tipo**: Tipo da carta (str).
  - 🔧 **Artifact**: Representa equipamentos ou itens mágicos.
  - 💖 **Creature**: Criaturas que podem atacar e bloquear.
  - 🌌 **Enchantment**: Efeitos permanentes que alteram o campo de batalha.
  - ⚡ **Instant**: Feitiços que podem ser jogados a qualquer momento.
  - ✨ **Sorcery**: Feitiços que só podem ser jogados no seu turno principal.
  - 🎭 **Battle**: Um tipo especial de carta que adiciona desafios dinâmicos.
  - 🌠 **Planeswalker**: Personagens poderosos com habilidades únicas.
  - 🌱 **Land**: Fontes de mana para conjurar feitiços.
- **custo**: Custo de mana para conjurar a carta (int).
- **cor**: Cor da carta (str).
  - Branco (💜), Azul (💙), Preto (⚫), Vermelho (🔴), Verde (💚), ou Incolor.
- **rarity**: Raridade da carta (str). Exemplos: Comum, Incomum, Rara, Mítica.
- **habilidade**: Descrição da habilidade especial da carta (str).

---

Divirta-se explorando o universo de Magic: The Gathering com seu banco de dados personalizado! 🎮

