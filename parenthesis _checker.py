def is_paranthesis_correct(input_str):
    open_paranthesis = []
    for char in input_str:
        if char in ('(', '{', '['):
            open_paranthesis.append(char)
        if char in (')', '}', ']'):
            if open_paranthesis.pop() + char not in ('()', '{}', "[]"):
                return False

    return len(open_paranthesis) == 0


print(is_paranthesis_correct("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(is_paranthesis_correct("( 23 ( 2 - 3);"))
print(is_paranthesis_correct("( 11 }"))
