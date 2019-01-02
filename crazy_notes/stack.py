class Stack:
    """
    >>> from crazy_notes.stack import Stack
    >>> s = Stack()
    >>> s.push(1)
    >>> s.push(2)
    >>> s.push(3)
    >>> s.top()
    3
    >>> s.is_empty()
    False
    >>> s.pop()
    3
    >>> s.top()
    2
    """
    def __init__(self, max_size=101):
        self.elements = [None] * max_size
        self.top_element = -1
        self.max_size = max_size

    def top(self):
        if self.is_empty():
            return

        return self.elements[self.top_element]

    def pop(self):
        if self.is_empty():
            return

        el = self.top()
        self.top_element -= 1
        return el

    def push(self, element):
        if self.top_element >= self.max_size -1:
            raise Exception('Stack is overflow')

        self.top_element += 1
        self.elements[self.top_element] = element

    def is_empty(self):
        if self.top_element == -1:
            return True

        return False


def stack_reverse(s, s_len):
    """
    >>> from stack import stack_reverse
    >>> s = 'hello'
    >>> stack_reverse(s, len(s))
    'olleh'
    """
    stack = Stack(s_len)
    for i in s:
        stack.push(i)
    reverse_string = ''
    while not stack.is_empty():
        reverse_string += stack.pop()

    return reverse_string


def check_balance_parentheses(expression):
    """
    >>> from stack import check_balance_parentheses
    >>> check_balance_parentheses('([)]')
    False
    >>> check_balance_parentheses(')[]')
    False
    >>> check_balance_parentheses('[{}({})]')
    True
    """
    brakets_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    rev_brakets_dict = {v: k for k, v in brakets_dict.items()}

    stack = Stack(len(expression))
    stack.push(expression[0])

    for e in expression[1:]:
        if e in brakets_dict.keys():
            stack.push(e)
        elif e in rev_brakets_dict.keys():
            if stack.is_empty():
                return False

            open_braket_elem = rev_brakets_dict[e]

            if stack.top() != open_braket_elem:
                return False

            stack.pop()

    return stack.is_empty()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
