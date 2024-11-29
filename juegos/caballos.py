import random, time, os
from colorama import Fore, Back, Style, init


def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Por favor, introduce un número entero válido.")


def run_race(N, L):
    M = [0 for _ in range(N)]
    colors = [
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
    ]
    init(autoreset=True)

    while max(M) < L:
        M[random.randint(0, N - 1)] += 1
        time.sleep(0.01)
        os.system("cls" if os.name == "nt" else "clear")  # Limpia la consola
        print(f"i: {' '*98} | Meta: {L}")
        for i in range(N):
            color = colors[i % len(colors)]  # Selecciona un color de la lista
            print(color + f"{i+1}: {' '*int(M[i]/L*100)}{i+1}🐎")
    print(f"¡Ganó el caballo {M.index(max(M))+1}!")


def main():
    N = get_input("N: ")
    L = get_input("L: ")
    run_race(N, L)


if __name__ == "__main__":
    main()
