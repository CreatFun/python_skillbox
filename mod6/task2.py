class DoubleElement:
    def __init__(self, *lst):
        self.list_of_nums = lst
        self.index = 0


    def __next__(self):
        if len(self.list_of_nums) % 2 == 0:
            if self.index < len(self.list_of_nums) - 1:
                current_index = self.index
                self.index += 2
                return self.list_of_nums[current_index], self.list_of_nums[current_index + 1]
            else:
                raise StopIteration
        else:
            if self.index < len(self.list_of_nums):
                if self.index == len(self.list_of_nums) - 1:
                    current_index = self.index
                    self.index += 2
                    return self.list_of_nums[current_index], None
                else:
                    current_index = self.index
                    self.index += 2
                    return self.list_of_nums[current_index], self.list_of_nums[current_index + 1]
            else:
                raise StopIteration

    def __iter__(self):
        self.list_of_nums = self.get_list_of_nums()
        self.index = 0
        return self

    def get_list_of_nums(self):
        return self.list_of_nums


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)

# Ожидаемый результат кода:
# (1, 2)
# (3, 4)
#
# (1, 2)
# (3, 4)
# (5, None)
