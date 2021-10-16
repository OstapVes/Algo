class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):

        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def pop(self):

        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def top(self):

        return self.head.data

    def size(self):

        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def isEmpty(self):

        if self.head is None:
            return True
        else:
            return False

    def printStack(self):

        print("Stack elements:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

    def stack_to_list(self):
        empty_list = list()
        curr_pos = self.head
        while curr_pos is not None:
            empty_list.append(curr_pos.data)
            curr_pos = curr_pos.next
        return empty_list


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(5)

stack.printStack()

print("\nTop element:", stack.top())

print("Size:", stack.size())

stack.pop()

stack.printStack()

print("\nStack is empty:", stack.isEmpty())

my_stack_list = stack.stack_to_list()
print(my_stack_list)