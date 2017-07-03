import re


class TextParser():

    def __init__(self):
        self.file = None
        self.string_file = None
        self.amount_of_lines = None
        self.list_of_words = None
        self.amount_of_words = None
        self.amount_of_unique_words = None

    def open_file(self, file_to_open):
        self.file = open(file_to_open)
        self.string_file = self.file.read()

    def count_lines(self):
        lines_counter = 0

        for line in self.string_file:
            lines_counter += 1

        self.amount_of_lines = lines_counter

    def count_words(self):
        words_string = re.sub(r"[\n\t\-\,\.\:\;\'\d]+", "", self.string_file)
        self.list_of_words = words_string.split(" ")
        self.amount_of_words = len(self.list_of_words)

    def count_unique_words(self):
        list_of_unique_words = set(self.list_of_words)
        self.amount_of_unique_words = len(list_of_unique_words)

    def show_text_parameters(self):
        print("Amount of lines equals: " + str(self.amount_of_lines))
        print("Amount of words equals: " + str(self.amount_of_words))
        print("Amount of unique words "
              "equals: " + str(self.amount_of_unique_words))

    def implement_text_parsing(self, user_file):
        self.open_file(user_file)
        self.count_lines()
        self.count_words()
        self.count_unique_words()
        self.show_text_parameters()


if __name__ == '__main__':

    tp = TextParser()
    tp.implement_text_parsing("The_Everest_Story.txt")
