class TextParser():

    def __init__(self):
        self.file = None
        self.amount_of_lines = None

    def open_file(self, file_to_open):
        self.file = open(file_to_open)

    def count_lines(self):

        lines_counter = 0

        for line in self.file:
            lines_counter += 1

        self.amount_of_lines = lines_counter

    def show_text_parameters(self):
        print("Amount of lines equals: " + str(self.amount_of_lines))

    def implement_text_parsing(self, user_file):
        self.open_file(user_file)
        self.count_lines()
        self.show_text_parameters()


if __name__ == '__main__':

    tp = TextParser()
    tp.implement_text_parsing("The_Everest_Story.txt")
