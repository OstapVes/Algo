import unittest
from main import Node, Stack
from collections import deque


class TestStack(unittest.TestCase):

    def test_push(self):
        test = Stack()
        test.push(4)
        test.push(5)
        test.push(6)
        test.push(7)

        test_list = test.stack_to_list()

        right_stack = deque()
        right_stack.appendleft(4)
        right_stack.appendleft(5)
        right_stack.appendleft(6)
        right_stack.appendleft(7)

        right_stack_list = list(right_stack)

        self.assertEqual(test_list, right_stack_list)

    def test_pop(self):
        test = Stack()
        test.push(4)
        test.push(5)
        test.push(6)
        test.push(7)
        test.pop()

        test_list = test.stack_to_list()

        right_stack = deque()
        right_stack.appendleft(4)
        right_stack.appendleft(5)
        right_stack.appendleft(6)
        right_stack.appendleft(7)
        right_stack.popleft()
        right_stack_list = list(right_stack)

        self.assertEqual(test_list, right_stack_list)

    def test_size(self):
        test = Stack()
        test.push(4)
        test.push(5)
        test.push(6)
        test.push(7)
        test_size = test.size()

        right_stack = deque()
        right_stack.appendleft(4)
        right_stack.appendleft(5)
        right_stack.appendleft(6)
        right_stack.appendleft(7)
        right_stack_size = len(right_stack)

        self.assertEqual(test_size, right_stack_size)