import json
from pathlib import Path
from pet import Pet


SAVE_FILE = Path("save_pet.json")


def salvar_pet(pet: Pet, caminho: Path = SAVE_FILE):
    with caminho.open("w", encoding="utf-8") as f:
        json.dump(pet.to_dict(), f, indent=2, ensure_ascii=False)


def carregar_pet(caminho: Path = SAVE_FILE) -> Pet | None:
    if not caminho.exists():
        return None
    with caminho.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return Pet.from_dict(data)
