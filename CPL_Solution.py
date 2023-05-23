import requests
import json 

def get_user_full_name_list(Number1, Number2):

    Page1Url = "https://reqres.in/api/users?page=1"
    Page2Url = "https://reqres.in/api/users?page=2"
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    responsePage1= requests.get(Page1Url, headers=headers, timeout=10).json()
    responsePage2= requests.get(Page2Url, headers=headers, timeout=10).json()

    mylist = []  # creating combined list of all users on Page 1 and Page2
    myFinalList = [] #creating list for the numbers specified in function
    myFinalSortedList = [] #creating sorted list for the numbers specified
  
    # Iterating through the Page of URL 1: 
    for i in responsePage1['data']:
        stri = str(i)
        x = stri.split(", ")
        x[2] = x[2].split(": ")[1]
        x[3] = x[3].split(": ")[1]
        x[2] = x[2].replace("'","")
        x[3] = x[3].replace("'","")
        FirstLast_Name = x[2] + " " + x[3]
        mylist.append(FirstLast_Name)

        # Iterating through the Page of URL 2:
    for i in responsePage2['data']:
        stri = str(i)
        x = stri.split(", ")
        x[2] = x[2].split(": ")[1]
        x[3] = x[3].split(": ")[1]
        x[2] = x[2].replace("'","")
        x[3] = x[3].replace("'","")
        FirstLast_Name = x[2] + " " + x[3]
        mylist.append(FirstLast_Name)
        
    k= 0
    j = 0
    for k in mylist:      
        if j >= Number1 - 1  and j < Number2:
            myFinalList.append(k)
        j = j + 1
   
    SortedList = sorted(myFinalList)
    return SortedList  # returning sorted list 


Number1=int(input("Enter first number  :")) # taking first number from user
Number2=int(input("Enter second number :")) # taking second number from user

MainList = get_user_full_name_list(Number1, Number2) 
print(MainList)

  
