class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None
        self.current_element = None

    def __iter__(self):
        self.current_element = self.head
        return self

    def __next__(self):
        if self.current_element is not None:
            return_element = self.current_element  # сохраняем текущий
            self.current_element = self.current_element.next  # переключаем текущий на следующий
            return return_element  # возвращаем сохраненный
        else:
            raise StopIteration

    def print_list(self):
        if self.is_empty():
            raise Exception("Список пуст")
        else:
            current_element = self.head
            while current_element is not None:
                print(current_element.data, end=" -> ")
                current_element = current_element.next
            print("\n")

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.end = self.head
        else:
            self.end.next = new_node  # последнему элементу добавляем ссылку на добавленный
            self.end = new_node  # добавленный становится последним

    def get_size(self):
        if self.head is None:
            return 0
        count = 1
        current_element = self.head
        while current_element.next is not None:
            count += 1
            current_element = current_element.next
        return count

    def is_empty(self):
        if self.get_size() == 0:
            return True
        return False

    def get(self, index: int):
        if self.is_empty():
            raise Exception("Список пуст")
        else:
            if not self.is_index_correct(index):
                raise IndexError("Некорректный индекс")
            else:
                count = 0
                current_element = self.head
                while count < index:
                    count += 1
                    current_element = current_element.next
                return current_element.data

    def remove(self, index):
        if self.is_empty():
            raise Exception("Список пуст")
        else:
            if not self.is_index_correct(index):
                raise IndexError("Некорректный индекс")
            else:
                count = 0
                current_element = self.head
                limit = index
                if index == self.get_size() - 1:
                    limit = index - 1
                    while count < limit:
                        count += 1
                        current_element = current_element.next
                    deleted_value = current_element.next.data  # удаляемый элемент - последний в списке
                    current_element.next = None  # у текущего удаляем ссылку на последний, чтобы убрать последний элемент из списка
                else:
                    while count < limit:
                        count += 1
                        current_element = current_element.next
                    deleted_value = current_element.data  # удаляемый элемент - текущий
                    current_element.data = current_element.next.data  # в удаленный элемент записываем значение
                    current_element.next = current_element.next.next  # и ссылку следующего по списку элемента
                return deleted_value

    def insert(self, n, val):
        if self.is_empty():
            raise Exception("Список пуст")
        else:
            if not self.is_index_correct(n) or n == 0:
                raise IndexError("Некорректный индекс")
            else:
                count = 0
                current_element = self.head
                while count < n - 1:
                    count += 1
                    current_element = current_element.next
                # здесь current_element - элемент с индексом n-1
                new_node = Node(val)
                new_node.next = current_element.next  # для вставленного элемента следующим будет элемент с индексом n
                current_element.next = new_node  # а для текущего элемента (n-1) новый станет следующим (новый между n-1 и n)

    def is_index_correct(self, index):
        if index < 0 or index > self.get_size() - 1 or type(index) is not int:
            return False
        return True


new_list = LinkedList()

new_list.push(1)
new_list.print_list()
new_list.push(2)
new_list.print_list()
new_list.push(3)
new_list.print_list()
new_list.push(4)
new_list.print_list()

new_list.insert(1, "new")
new_list.print_list()

print(new_list.remove(2))
new_list.print_list()
print(new_list.get(2))

print("Итерация 1: ", end="")
for i in new_list:
    print(i.data, end=", ")

print("\nИтерация 2: ", end="")
for i in new_list:
    print(i.data, end=", ")
