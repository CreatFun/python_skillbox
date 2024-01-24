class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class Queue:

    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.back is None:
            self.front = Node(data) # создаем первый элемент
            self.back = self.front # последний элемент равен первому
        else:
            self.back.next = Node(data) # новый элемент следующий после последнего
            self.back.next.previous = self.back # бывший последним элемент теперь предыдущий для добавленного
            self.back = self.back.next # последним теперь является добавленный элемент

    def dequeue(self):
        if self.front is None:
            raise Exception("Очередь пуста")
        else:
            dequeued_node = self.front # сохраняем первый элемент
            if self.front.next is None:
                self.front = None
                self.back = None
            else:
                self.front = self.front.next  # первым теперь будет следующий за сохраненным элемент
                self.front.previous = None  # у нового первого элемента теперь нет предыдущего
            return dequeued_node.data # возвращаем значение сохраненного элемента

    def peek(self):
        if self.front is None:
            raise Exception("Очередь пуста")
        else:
            return self.front.data

    def print(self):
        if not self.is_empty():
            current_element = self.front
            print("FRONT", end=" ")
            ending = " -> "
            while current_element is not None:
                if current_element.next is None:
                    ending = ""
                print(current_element.data, end=ending)
                current_element = current_element.next
            print(" BACK \n")
        else:
            raise Exception("Очередь пуста")

    def insert(self, n, val):
        if self.is_empty():
            raise Exception("Очередь пуста")
        else:
            if not self.is_index_correct(n) or n == 0:
                raise IndexError("Некорректный индекс")
            else:
                count = 0
                current_element = self.front
                while count < n - 1:
                    count += 1
                    current_element = current_element.next
                # здесь current_element - элемент с индексом n-1
                new_node = Node(val)
                new_node.next = current_element.next
                current_element.next.previous = new_node
                current_element.next = new_node
                new_node.previous = current_element

    def is_index_correct(self, index):
        if index < 0 or index > self.get_size() - 1 or type(index) is not int:
            return False
        return True

    def get_size(self):
        if self.back is None:
            return 0
        count = 1
        current_element = self.front
        while current_element.next is not None:
            count += 1
            current_element = current_element.next
        return count
queue = Queue()

queue.enqueue(1)
queue.print()
queue.enqueue(2)
queue.print()
queue.enqueue(3)
queue.print()
queue.enqueue(4)
queue.print()

queue.insert(2, "new")
queue.print()
print("Первый элемент в очереди: ", queue.peek())

print("Удален из очереди: ", queue.dequeue())
queue.print()
print("Удален из очереди: ", queue.dequeue())
queue.print()
print("Удален из очереди: ", queue.dequeue())
queue.print()
print("Первый элемент в очереди: ", queue.peek())
