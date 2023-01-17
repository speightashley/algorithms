from python_stack_implementation import ArrayStack


def is_matched(raw: str):
    """Return True if all HTML tags are properly matched"""

    S = ArrayStack()
    j = raw.find("<")
    while j != -1:
        k = raw.find(">", j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k]
        if not tag.startswith("/"):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find("<", k + 1)
    return S.is_empty()
