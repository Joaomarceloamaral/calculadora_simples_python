from modules.operations_functions.sum import sum_two_numbers
from modules.operations_functions.subtraction import subtract_two_numbers
from modules.operations_functions.multiplication import multiplicate_two_numbers
from modules.operations_functions.division import divide_two_numbers


def execute_option(option: str):

    match option:

        case "1":
            print("\n\n---------------------- Soma ----------------------")

            number1 = float(input("Insira o primeiro numero da soma: "))
            number2 = float(input("Insira o segundo numero da soma: "))

            result = sum_two_numbers(number1, number2)

            return result

        case "2":
            print("\n\n---------------------- Subtração ----------------------")

            number1 = float(input("Insira o primeiro numero da subtração: "))
            number2 = float(input("Insira o segundo numero da subtração: "))

            result = subtract_two_numbers(number1, number2)

            return result

        case "3":
            print("\n\n---------------------- Multiplicação ----------------------")

            number1 = float(input("Insira o primeiro numero da multiplicação: "))
            number2 = float(input("Insira o segundo numero da multiplicação: "))

            result = multiplicate_two_numbers(number1, number2)

            return result

        case "4":
            print("\n\n---------------------- Divisão ----------------------")

            number1 = float(input("Insira o primeiro numero da divisão: "))
            number2 = float(input("Insira o segundo numero da divisão: "))

            try:
                result = divide_two_numbers(number1, number2)

            except ZeroDivisionError:

                print("Divisão por zero não pode ser realizada!\n")
                return False

            else:

                return result
