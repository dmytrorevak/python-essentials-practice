import re


class TextParser():

    def __init__(self):
        self.file = None
        self.file_text = None
        self.list_of_words = None
        self.all_text_letters = None
        self.amount_of_lines = None
        self.amount_of_words = None
        self.amount_of_unique_words = None
        self.amount_of_vowels = None
        self.amount_of_consonants = None

    def open_file(self, file_to_open):
        self.file = open(file_to_open)
        print(self.file)
        self.file_text = open(file_to_open).read()

    def count_lines(self):
        lines_counter = 0

        for line in self.file:
            lines_counter += 1

        self.amount_of_lines = lines_counter + 1

    def count_words(self):
        letters_spaces_list = []

        for char in self.file_text:
            if char.isalnum():
                letters_spaces_list.append(char)
            else:
                letters_spaces_list.append(' ')

        letters_spaces_string = "".join(letters_spaces_list)
        clear_text = re.sub(r"\s+", " ", letters_spaces_string)
        self.list_of_words = clear_text.split(" ")
        self.amount_of_words = len(self.list_of_words)

    def count_unique_words(self):
        list_of_unique_words = set(self.list_of_words)
        self.amount_of_unique_words = len(list_of_unique_words)

    def set_all_text_letters(self):
        self.all_text_letters = str(re.findall(r"[A-Za-z]", self.file_text))

    def count_vowel_letters(self):
        all_vowel_letters = re.findall(r"[AaEeIiOoUu]", self.all_text_letters)
        self.amount_of_vowels = len(all_vowel_letters)

    def count_consonants_letters(self):
        amount_of_letters = len(self.all_text_letters)
        self.amount_of_consonants = amount_of_letters - self.amount_of_vowels

    def show_text_parameters(self):
        print("Amount of lines equals: " + str(self.amount_of_lines))
        print("Amount of words equals: " + str(self.amount_of_words))
        print("Amount of unique words "
              "equals: " + str(self.amount_of_unique_words))
        print("Amount of vowels equals: " + str(self.amount_of_vowels))
        print("Amount of consonants equals: " + str(self.amount_of_consonants))

    def implement_text_parsing(self, user_file):
        self.open_file(user_file)
        self.set_all_text_letters()
        self.count_lines()
        self.count_words()
        self.count_unique_words()
        self.count_vowel_letters()
        self.count_consonants_letters()
        self.show_text_parameters()


if __name__ == '__main__':

    tp = TextParser()
    tp.implement_text_parsing("The_Everest_Story.txt")
