from dataclasses import dataclass


@dataclass
class Alimento:
    nome: str
    energia: int = 20
    reducao_fome: int = 20


@dataclass
class Brinquedo:
    nome: str
    aumento_alegria: int = 10
    custo_energia: int = 10
    aumento_fome: int = 10