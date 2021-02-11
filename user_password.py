defuser = "coder"
defpassword ="1234"

while(True):
    user = input("user name:")
    password =input("password:")
    if (user ==defuser) and (password ==defpassword):
        print("welcome",user)
        break
    elif (user !=defuser) and (password ==defpassword):
        print("your user name is wrong !!")

    elif (user ==defuser) and (password !=defpassword):
        print("your password is wrong !!")
        print("do you want to change your password ? (yes or no)")

        answer =input()
    if (answer =="yes"):

        newpassword =input("new password:")
        print("please wait ")
        defpassword=newpassword
        print("password is successfully changed")


    else:

             print("Please try agin ")
