from validations import check_date, check_target, checktitle

def create_project():
    title=input("please enter your project title: ")
    title=checktitle(title)
    details=input("please enter your project description: ")
    total_target=input("please enter your project total target: ")
    total_target=check_target(total_target)
    start_date=input("please enter your project start-date[yyyy-mm-dd]: ")
    start_date=check_date(start_date)
    end_date=input("please enter your project end-date[yyyy-mm-dd]: ")
    end_date=check_date(end_date)

    datahandle=f"{title}||{details}||{total_target}||{start_date}||{end_date}\n" 
    projectfile=open("project_data.txt", "a")
    projectfile.write(datahandle)
    projectfile.close()
    print("****project created !****")

def view_projects():
    projectfile=open("project_data.txt","r")
    projects=projectfile.readlines()
    for i in projects:
        i=i.strip("\n")
        print(f"{i}\n")
    projectfile.close()
    x=input("press any key to exit...")#to freeze the screen 

def search(startdate,enddate):

    projfile = open("project_data.txt", "r")
    projdata = projfile.readlines()  #read file content into a list
    for i in projdata:
        i = i.strip("\n")  # remove the \n from the end of each line
        proj = i.split("||")  # split string into attributes
        for j in proj:
            if proj[3]==startdate and proj[4]==enddate:
                return proj
    else:
        print("\nno projects found\n")
        projfile.close()#cloasing the file
        return False

def delete(title):   
    projread=open("project_data.txt","r")
    temp=open("temp.txt","a")
    readtemp=open("temp.txt","r")

    projdata=projread.readlines()
    for j,i in enumerate(projdata):
        i=i.strip("\n")
        project=i.split("||")
        if project[0]==title:
            print(projdata[j])
            del projdata[j]
        print(i)
        # temp.write(f"{i}\n")
    # 
    # 
    # open('project_data.txt', 'w').close()
    # projappend=open("project_data.txt","a")
    # newdata=readtemp.readlines()
    # for i in newdata:
        # print(i)
        # i=i.strip("\n")
        # projappend.write(i)

    projread.close()
    # projappend.close()
    temp.close()
    readtemp.close() 
    # open('temp.txt', 'w').close()

x=input("enter title:  ")
delete(x)
# create_project()