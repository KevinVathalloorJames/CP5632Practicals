def main():
    list_of_numbers = []
    for i in range(1, 6):
        number = int(input("Enter Number ".format(i)))
        list_of_numbers.append(number)
    print("The First number is ", list_of_numbers[0])
    print("The last number is ", list_of_numbers[-1])
    print("The smallest number is ", min(list_of_numbers))
    print("The largest number is ", max(list_of_numbers))
    print("The average of the number is ", sum(list_of_numbers)/len(list_of_numbers))
    authorised_usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter the username : ")
    if username in authorised_usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()
