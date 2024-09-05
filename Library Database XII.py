import pickle
import os

def create():
    f=open("library.dat","wb")
    fx=open("num.txt","w")
    id=99
    while True:
        d={}
        id+=1
        l=[]
        Name_of_customer=input("enter name")
        l.append(Name_of_customer)
        Title_of_Book=input("enter title")
        l.append(Title_of_Book)
        Author=input("enter author name")
        l.append(Author)
        Date_of_Issuing=input("enter date of issuing")
        l.append(Date_of_Issuing)
        Date_of_Returning=input("enter date of returning")
        l.append(Date_of_Returning)
        d[id]=l
        print(d)
        pickle.dump(d,f)
        ch=input("do you want to enter more records(y/n)")
        if ch=="n" or ch=="N":
            break
    f.close()
    fx.write(str(id))
    fx.close()

def append():
    f=open("library.dat","ab")
    fx=open("num.txt","r+")
    id=int(fx.read())
    while True:
        d={}
        id=id+1
        l=[]
        Name_of_customer=input("enter name")
        l.append(Name_of_customer)
        Title_of_Book=input("enter title")
        l.append(Title_of_Book)
        Author=input("enter author name")
        l.append(Author)
        Date_of_Issuing=input("enter date of issuing")
        l.append(Date_of_Issuing)
        Date_of_Returning=input("enter date of returning")
        l.append(Date_of_Returning)
        d[id]=l
        print(d)
        pickle.dump(d,f)
        ch=input("do you want to enter more records(y/n)")
        if ch=="n" or ch=="N":
            break
    f.close()
    fx.seek(0)
    fx.write(str(id))
    fx.close()

def display_all_rec():
    f=open("library.dat","rb")
    try:
        while True:
            d=pickle.load(f)
            a=list(d.keys())
            print("The id is{}, name is {},title is {},author is {}"
                  " ,date of issuing is {} ,date of returning is {}" 
                  .format(a[0],d[a[0]][0],d[a[0]][1],d[a[0]][2],
                          d[a[0]][3],d[a[0]][4]))
            
    except EOFError:pass
    finally:f.close()

def delete_id_rec():
    f1=open("library.dat","rb")
    f2=open("temp.dat","wb")
    lib_id=int(input("enter ID to delete"))
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            if lib_id in d:
                flag=1
            else:
                pickle.dump(d,f2)
    except EOFError:
        if flag==0: 
            print("sorry ID to delete was not there")
    finally:
        f1.close()
        f2.close()

def delete_name_rec():
    f1=open("library.dat","rb")
    f2=open("temp.dat","wb")
    nm=input("enter name to delete")
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            for i in d:
                a_name,b_title,c_author,d_doi,d_dor=d[i]
                if a_name.lower()==nm.lower():
                    flag=1
                else:
                    pickle.dump(d,f2)
    except EOFError:
        if flag==0: 
            print("Sorry name to delete was not there")
        else:
            print("Deleted record")
    finally:
        f1.close()
        f2.close()

def modify_name_of_customer():
    f1=open("library.dat","rb")
    f2=open("temp.dat","wb")
    id=int(input("enter id to search: "))
    name=input("enter name no to changed:")
    count=0
    try:
        while True:
            d=pickle.load(f1)
            if id in d:
                d[id][0]=name
                count=1
                pickle.dump(d,f2)
            else:
                pickle.dump(d,f2)
            print(d)
    except EOFError:
        if count==0: print("sorry id whose name had to be changed was not there")
    finally:
        f1.close()
        f2.close()

def search():
    if not os.path.isfile("library.dat"):
        print("sorry, file not found")
    else:
        f=open("library.dat","rb")
        name=input("enter name")
        flag=0
        try:
            while True:
                d=pickle.load(f)
                for i in d:
                    if d[i][0]==name:
                        flag=1
                        print("name",i)
                        print("The name is %s ,title is %s, author is %s, date of issuing is %s,date of returning is %s"%\
                              (d[i][0],d[i][1],d[i][2],d[i][3],d[i][4]))
        except EOFError:
            if flag==0:
                print("sorry, name not found in the database")
        finally:
            f.close()

import datetime
while True:
    Input_date1=input("enter the date in format 'dd/mm/yy':")
    day,month,year=Input_date1.split("/")
    isValidDate=True
    try:
        
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        isValidDate=False
    if(isValidDate):
        print ("date of issuing is valid")
        break
    else:
        print("date entered by you is invalid, enter again")

import datetime
while True:
    Input_date2=input("enter the date in format 'dd/mm/yy':")
    day,month,year=Input_date2.split("/")
    isValidDate=True
    try:
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        isValidDate=False
    if(isValidDate):
        print ("date of returning is valid")
        break
    else:
        print("date entered by you is invalid, enter again")

def main():
    while True:
        print(" 1.Create\n 2.Append\n 3.Display\n 4.Delete by name\n 5.Delete by id\n 6.Modify name\n 7.Search by name\n 8.Exit")
        ch=input("enter your choice")
        if ch=='1':
            create()
        elif ch=='2':
            append()
        elif ch=='3':
            display_all_rec()
        elif ch=='4':
            delete_name_rec()
        elif ch=='5':
            delete_id_rec()
        elif ch=='6':
            modify_name_of_customer()
        elif ch=='7':
            search()
        elif ch=='8':
            break
        else:
            print("invalid choice,try again")
