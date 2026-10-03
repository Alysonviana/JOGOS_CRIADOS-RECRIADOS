from save_manager import carregar_pet, salvar_pet
from tamagotchi import Tamagotchi


def mostrar_status(pet: Tamagotchi) -> None:
    status = pet.status()

    print("\n=== Status do Tamagotchi ===")
    print(f"Nome: {status['nome']}")
    print(f"Idade: {status['idade']} turno(s)")
    print(f"Energia: {status['energia']}")
    print(f"Fome: {status['fome']}")
    print(f"Alegria: {status['alegria']}")
    print(f"Higiene: {status['higiene']}")
    print(f"Vivo: {'Sim' if status['vivo'] else 'Não'}")
    print("============================\n")


def mostrar_menu() -> None:
    print("1 - Alimentar")
    print("2 - Dormir")
    print("3 - Limpar")
    print("4 - Brincar")
    print("5 - Exibir inventário")
    print("6 - Passar um turno")
    print("7 - Ver histórico")
    print("8 - Salvar e sair")
    print("0 - Reiniciar Tamagotchi")


def mostrar_inventario(pet: Tamagotchi) -> None:
    itens = pet.inventario.listar_itens()

    print("\n=== Inventário ===")

    if not itens:
        print("Inventário vazio.")
    else:
        for item in itens:
            print(f"- {item}")

    print("==================\n")


def main() -> None:
    pet = carregar_pet()

    if pet is None:
        while True:
            nome = input(
                "Digite o nome do Tamagotchi "
                "(3 a 20 caracteres): "
            ).strip()

            try:
                pet = Tamagotchi(nome)
                pet.nascer()
                break
            except ValueError as erro:
                print(f"Erro: {erro}")

        print(f"\n{pet.nome} nasceu!")
    else:
        print(f"\nBem-vindo de volta, {pet.nome}!")

    while True:
        if not pet.vivo:
            print(f"\n{pet.nome} morreu. Fim de jogo.")
            opcao = input(
                "Deseja criar um novo Tamagotchi? (s/n): "
            ).strip().lower()

            if opcao == "s":
                pet.nascer()
                print(f"{pet.nome} nasceu novamente!")
                continue

            break

        mostrar_status(pet)
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            pet.alimentar()
            pet.passar_tempo()

        elif opcao == "2":
            pet.dormir()
            pet.passar_tempo()

        elif opcao == "3":
            pet.limpar()
            pet.passar_tempo()

        elif opcao == "4":
            pet.brincar()
            pet.passar_tempo()

        elif opcao == "5":
            mostrar_inventario(pet)

        elif opcao == "6":
            pet.passar_tempo()

        elif opcao == "7":
            print("\n=== Histórico ===")
            for evento in pet.historico[-10:]:
                print(f"- {evento}")
            print("=================\n")

        elif opcao == "8":
            salvar_pet(pet)
            print("Jogo salvo. Até a próxima!")
            break

        elif opcao == "0":
            pet.nascer()
            print(f"{pet.nome} foi reiniciado.")

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()