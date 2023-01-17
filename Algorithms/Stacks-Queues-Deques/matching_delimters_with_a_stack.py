import python_stack_implementation


def is_matched(expr: str) -> bool:
    """
    Matches brackets to make sure that the correct delimiters are used
    :param expr: String
    :return: Boolean
    """

    lefty = "([{"
    righty = ")]}"

    S = python_stack_implementation.ArrayStack()

    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            # righty.index(c)\\needs to match the lefty index. Order Matters!
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


is_matched("([{}])")
