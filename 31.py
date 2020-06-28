"""
Разработка прототипа приложения “Калькулятор”, реализующего паттерн MVC (Model View Controller).
"""
class Model:
    @staticmethod
    def pls(a, b):
        return a + b

    @staticmethod
    def min(a, b):
        return a - b

    @staticmethod
    def mpy(a, b):
        return a * b

    @staticmethod
    def dev(a, b):
        return a / b


class View:
    @staticmethod
    def get_operation():
        operation = input("set operation (+, -, *, /): ")
        if operation == "+":
            return Model.pls
        elif operation == "-":
            return Model.min
        elif operation == "*":
            return Model.mpy
        elif operation == "/":
            return Model.dev
        else:
            return None

    @staticmethod
    def get_arguments():
        """
        Throws (TypeError, ValueError)
        :return:
        """
        a = float(input("set first argument: "))
        b = float(input("set second argument: "))
        return a, b

    @staticmethod
    def show_result(result):
        print("Result:", result)


class Controller:
    @staticmethod
    def run():
        operation = View.get_operation()

        try:
            a, b = View.get_arguments()
        except (TypeError, ValueError):
            print("Invalid argument")
            exit()

        result = operation(a, b)
        View.show_result(result)
