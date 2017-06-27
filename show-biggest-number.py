class AppController():

    def __init__(self):
        self.user_oparation = None

    def ask_user_operation(self):
        self.user_oparation = input("Enter the operation number "
                                    "you do prefer which (1 2 3): ")

    def implement_needed_operation(self):

        self.ask_user_operation()

        if self.user_oparation == "1":
            ShowBiggestNumbers().implement_biggest_number()
        elif self.user_oparation == "2":
            ShowBiggestOfFiveNumbers().implement_biggest_number()


class ShowBiggestNumbers():

    def __init__(self):
        self.user_numbers = []
        self.biggest_number = None
        self.count_of_comparing_numbers = 2

    def get_biggest_number(self):
        self.biggest_number = max(self.user_numbers)

    def ask_user_numbers(self):
        for i in range(self.count_of_comparing_numbers):
            current_user_number = input("Enter the " + str(i + 1) +
                                        " number: ")
            self.user_numbers.append(current_user_number)

    def show_biggest_number(self):
        print("The biggest number is: " + str(self.biggest_number))

    def implement_biggest_number(self):
        self.ask_user_numbers()
        self.get_biggest_number()
        self.show_biggest_number()


class ShowBiggestOfFiveNumbers(ShowBiggestNumbers):
    def __init__(self):
        ShowBiggestNumbers.__init__(self)
        self.count_of_comparing_numbers = 5


if __name__ == '__main__':

    app_controller = AppController()
    app_controller.implement_needed_operation()
