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


new_stack = Stack()

new_stack.push(11)
new_stack.push(22)
new_stack.push(33)
new_stack.push(44)

print("Крайний элемент: ", new_stack.peek())

print(new_stack.pop())
print(new_stack.pop())

print("Крайний элемент: ", new_stack.peek())
