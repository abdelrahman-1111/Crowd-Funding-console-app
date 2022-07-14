my_file = open("data.txt")
string_list = my_file.readlines()


my_file.close()
print(string_list)

string_list[1] = "Edit the list of strings as desired\n"

my_file = open("data.txt", "w")
new_file_contents = "".join(string_list)

my_file.write(new_file_contents)
my_file.close()

readable_file = open("data.txt")
read_file = readable_file.read()
print(read_file)