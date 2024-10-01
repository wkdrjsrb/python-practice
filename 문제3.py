def reverse_list(a):
    stack = list(a)
    reverse_string = ' '

    while stack:
        reverse_string += stack.pop()

    return reverse_string

a = input("문자열을 입력하시오 : ")

print("문자열 : ", reverse_list(a))
