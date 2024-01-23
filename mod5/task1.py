class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data) # создается новый узел с данными
            new_node.next = self.head # текущий крайний элемент становится следующим за добавленным
            self.head = new_node # добавленный элемент становится крайним

    def pop(self):
        if self.is_empty():
            raise Exception("Стек пустой")
        else:
            popped_node = self.head # сохраняем крайний элемент
            self.head = self.head.next # устанавливаем крайним элементом следующий элемент в стеке
            return popped_node.data # возвращаем значение сохраненного элемента, который был крайним

    def peek(self):
        if self.is_empty():
            raise Exception("Стек пустой")
        else:
            return self.head.data

    def print_stack(self):
        if not self.is_empty():
            current_element = self.head
            print("HEAD", end=" ")
            ending = " -> "
            while current_element is not None:
                if current_element.next is None:
                    ending = ""
                print(current_element.data, end=ending)
                current_element = current_element.next
            print("\n")
        else:
            raise Exception("Стек пустой")


stack = Stack()

stack.print_stack()
stack.push(1)
stack.print_stack()
stack.push(2)
stack.print_stack()
stack.push(3)
stack.print_stack()
stack.push(4)
stack.print_stack()

print("Крайний элемент: ", stack.peek())

print("Удален из стека: ", stack.pop())
stack.print_stack()
print("Удален из стека: ", stack.pop())
stack.print_stack()
print("Удален из стека: ", stack.pop())
stack.print_stack()
print("Крайний элемент: ", stack.peek())
