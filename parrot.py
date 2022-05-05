prompt = input("Tell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program. "
message = ""

# version without flag
# while message != 'quit':
#    message = input(prompt)
#
#    if message != 'quit':
#        print(message)

# version with flag

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
