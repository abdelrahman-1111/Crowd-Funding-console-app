from login_module import login
from project_module import project_list
from validations import checkmail
from register_module import register
ans=10
while ans!=0:
    print ("""
    ********main menu*********
    press '1' for register
    press '2' for login
    press '0' for Quit
    """)
    ans=input("enter your option: ") 
    if ans=="1": 
        register()
    elif ans=="2":
        user_email=input("please enter your login e-mail: ")
        checkmail(user_email)
        user_passwd=input("please enter your login password: ")
        if login(user_email,user_passwd):
            project_list()
        else:
            continue
    else:
        print ("that's not an option!")
