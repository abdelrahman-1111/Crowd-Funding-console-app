from curses.ascii import isalpha
import re
import datetime

#check the name is alphapatic only
def checkname(name):
    if name.isalpha():
        return name
    else:
        name=input("your name must not contains numbers\nre-enter you name: ")
        return checkname(name)
#checks the password if not spaces or empty
def checkpasswd(passwd):
    if passwd.isspace():
        passwd=input("password can no be spaces\nre-enter the password: ")
        return checkpasswd(passwd)
    elif passwd:
        return passwd 
    else:
        passwd=input("password can no be spaces\nre-enter the password: ")
        return checkpasswd(passwd)          
#comparing the 2 passwords the user enters
def confirmpasswd(pass1,pass2):
    if pass1==pass2:
        return pass1
    else:
        pass1= input("the password doesn't match \nre-enter the password: ")
        pass2= input("confirm the password: ")
        return confirmpasswd(pass1,pass2)
#check for the number validated against egyption phone numbers
def checkphone(mobile):
    regex = r'00201[0125]+[0-9]{8}'
    if(re.fullmatch(regex, mobile)):
        return mobile
    else:
        mobile = input("incorrect format re-enter the phone number: ")
        return checkphone(mobile)
#check the mail in sutable format
def checkmail(mail):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.fullmatch(regex, mail)):
        return mail
    else:
        while True:
            mail=input("invalid e-mail\nenter your e-mail: ")
            return checkmail(mail)
#check if title is alphapatic only
def checktitle(var):


    if var.isalpha():
        return var
    else:
        var=input("the title of your project must not contains numbers\nre-enter the project title: ")
        return checkname(var)
#checking that the total target is in digits
def check_target(target):
    if target.isdigit():
        return target
    else:
        target=input("your total target must be in numbers\nre-enter you total target: ")
        return check_target(target)
#check for the date formate validation
def check_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return date_text
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        date_text=input("please re-enter the date in the right formate: ")
        return check_date(date_text)


# var=input("enter date:  ")
# var=check_date(var)
# print(var)
