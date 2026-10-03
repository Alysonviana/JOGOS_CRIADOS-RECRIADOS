import random
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Pet:
    nome: str
    fome: int = 50
    sono: int = 50
    higiene: int = 50
    felicidade: int = 50
    idade: int = 0  # em "turnos"
    vivo: bool = True
    historico: list = field(default_factory=list)

    LIMITES = {"fome": 100, "sono": 100, "higiene": 100, "felicidade": 100}

    def nascer(self):
        """Inicializa o pet recém-nascido."""
        self.fome = 30
        self.sono = 20
        self.higiene = 10
        self.felicidade = 70
        self.idade = 0
        self.vivo = True
        self.historico = ["Nasceu!"]

    def alimentar(self):
        if not self.vivo:
            return
        self.fome = max(0, self.fome - 25)
        self.felicidade = min(self.LIMITES["felicidade"], self.felicidade + 5)
        self.historico.append(f"{self.nome} comeu.")

    def dormir(self):
        if not self.vivo:
            return
        self.sono = max(0, self.sono - 30)
        self.felicidade = min(self.LIMITES["felicidade"], self.felicidade + 3)
        self.historico.append(f"{self.nome} dormiu.")

    def limpar(self):
        if not self.vivo:
            return
        self.higiene = max(0, self.higiene - 35)
        self.felicidade = min(self.LIMITES["felicidade"], self.felicidade + 4)
        self.historico.append(f"{self.nome} foi limpo.")

    def brincar(self):
        if not self.vivo:
            return
        if self.fome > 70 or self.sono > 70:
            self.historico.append(f"{self.nome} está muito cansado/faminto para brincar.")
            return
        self.felicidade = max(0, self.felicidade - 10)
        self.fome = min(self.LIMITES["fome"], self.fome + 10)
        self.sono = min(self.LIMITES["sono"], self.sono + 10)
        self.historico.append(f"{self.nome} brincou.")

    def passar_tempo(self, turnos: int = 1):
        """Avança o tempo e deteriora atributos."""
        if not self.vivo:
            return
        for _ in range(turnos):
            self.idade += 1
            self.fome = min(self.LIMITES["fome"], self.fome + random.randint(5, 10))
            self.sono = min(self.LIMITES["sono"], self.sono + random.randint(3, 8))
            self.higiene = min(self.LIMITES["higiene"], self.higiene + random.randint(4, 9))
            # Felicidade cai se atributos estiverem ruins
            if self.fome > 70 or self.sono > 70 or self.higiene > 70:
                self.felicidade = max(0, self.felicidade - random.randint(3, 7))
            else:
                self.felicidade = min(self.LIMITES["felicidade"], self.felicidade + random.randint(0, 2))
        self._checar_vida()

    def _checar_vida(self):
        """Verifica condições de morte."""
        if self.fome >= 100 or self.sono >= 100 or self.higiene >= 100 or self.felicidade <= 0:
            self.vivo = False
            self.historico.append(f"{self.nome} morreu aos {self.idade} turnos.")

    def status(self) -> dict:
        return {
            "nome": self.nome,
            "fome": self.fome,
            "sono": self.sono,
            "higiene": self.higiene,
            "felicidade": self.felicidade,
            "idade": self.idade,
            "vivo": self.vivo,
        }

    def to_dict(self) -> dict:
        return {
            "nome": self.nome,
            "fome": self.fome,
            "sono": self.sono,
            "higiene": self.higiene,
            "felicidade": self.felicidade,
            "idade": self.idade,
            "vivo": self.vivo,
            "historico": self.historico,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Pet":
        return cls(
            nome=data["nome"],
            fome=data["fome"],
            sono=data["sono"],
            higiene=data["higiene"],
            felicidade=data["felicidade"],
            idade=data["idade"],
            vivo=data["vivo"],
            historico=data.get("historico", []),
        )

    