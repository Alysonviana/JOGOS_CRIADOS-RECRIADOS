from pet import Pet
from save_manager import salvar_pet, carregar_pet


def mostrar_status(pet: Pet):
    s = pet.status()
    print("\n=== Status do Tamagotchi ===")
    print(f"Nome: {s['nome']}")
    print(f"Idade (turnos): {s['idade']}")
    print(f"Fome: {s['fome']}")
    print(f"Sono: {s['sono']}")
    print(f"Higiene: {s['higiene']}")
    print(f"Felicidade: {s['felicidade']}")
    print(f"Vivo: {s['vivo']}")
    print("============================\n")


def menu():
    print("Ações disponíveis:")
    print("1 - Alimentar")
    print("2 - Dormir")
    print("3 - Limpar")
    print("4 - Brincar")
    print("5 - Passar 1 turno")
    print("6 - Salvar e sair")
    print("7 - Ver histórico recente")
    print("0 - Reiniciar pet (nascer de novo)")


def main():
    pet = carregar_pet()
    if pet is None:
        nome = input("Dê um nome ao seu Tamagotchi: ").strip()
        if not nome:
            nome = "Tamagotchi"
        pet = Pet(nome=nome)
        pet.nascer()
        print(f"{pet.nome} nasceu! Cuide bem dele.\n")
    else:
        print(f"Bem-vindo de volta, {pet.nome}!\n")

    while True:
        if not pet.vivo:
            print(f"{pet.nome} morreu. Fim de jogo.")
            op = input("Deseja nascer de novo? (s/n): ").strip().lower()
            if op == "s":
                pet.nascer()
                print(f"{pet.nome} nasceu de novo!")
            else:
                break

        mostrar_status(pet)
        menu()
        op = input("Escolha uma ação: ").strip()

        if op == "1":
            pet.alimentar()
        elif op == "2":
            pet.dormir()
        elif op == "3":
            pet.limpar()
        elif op == "4":
            pet.brincar()
        elif op == "5":
            pet.passar_tempo(1)
        elif op == "6":
            salvar_pet(pet)
            print("Jogo salvo. Até logo!")
            break
        elif op == "7":
            print("\nHistórico recente:")
            for linha in pet.historico[-10:]:
                print(" -", linha)
        elif op == "0":
            pet.nascer()
            print(f"{pet.nome} nasceu de novo!")
        else:
            print("Opção inválida.")

        # Pequena deterioração automática a cada ação
        pet.passar_tempo(1)


if __name__ == "__main__":
    main()