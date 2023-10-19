# uppgift 1
def add_together(a, b):
    return a + b

print(add_together(5, 5))


# uppgift 2
def show_name():
    user_name = input("Enter your name: ")
    print(user_name)

show_name()


# uppgift 3
for i in range(10):
    print(add_together(i, i))


# uppgift 4 (another version of this program)
def show_friend_list(friend_list):
    for index, name in enumerate(friend_list, 1):
        print(f"{index}.) {name}")


def choose_action(index, friend_list):
    if index > len(friend_list):
        print("No such name exists in the list")
        return friend_list
    
    user_input = input("r/c: ")

    # remove 
    if user_input == "r": 
        friend_list.pop(index - 1)

    # change
    elif user_input == "c":
        friend_list[index - 1] = input("Change to: ")

    else:
        print("Unknown command")

    return friend_list

friend_list = []
print("Add element = new name\nRemove or change - name position in the list\nEnter to exit")

while True:
    show_friend_list(friend_list)
    user_input = input("ADD/REMOVE/CHANGE:")

    if user_input == "": 
        break
    if user_input.isdigit():
        friend_list = choose_action(int(user_input), friend_list)
    else: 
        friend_list.append(user_input)

print("Your final friend list: ")
show_friend_list(friend_list)


# uppgift 5 (code from module 3)
def ask_numbers(): 

    first_number = int(input("enter your first number :"))
    second_number = int(input("enter your second number :"))

    choose_operation(first_number, second_number)


def choose_operation(num1, num2):

    # Jag knyter här resultaten av varje operation med det siffran användaren anger
    operations = {"1" : num1 + num2, 
                  "2" : num1 - num2, 
                  "3" : num1 * num2, 
                  "4" : num1 / num2
                  }
    show_operations()

    user_operation_choice = input("type in a number of operation you want to perform: ")
    print(show_awnser(operations[user_operation_choice]))


def show_operations():
    operation_names = ["addition", "subtraktion", "multiplication", "devision"]
    
    for index in range(1, len(operation_names) + 1):
        print("%s - %s" %(index, operation_names[index - 1]))


def show_awnser(awnser):
    return awnser


ask_numbers()


