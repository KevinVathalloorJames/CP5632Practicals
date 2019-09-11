OUTPUT_FILE = "name.txt"
user_name = input("Enter your name: ")
out_file = open(OUTPUT_FILE, 'w')
print(user_name, file=out_file)
out_file.close()

out_file = open(OUTPUT_FILE, 'r')
user_name = out_file.read().strip()
out_file.close()
print("Your name is", user_name)
out_file.close()

file_values = open("numbers", 'r')
number_1 = int(file_values.readline())
number_2 = int(file_values.readline())
print(number_1, "a" )
file_values.close()
print("The sum is: ", number_1+number_2)

total = 0
file_values = open("numbers", 'r')
for line in file_values:
    number = int(line)
    total += number
file_values.close()
print("The sum is: ", total)




