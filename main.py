# Add spaces to the end of a String in Python

my_str = 'abc'

result_1 = my_str.ljust(6, ' ')
print(repr(result_1))  # 👉️ 'abc   '

result_2 = my_str + " " * 3
print(repr(result_2))  # 👉️ 'abc   '

result_3 = f'{my_str: <6}'
print(repr(result_3))  # 👉️ 'abc   '
