from validations import checkmail
def login(e_mail,passwd):
    usersfile = open("users_data.txt", "r")
    usersdata = usersfile.readlines()  #read file content into a list
    for i in usersdata:
        i = i.strip("\n")  # remove the \n from the end of each line
        user = i.split("||")  # split string into parts
        if e_mail==user[2]:
            if e_mail==user[2] and passwd==user[3]:
                print(f"\nwelcome back!, {user[0]}")
                return True
            else:
                print("\nincorrect password")
                break
    else:
        print("\nthis email doesn't have an account\n\nplease register first. ")
    usersfile.close()#closing the file

