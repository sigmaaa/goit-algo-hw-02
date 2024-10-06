from collections import deque


def is_palindrom(deque_string):

    while len(deque_string) != 1 and len(deque_string) != 0:
        if (deque_string.popleft().lower() != deque_string.pop().lower()):
            return False
    return True


if __name__ == '__main__':
    some_string_deque = deque(
        input("Type some word to check if it's palindrom \n"))
    print(is_palindrom(some_string_deque))
