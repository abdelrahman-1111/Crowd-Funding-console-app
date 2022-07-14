from validations import checkmail, checkname, checkpasswd,checkphone, confirmpasswd

def register():
    firstname=input("please enter your name: ")
    firstname=checkname(firstname)
    lastname=input("please enter your lastname: ")
    lastname=checkname(lastname)
    email=input("please enter your e-mail: ")
    email=checkmail(email)
    password=input("please enter your password: ")
    password=checkpasswd(password)
    Cpassword=input("please confirm your password: ")
    password=confirmpasswd(password,Cpassword)
    phone=input("please enter your phone number: ")
    phone=checkphone(phone)
    datahandle=f"{firstname}||{lastname}||{email}||{password}||{phone}\n" 
    userfile=open("users_data.txt", "a")
    userfile.write(datahandle)
    userfile.close()