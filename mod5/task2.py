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

    def print_queue(self):
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


queue = Queue()

queue.print_queue()
queue.enqueue(1)
queue.print_queue()
queue.enqueue(2)
queue.print_queue()
queue.enqueue(3)
queue.print_queue()
queue.enqueue(4)
queue.print_queue()

print("Первый элемент в очереди: ", queue.peek())

print("Удален из очереди: ", queue.dequeue())
queue.print_queue()
print("Удален из очереди: ", queue.dequeue())
queue.print_queue()
print("Удален из очереди: ", queue.dequeue())
queue.print_queue()
print("Первый элемент в очереди: ", queue.peek())
