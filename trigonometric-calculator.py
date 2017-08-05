import math
import decimal


class Calculator():

    def __init__(self):
        self.first_argument = None
        self.second_argument = None
        self.mathematical_operation = None
        self.result = None
        self.continue_calculating = True
        self.one_argument_operations = ["cos", "sin", "tan", "sqrt"]
        self.two_argument_operations = ["+", "-", "*", "/", "%", "pow"]

    def addition(self):
        return self.first_argument + self.second_argument

    def subtraction(self):
        return self.first_argument - self.second_argument

    def multiplication(self):
        return self.first_argument * self.second_argument

    def division(self):
        return self.first_argument / self.second_argument

    def division_with_rest(self):
        return self.first_argument % self.second_argument

    def pow(self):
        return math.pow(self.first_argument, self.second_argument)

    def sqrt(self):
        return math.sqrt(self.first_argument)

    def sin(self):
        return math.sin(self.first_argument)

    def cos(self):
        return math.cos(self.first_argument)

    def tan(self):
        return math.tan(self.first_argument)

    def validate_input_argument(self, data):
        try:
            float(data)
            return True
        except ValueError:
            print("You have entered incorrect value! Please, try again.")
            return False

    def get_argument_input(self, argument):
        user_input = input("Please, enter the " + argument + " : ")
        is_input_valid = self.validate_input_argument(user_input)

        if is_input_valid:
            setattr(self, argument, float(user_input))
        else:
            self.get_argument_input(argument)

    def get_mathematical_operation(self):
        self.mathematical_operation = input("Please, choose the mathematical"
                                            " operation (+ - * / % pow sqrt "
                                            "cos sin tan): ")
        if self.mathematical_operation not in (self.one_argument_operations and
                                               self.two_argument_operations):
            print("You have entered incorrect mathematical operator! "
                  "Please, try again")
            self.get_mathematical_operation()

    def get_calculating_information(self):
        self.get_argument_input('first_argument')
        self.get_mathematical_operation()
        if self.mathematical_operation not in self.one_argument_operations:
            self.get_argument_input('second_argument')

    def calculation(self):
        choosed_operator = self.mathematical_operation

        if choosed_operator == "+":
            self.result = self.addition()
        elif choosed_operator == "-":
            self.result = self.subtraction()
        elif choosed_operator == "*":
            self.result = self.multiplication()
        elif choosed_operator == "/":
            self.result = self.division()
        elif choosed_operator == "%":
            self.result = self.division_with_rest()
        elif choosed_operator == "pow":
            self.result = self.pow()
        elif choosed_operator == "sqrt":
            self.result = self.sqrt()
        elif choosed_operator == "sin":
            self.result = self.sin()
        elif choosed_operator == "cos":
            self.result = self.cos()
        else:
            self.result = self.tan()

    def show_result(self):
        print("Your result is: " + "{0:.3f}".format(self.result))

    def ask_for_continue(self):
        user_continue_answer = input("Please, enter 'yes' if "
                                     "you want to calculate something else: ")

        if user_continue_answer != "yes":
            self.continue_calculating = False

    def implement_calculator(self):
        while self.continue_calculating is True:
            self.get_calculating_information()
            self.calculation()
            self.show_result()
            self.ask_for_continue()


if __name__ == '__main__':

    calculator = Calculator()
    calculator.implement_calculator()
