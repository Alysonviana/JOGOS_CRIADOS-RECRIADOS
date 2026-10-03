from dataclasses import dataclass, field
from typing import List

from itens import Alimento, Brinquedo


@dataclass
class Inventario:
    capacidade: int = 10
    alimentos: List[Alimento] = field(default_factory=list)
    brinquedos: List[Brinquedo] = field(default_factory=list)

    @property
    def quantidade_itens(self) -> int:
        return len(self.alimentos) + len(self.brinquedos)

    def adicionar_alimento(self, alimento: Alimento) -> bool:
        if self.quantidade_itens >= self.capacidade:
            return False

        self.alimentos.append(alimento)
        return True

    def adicionar_brinquedo(self, brinquedo: Brinquedo) -> bool:
        if self.quantidade_itens >= self.capacidade:
            return False

        self.brinquedos.append(brinquedo)
        return True

    def obter_alimento(self, indice: int = 0) -> Alimento | None:
        if not self.alimentos:
            return None

        if indice < 0 or indice >= len(self.alimentos):
            return None

        return self.alimentos.pop(indice)

    def obter_brinquedo(self, indice: int = 0) -> Brinquedo | None:
        if not self.brinquedos:
            return None

        if indice < 0 or indice >= len(self.brinquedos):
            return None

        return self.brinquedos.pop(indice)

    def listar_itens(self) -> list[str]:
        itens = []

        for alimento in self.alimentos:
            itens.append(f"Alimento: {alimento.nome}")

        for brinquedo in self.brinquedos:
            itens.append(f"Brinquedo: {brinquedo.nome}")

        return itens

    def to_dict(self) -> dict:
        return {
            "capacidade": self.capacidade,
            "alimentos": [
                {
                    "nome": alimento.nome,
                    "energia": alimento.energia,
                    "reducao_fome": alimento.reducao_fome,
                }
                for alimento in self.alimentos
            ],
            "brinquedos": [
                {
                    "nome": brinquedo.nome,
                    "aumento_alegria": brinquedo.aumento_alegria,
                    "custo_energia": brinquedo.custo_energia,
                    "aumento_fome": brinquedo.aumento_fome,
                }
                for brinquedo in self.brinquedos
            ],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Inventario":
        inventario = cls(capacidade=data.get("capacidade", 10))

        for item in data.get("alimentos", []):
            inventario.alimentos.append(
                Alimento(
                    nome=item["nome"],
                    energia=item.get("energia", 20),
                    reducao_fome=item.get("reducao_fome", 20),
                )
            )

        for item in data.get("brinquedos", []):
            inventario.brinquedos.append(
                Brinquedo(
                    nome=item["nome"],
                    aumento_alegria=item.get("aumento_alegria", 10),
                    custo_energia=item.get("custo_energia", 10),
                    aumento_fome=item.get("aumento_fome", 10),
                )
            )

        return inventario