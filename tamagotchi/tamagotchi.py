from dataclasses import dataclass, field
from typing import Optional

from inventario import Inventario
from itens import Alimento, Brinquedo
from tempo_vida import TempoVida


@dataclass
class Tamagotchi:
    nome: str
    _energia: int = field(default=100, repr=False)
    _fome: int = field(default=50, repr=False)
    _alegria: int = field(default=100, repr=False)
    _higiene: int = field(default=100, repr=False)
    vivo: bool = True
    historico: list[str] = field(default_factory=list)

    tempo_vida: TempoVida = field(default_factory=TempoVida)
    inventario: Inventario = field(default_factory=Inventario)

    MINIMO = 0
    MAXIMO = 100

    def __post_init__(self) -> None:
        self.nome = self.nome.strip()

        if not 3 <= len(self.nome) <= 20:
            raise ValueError(
                "O nome deve possuir entre 3 e 20 caracteres."
            )

        self.energia = self._energia
        self.fome = self._fome
        self.alegria = self._alegria
        self.higiene = self._higiene

    @staticmethod
    def _limitar(valor: int) -> int:
        return max(Tamagotchi.MINIMO, min(Tamagotchi.MAXIMO, valor))

    @property
    def energia(self) -> int:
        return self._energia

    @energia.setter
    def energia(self, valor: int) -> None:
        self._energia = self._limitar(valor)

    @property
    def fome(self) -> int:
        return self._fome

    @fome.setter
    def fome(self, valor: int) -> None:
        self._fome = self._limitar(valor)

    @property
    def alegria(self) -> int:
        return self._alegria

    @alegria.setter
    def alegria(self, valor: int) -> None:
        self._alegria = self._limitar(valor)

    @property
    def higiene(self) -> int:
        return self._higiene

    @higiene.setter
    def higiene(self, valor: int) -> None:
        self._higiene = self._limitar(valor)

    @property
    def idade(self) -> int:
        return self.tempo_vida.idade

    def registrar(self, mensagem: str) -> None:
        self.historico.append(mensagem)

    def nascer(self) -> None:
        self.energia = 100
        self.fome = 50
        self.alegria = 100
        self.higiene = 100
        self.vivo = True
        self.tempo_vida.reiniciar()
        self.inventario = Inventario()
        self.historico = ["Tamagotchi criado."]

        self.inventario.adicionar_alimento(
            Alimento(nome="Ração", energia=20, reducao_fome=20)
        )
        self.inventario.adicionar_brinquedo(
            Brinquedo(
                nome="Bola",
                aumento_alegria=10,
                custo_energia=10,
                aumento_fome=10,
            )
        )

    def esta_vivo(self) -> bool:
        return self.vivo

    def alimentar(self, alimento: Optional[Alimento] = None) -> bool:
        if not self.vivo:
            self.registrar("Ação recusada: o Tamagotchi está morto.")
            return False

        if alimento is None:
            alimento = self.inventario.obter_alimento()

        if alimento is None:
            self.registrar("Não há alimento disponível.")
            return False

        self.fome -= alimento.reducao_fome
        self.energia += alimento.energia

        self.registrar(
            f"{self.nome} foi alimentado com {alimento.nome}."
        )

        self._verificar_morte()
        return True

    def brincar(self, brinquedo: Optional[Brinquedo] = None) -> bool:
        if not self.vivo:
            self.registrar("Ação recusada: o Tamagotchi está morto.")
            return False

        if brinquedo is None:
            brinquedo = self.inventario.obter_brinquedo()

        if brinquedo is None:
            self.registrar("Não há brinquedo disponível.")
            return False

        if self.energia < brinquedo.custo_energia:
            self.registrar(
                "Brincadeira recusada: energia insuficiente."
            )
            self.inventario.brinquedos.insert(0, brinquedo)
            return False

        self.alegria += brinquedo.aumento_alegria
        self.energia -= brinquedo.custo_energia
        self.fome += brinquedo.aumento_fome

        self.registrar(
            f"{self.nome} brincou com {brinquedo.nome}."
        )

        self._verificar_morte()
        return True

    def dormir(self) -> bool:
        if not self.vivo:
            self.registrar("Ação recusada: o Tamagotchi está morto.")
            return False

        self.energia += 10
        self.fome += 10

        self.registrar(f"{self.nome} dormiu.")
        self._verificar_morte()
        return True

    def limpar(self) -> bool:
        if not self.vivo:
            self.registrar("Ação recusada: o Tamagotchi está morto.")
            return False

        self.higiene += 20
        self.registrar(f"{self.nome} foi limpo.")
        self._verificar_morte()
        return True

    def passar_tempo(self, quantidade: int = 1) -> None:
        if not self.vivo:
            return

        for _ in range(quantidade):
            self.tempo_vida.avancar_dia()
            self.fome += 10
            self.energia -= 10
            self.alegria -= 5
            self.higiene -= 5

        self.registrar(
            f"Tempo atualizado: {quantidade} turno(s)."
        )
        self._verificar_morte()

    def _verificar_morte(self) -> None:
        if (
            self.fome <= 0
            or self.energia <= 0
            or self.alegria <= 0
            or self.higiene <= 0
        ):
            if self.vivo:
                self.vivo = False
                self.registrar(
                    f"{self.nome} morreu aos {self.idade} turnos."
                )

    def status(self) -> dict:
        return {
            "nome": self.nome,
            "idade": self.idade,
            "energia": self.energia,
            "fome": self.fome,
            "alegria": self.alegria,
            "higiene": self.higiene,
            "vivo": self.vivo,
        }

    def to_dict(self) -> dict:
        return {
            "nome": self.nome,
            "energia": self.energia,
            "fome": self.fome,
            "alegria": self.alegria,
            "higiene": self.higiene,
            "vivo": self.vivo,
            "historico": self.historico,
            "tempo_vida": {
                "idade": self.idade,
            },
            "inventario": self.inventario.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Tamagotchi":
        tempo = data.get("tempo_vida", {})
        inventario = data.get("inventario", {})

        pet = cls(
            nome=data["nome"],
            _energia=data.get("energia", 100),
            _fome=data.get("fome", 50),
            _alegria=data.get("alegria", 100),
            _higiene=data.get("higiene", 100),
            vivo=data.get("vivo", True),
            historico=data.get("historico", []),
            tempo_vida=TempoVida(
                idade=tempo.get("idade", 0)
            ),
            inventario=Inventario.from_dict(inventario),
        )

        return pet