from project_methods import create_project , delete
from validations import checktitle


def edit_list():
    ans=10
    while ans!=0:
        print ("""
        ***********edit menu**************
        press '1' to edit entire project
        press '2' to edit specific attribute in project 
        press '0' to go back
        """)
        ans=input("enter your option: ") 
        if ans=="1": 
            t=input("enter the title of the project you want to edit:  ")
            checktitle(t)
            delete(t)
            create_project()
        elif ans=="2":
            specific_column()
        elif ans=='0':
            print("goodbye :( ")
            return 0
        else:
            print("thats not an option!")

def specific_column():
    ans=10
    while ans!=0:
        print ("""
        ***********edit project's**************
        press '1' title
        press '2' details
        press '3' total target 
        press '4' start date 
        press '5' end date 
        press '0' to go back
        """)
        ans=input("enter your option: ") 
        if ans=="1": 
            t=input("enter the title of the project you want to edit:  ")
            checktitle(t)
            delete(t)
            create_project()
        elif ans=="2":
            
        elif ans=='3':
            print ("edit")
        elif ans=='4':
            project_title=input("/nplease enter the title of the project\nyou want to delete: ")
            checktitle(project_title)
            delete(project_title)
        elif ans=='5':
            start=input("/nplease enter the start-date of the project: ")
            check_date(start)
            end=input("/nplease enter the end-date of the project: ")
            check_date(end)
            if search(start,end):
                search_result=search(start,end)
                print(f"/nproject found, here's the data of the proje
        elif ans=='0':
            print("goodbye :( ")
            return 0
        else:
            print("thats not an option!")