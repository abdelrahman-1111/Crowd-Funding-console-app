from project_methods import create_project, delete, view_projects ,search
from validations import check_date, checktitle


def project_list():
    ans=10
    while ans!=0:
        print ("""
        ********project menu*********
        press '1' to create a project
        press '2' to view all projects 
        press '3' to edit a project
        press '4' to delete a project
        press '5' to search for project
        press '0' to logout
        """)
        ans=input("enter your option: ") 
        if ans=="1": 
            create_project()
        elif ans=="2":
            view_projects()
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
                print(f"/nproject found, here's the data of the project\n{search_result}")
        elif ans=='0':
            print("goodbye :( ")
            return 0
        else:
            print("thats not an option!")

project_list()