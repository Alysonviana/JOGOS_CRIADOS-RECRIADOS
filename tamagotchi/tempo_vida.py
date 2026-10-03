from dataclasses import dataclass


@dataclass
class TempoVida:
    idade: int = 0

    def avancar_dia(self, quantidade: int = 1) -> None:
        if quantidade < 0:
            raise ValueError("A quantidade de dias não pode ser negativa.")

        self.idade += quantidade

    def reiniciar(self) -> None:
        self.idade = 0