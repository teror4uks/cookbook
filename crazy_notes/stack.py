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


DIVISION = '/'
MULTIPLICATION = '*'
ADDITION = '+'
SUBTRACTION = '-'
EXPONENT = '^'

BRAKETS = {
    '(': ')',
    '{': '}',
    '[': ']'
}

REV_BRAKETS = {v: k for k, v in BRAKETS.items()}

OPERATORS = {
    DIVISION,
    MULTIPLICATION,
    ADDITION,
    SUBTRACTION,
    EXPONENT,
}

ORDER_RULES = {
    EXPONENT: 1,
    MULTIPLICATION: 2,
    DIVISION: 2,
    ADDITION: 3,
    SUBTRACTION: 3,
}


def is_operand(exp):
    try:
        int(exp)
        return True
    except Exception:
        return False


def has_higher_prec(op1, op2):
    """
    1) Parentheses () {} []
    2) Exponents ^ (right to left)
    3) Multiplication and division (left to right)
    4) Addition and subtraction (left to right)
    """
    wt_op1 = ORDER_RULES[op1]
    wt_op2 = ORDER_RULES[op2]

    if wt_op1 <= wt_op2:
        return True

    return False


def is_opening_parentheses(exp):
    return exp in BRAKETS


def is_closing_parentheses(exp):
    return exp in BRAKETS.values()


def parse_infix_to_postfix(calculated_string):
    """
    >>> from crazy_notes.stack import parse_infix_to_postfix
    >>> parse_infix_to_postfix('((1+2)+2)*2^2')
    '12+2+22^*'
    """
    result_str = ''
    stack = Stack(len(calculated_string))

    for s in calculated_string:
        if is_operand(s):
            result_str += s

        elif s in OPERATORS:
            while not stack.is_empty() and not is_opening_parentheses(stack.top()) and has_higher_prec(stack.top(), s):
                result_str += stack.pop()

            stack.push(s)

        elif is_opening_parentheses(s):
            stack.push(s)

        elif is_closing_parentheses(s):
            while not stack.is_empty() and not is_opening_parentheses(stack.top()):
                result_str += stack.pop()

            stack.pop()

    while not stack.is_empty():
        result_str += stack.pop()

    return result_str


def perform(op1, op2, operator):
    if operator == DIVISION:
        return float(op1) / float(op2)
    if operator == MULTIPLICATION:
        return float(op1) * float(op2)
    if operator == ADDITION:
        return float(op1) + float(op2)
    if operator == SUBTRACTION:
        return float(op1) - float(op2)
    if operator == EXPONENT:
        return float(op1) * float(op2)


def evaluate_postfix(expression):
    """
    >>> from crazy_notes.stack import evaluate_postfix
    >>> evaluate_postfix('12+2+22^*')  # infix form '((1+2)+2)*2^2'
    20.0
    """
    stack = Stack(len(expression))
    for exp in expression:

        if exp not in OPERATORS:
            stack.push(exp)
            continue

        op1 = stack.pop()
        op2 = stack.pop()
        res = perform(op2, op1, exp)
        stack.push(res)

    return stack.pop()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
