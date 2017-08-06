# class ReverseIterator():

#     def __init__(self, list_object):
#         self.list_object = list_object
#         self.iter = len(list_object)

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.iter > 0:
#             self.iter -= 1
#             return self.list_object[self.iter]
#         else:
#             raise StopIteration()


# def reverse_generator(list_object):
#     list_length = len(list_object)

#     for i in range(list_length - 1, -1, -1):
#         yield list_object[i]


# alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# numeric_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ri1 = ReverseIterator(alphabet_list)
# ri2 = ReverseIterator(numeric_list)
# rg1 = reverse_generator(alphabet_list)
# rg2 = reverse_generator(numeric_list)

# for i, j, x, y in zip(ri1, ri2, rg1, rg2):
    # print('Iterator items: {0}, {1} \n'
          # 'Generator items: {2}, {3}'.format(i, j, x, y))


# -----------------------------------------------------------------------------------------------

def read_files(filemanes):
    for file in filemanes:
        file = open(file)
        for line in file:
            yield line


all_files_lines = read_files(['test.txt', 'test1.txt', 'test2.txt'])
lines = (line for line in all_files_lines if len(line) <= 40)

for line in lines:
    print(line)
