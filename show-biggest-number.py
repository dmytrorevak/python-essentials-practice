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
        elif self.user_oparation == "3":
            ShowAllKindsOfNumbers().implement_all_kinds_of_numbers()
        else:
            print("You have entered incorrect number!")


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
            self.user_numbers.append(int(current_user_number))

    def show_biggest_number(self):
        print("The biggest number is: " + str(self.biggest_number))

    def implement_biggest_number(self):
        self.ask_user_numbers()
        self.get_biggest_number()
        self.show_biggest_number()


class ShowBiggestOfFiveNumbers(ShowBiggestNumbers):

    def __init__(self):
        super().__init__()
        self.count_of_comparing_numbers = 5


class ShowAllKindsOfNumbers(ShowBiggestNumbers):

    def __init__(self):

        super().__init__()

        self.continue_asking_numbers = True
        self.smallest_number = None
        self.sum_of_numbers = None
        self.even_numbers = None
        self.odd_numbers = None
        self.positive_numbers = None

    def stop_asking_numbers(self):
        self.continue_asking_numbers = False

    def ask_user_numbers(self):
        while self.continue_asking_numbers:
            current_user_number = input("Enter the number: ")

            if current_user_number == 'x':
                self.stop_asking_numbers()
            else:
                self.user_numbers.append(int(current_user_number))

    def get_smallest_number(self):
        self.smallest_number = min(self.user_numbers)

    def show_smallest_number(self):
        print("The smallest number is: " + str(self.smallest_number))

    def get_sum_of_numbers(self):
        self.sum_of_numbers = sum(self.user_numbers)

    def show_sum_of_numbers(self):
        print("The sum number is: " + str(self.sum_of_numbers))

    def get_even_numbers(self):
        self.even_numbers = [i for i in self.user_numbers if i % 2 == 0]

    def show_amount_of_even_numbers(self):
        print("Amount of even numbers is: " + str(len(self.even_numbers)))

    def get_odd_numbers(self):
        self.odd_numbers = [i for i in self.user_numbers if i % 2 != 0]

    def show_amount_of_odd_numbers(self):
        print("Amount of odd numbers is: " + str(len(self.odd_numbers)))

    def get_positive_numbers(self):
        self.positive_numbers = [i for i in self.user_numbers if i > 0]

    def show_amount_of_positive_numbers(self):
        print("Amount of positive numbers "
              "is: " + str(len(self.positive_numbers)))

    def implement_all_kinds_of_numbers(self):
        super().implement_biggest_number()
        self.ask_user_numbers()
        self.get_smallest_number()
        self.get_sum_of_numbers()
        self.get_even_numbers()
        self.get_odd_numbers()
        self.get_positive_numbers()
        self.show_smallest_number()
        self.show_sum_of_numbers()
        self.show_amount_of_even_numbers()
        self.show_amount_of_odd_numbers()
        self.show_amount_of_positive_numbers()


if __name__ == '__main__':

    app_controller = AppController()
    app_controller.implement_needed_operation()
