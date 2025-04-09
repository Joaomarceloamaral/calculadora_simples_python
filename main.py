from modules.menu_functions.menu_option import get_menu_option
from modules.menu_functions.execute_option import execute_option


def main():

    option = "0"
    while option != "s":

        option = get_menu_option()

        result = execute_option(option)

        if (option != "s") & (result is not False):

            print(f"Resultado: {result}\n")

    print("\n\nObrigado por utilizar minha calculadora! :)\n")
    print("Saindo...\n")


if __name__ == "__main__":
    main()
