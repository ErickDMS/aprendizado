try:
    name = input('What is your name?')
except EOFError as name:
    print(name)

print('Hello,', name)
