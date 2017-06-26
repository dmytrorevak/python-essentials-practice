class Calculator():

    __first_argument = None
    __second_argument = None
    __mathematical_operation = None
    __result = None
    __continue_calculating = True

    def __addition(self):
        return self.__first_argument + self.__second_argument

    def __subtraction(self):
        return self.__first_argument - self.__second_argument

    def __multiplication(self):
        return self.__first_argument * self.__second_argument

    def __division(self):
        return self.__first_argument / self.__second_argument

    def __division_with_rest(self):
        return self.__first_argument % self.__second_argument

    def __get_input_information(self):
        self.__first_argument = float(input("Please, "
                                            "enter the first argument: "))

        self.__mathematical_operation = input("Please, choose the mathematical"
                                              " operation (+ - * / %): ")

        self.__second_argument = float(input("Please, "
                                             "enter the second argument: "))

    def __calculation(self):
        choosed_operator = self.__mathematical_operation

        if choosed_operator == "+":
            self.__result = self.__addition()
        elif choosed_operator == "-":
            self.__result = self.__subtraction()
        elif choosed_operator == "*":
            self.__result = self.__multiplication()
        elif choosed_operator == "/":
            self.__result = self.__division()
        elif choosed_operator == "%":
            self.__result = self.__division_with_rest()
        else:
            print("You have entered incorrect mathematical operator!")

    def __show_result(self):
        print(self.__result)

    def __ask_for_continue(self):
        user_continue_answer = input("Please, enter 'yes' if "
                                     "you want to calculate something else: ")

        if user_continue_answer != "yes":
            self.__continue_calculating = False

    def implement_calculator(self):
        while self.__continue_calculating is True:
            self.__get_input_information()
            self.__calculation()
            self.__show_result()
            self.__ask_for_continue()


if __name__ == '__main__':

    calculator = Calculator()
    calculator.implement_calculator()
    # calculator.__addition()