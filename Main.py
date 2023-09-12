import os
import tkinter as tk

#Good Bye Message's Function
def byegui():
    window = tk.Tk()

    window.minsize(400, 200)
    window.maxsize(700, 200)


    window.title("Welcome")

    label = tk.Label(window, text="Thankyou for using Charity Management System Copyright © 1997 ASH Technologies Private Limited!\n\nWe hope you have a nice day")
    label.pack()
    window.after(3000, window.destroy)


    window.mainloop()

def pattern(): #Repeated pattern for the UI
    {
        print('''
            \t\t\t\t---------------------------------------------------
            \t\t\t\t|                                                 |
            \t\t\t\t|                                                 |
            \t\t\t\t|                                                 |
            \t\t\t\t|           CHARITY MANAGEMENT SYSTEM             |
            \t\t\t\t|                                                 |
            \t\t\t\t|                                                 |
            \t\t\t\t|                                                 |
            \t\t\t\t|                                                 |
            \t\t\t\t---------------------------------------------------''')
    }


def donation_amount(): #Repeated pattern displayed when someone makes a donation
    {
        print('''
                \t\t\t\t---------------------------------------------------
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|         How Much Do You want to donate?         |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t---------------------------------------------------''')
    }

root = tk.Tk()


def call_name(): #Pattern Called when Input of Name required from user
    {
        print('''
            \t\t\t\t---------------------------------------
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|         Enter your name             |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t---------------------------------------''')
    }


def thanks_message(): #Thankyou message for registeration and making a donation
    {
        print('''
                ---------------------------------------------------
                |                                                 |
                |                                                 |
                |                                                 |
                |               THANK YOU!                        |
	            |       Your decision has been recorded           |
                |                                                 |
                |                                                 |
                ---------------------------------------------------''')
    }





def get_slip(): #Message Before Slip generation
    print('''
                        \t\t\t\t---------------------------------------------------
                        \t\t\t\t|                                                 |
                        \t\t\t\t|                                                 |
                        \t\t\t\t|                                                 |
                        \t\t\t\t|     Press 1 to get a slip of your donation.     |
                        \t\t\t\t|                                                 |
                        \t\t\t\t|                                                 |
                        \t\t\t\t---------------------------------------------------''')


def thanks_choice(): #Thankyou message at the end
    print('''
                          \t\t\t\t---------------------------------------------------
                          \t\t\t\t|                                                 |
                          \t\t\t\t|                    THANK YOU                    |
                          \t\t\t\t|                      for                        |
                          \t\t\t\t|                    Choosing                     |
                          \t\t\t\t|                      CMS                        |
                          \t\t\t\t|                                                 |
                          \t\t\t\t|                                                 |
                          \t\t\t\t|                                                 |
                          \t\t\t\t---------------------------------------------------''')


def approval_pending(): #If status of request is PENDING
    print("Approval is pending.")
    


def valid_key(): #Function called when invalid key is displayed
    print('''
            \t\t\t\t---------------------------------------
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|            Press a valid            |
            \t\t\t\t|                 key                 |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t---------------------------------------''')


def rejection_status(): #Function called when Request Status is Rejected
    print('''
            \t\t\t\t---------------------------------------
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|        Sorry! The request has       |
            \t\t\t\t|            been rejected.           |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t---------------------------------------''')

    byegui()


def registered_case():#Function called when request is submitted by user
    print('''
            \t\t\t\t---------------------------------------
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|            Your Request             |
            \t\t\t\t|              has been               |
            \t\t\t\t|             Registered              |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t---------------------------------------''')


def thanks_for_choice():
    print('''
            \t\t\t\t---------------------------------------
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|        Thank you for choosing       |
            \t\t\t\t|                CMS                  |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t---------------------------------------''')


def make_case(state): #Function called when new cases registered
   
    print("\t\t\t", state)

def welgui():
    #GUI that is shown when you run program
    
    
    root.minsize(400, 200)
    root.maxsize(700, 200)


    root.title("Welcome")

    label = tk.Label(root, text="Welcome to Charity Management System Copyright © 1997 ASH Technologies Private Limited!\n\nMade by:\n\nHira Sardar\nMuhammad Sami Ullah\nMuhammad Abbas\n\nBSCS12-C")
    label.pack()

    button = tk.Button(root, text="Continue", command=close_window)
    button.pack()

    root.mainloop()

def close_window():
    root.destroy()






welgui()

password = 1234
edhi_edu1 = 50000
chaddar_edu1 = 20000
edhi_health1 = 100000
chaddar_health1 = 20000
edhi_food1 = 15000
chaddar_food1 = 30000


print("Are you an Admin or User (1:admin,0;user)? ")
personality = int(input())
if (personality == 0): #Initiates a series of commands if you are a USER
    count = 0
    print("Do you want to sign-up or log-in")
    print("Press 1 to sign-up and 0 to log-in") #Different Login and Signup options
    user = int(input())
    while (user == 1):
        print('''
            \t\t\t\t---------------------------------------
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|         Enter your name             |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t---------------------------------------''')
        name = input()
        os.system('cls') #clears screen
        print('''
            \t\t\t\t---------------------------------------
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|         Enter your CNIC             |
            \t\t\t\t|    (without Dashes or Spaces)       |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t---------------------------------------''')
        cnic = int(input())
        os.system('cls')
        print('''
            \t\t\t\t---------------------------------------
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|         Enter your password         |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t---------------------------------------''')
        passcode = input()
        os.system('cls') #clears screen
        passcode = passcode+"\n"
        fp1 = open("password.txt", "a")
        fp1.write(passcode)
        print("In case you forget your password") #A useful feature for when you forget password
        print('''
            \t\t\t\t---------------------------------------
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|       Enter your school name        |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t---------------------------------------''')
        school = input()
        school = school+"\n"
        fp2 = open("School.txt", "a")
        fp2.write(school)
        fp1.close()
        fp2.close()
        os.system('cls')
        break
    while (user == 0):
        print("How do you want to login?") #Login via Password or your school's name
        print('''
            \t\t\t\t---------------------------------------
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t|         Press 1 to login            |
            \t\t\t\t|            by password              |
            \t\t\t\t|         Press 0 to login            |
            \t\t\t\t|            by question              |
            \t\t\t\t|                                     |
            \t\t\t\t|                                     |
            \t\t\t\t---------------------------------------''')
        log_in = int(input())
        os.system('cls')
        if (log_in == 1): #If user decides to log in using password
            print('''
                \t\t\t\t---------------------------------------
                \t\t\t\t|                                     |
                \t\t\t\t|                                     |
                \t\t\t\t|         Enter your password         |
                \t\t\t\t|                                     |
                \t\t\t\t|                                     |
                \t\t\t\t|                                     |
                \t\t\t\t|                                     |
                \t\t\t\t|                                     |
                \t\t\t\t---------------------------------------''')
            passcode = input()
            passcode = passcode+"\n"
            fp1 = open("password.txt", "r") #Checks if password matches with one in the file
            for line in fp1.readlines():
                if line == passcode:
                    count = count+1
                else:
                    pass
            break
        os.system('cls')
        if (log_in == 0): #If user wants to login via School Name
            print('''
                        \t\t\t\t---------------------------------------
                        \t\t\t\t|                                     |
                        \t\t\t\t|                                     |
                        \t\t\t\t|       Enter your school name        |
                        \t\t\t\t|                                     |
                        \t\t\t\t|                                     |
                        \t\t\t\t|                                     |
                        \t\t\t\t|                                     |
                        \t\t\t\t|                                     |
                        \t\t\t\t---------------------------------------''')
            school = input()
            school = school+"\n"
            fp2 = open("School.txt", "r") #Checks if school name matches with one in the file
            for line in fp2.readlines():
                if line == school:
                    count = count+1
                else:
                    pass
            break
        os.system('cls')
        if (count == 0): #in case of wrong password, 3 tries
            for d in range(3):
                print("WRONG PASSWORD")
                print("PLEASE TYPE RIGHT PASSWORD")
                password = input()
                password = password + "\n"
                fp1 = open("password.txt", "r")
                for line in fp1.readlines():
                    if line == password:
                        count = count+1
                        break
                    else:
                        pass
            break

    if (count >= 1): #User's Options
        os.system('cls')
        pattern()
        print('''
                 \t\t\t---------------------------------------------------
                 \t\t\t|                                                 |
                 \t\t\t|                                                 |
                 \t\t\t|          To Make a Donation (press 1)           |
                 \t\t\t|                                                 |
                 \t\t\t|        To Request for a Donation (press 2)      |
                 \t\t\t|                                                 |
                 \t\t\t|      To check for Donation Status (press 3)     |
                 \t\t\t|                                                 |
                 \t\t\t|                                                 |
                 \t\t\t---------------------------------------------------''')
        print("\n")
        donation = int(input())
        os.system('cls')
        if (donation == 1): #User wants to make a donation
            pattern()
            call_name()
            name = input()
            os.system('cls')
            #Multiple Options he can donate to
            print('''
                     \t\t\t\t---------------------------------------------------
                     \t\t\t\t|                                                 |
                     \t\t\t\t|       Organization you want to donate to        |
                     \t\t\t\t|                                                 |
                     \t\t\t\t|                                                 |
                     \t\t\t\t|           Edhi Organization (press 1)           |
                     \t\t\t\t|                                                 |
                     \t\t\t\t|          Chadar Organization (press2)           |
                     \t\t\t\t|                                                 |
                     \t\t\t\t|           Registered Cases (press 3)            |
                     \t\t\t\t|                                                 |
                     \t\t\t\t|                          Your Need is our Need  |
                    \t\t\t\t---------------------------------------------------''')
            org = int(input())
            os.system('cls')
            if (org == 3): #For the registered cases 
                pattern()
                print("\t\t\t---------------------------------------------------")
                fp10= open("Approval.txt","r")

                for line in fp10.readlines(): #reads from file of Approved cases
                    newcase = line
                    make_case(newcase)
                fp10.close()

                print("\t\t\t---------------------------------------------------")
                donation_amount()
                print("\t\t\t")
                newcase_donation = int(input())
                get_slip()
                get_a_slip = int(input())
                if (get_a_slip == 1):
                    #The message you get after sucessful donation
                    thanks_choice()
                    print('''
                            \t\t\t\t---------------------------------------
                            \t\t\t\t|                                     |
                            \t\t\t\t|                                     |
                            \t\t\t\t|            You Donated              |
                            \t\t\t\t\t      ''',newcase_donation,'''         
                            \t\t\t\t|              for the cause          |
                            \t\t\t\t|                                     |
                            \t\t\t\t|                                     |
                            \t\t\t\t|                                     |
                            \t\t\t\t---------------------------------------''')
        



                      

            if (org == 1) or (org == 2): #If user opts to request donation or makes donation to non-app registered cases
                pattern()
                print('''
                         \t\t\t\t---------------------------------------------------
                         \t\t\t\t|                                                 |
                         \t\t\t\t|         You want to donate for what cause       |
                         \t\t\t\t|                                                 |
                         \t\t\t\t|                                                 |
                         \t\t\t\t|              Education (press 1)                |
                         \t\t\t\t|                Health  (press2)                 |
                         \t\t\t\t|            Food & Shelter (Press 3)             |
                         \t\t\t\t|                                                 |
                         \t\t\t\t|                                                 |
                         \t\t\t\t|                          Your Need is our Need! |
                         \t\t\t\t---------------------------------------------------''')
                print("\n")
                cause_donation = int(input())
                os.system('cls')

                #Beginning of MULTIPLE STORED CASES AND THEIR DONATION FLOW
                if (org == 1 and cause_donation == 1):
                    if (edhi_edu1 > 0):
                        pattern()
                        print('''
                             \t\t\t\t----------------------------------------------------------------
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|       Muhammad Ahmad needs''', edhi_edu1, ''' to pay semester fee        |
                             \t\t\t\t|                (press 1)                                     |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                       Your Need is our Need! |
                            \t\t\t\t----------------------------------------------------------------''')
                        educase = int(input())
                        if (educase == 1):
                            
                            donation_amount()
                            how_much_donated = int(input())
                            need_donation = edhi_edu1
                            edhi_edu1 = edhi_edu1 - how_much_donated #deduction of amount from the data
                            left_amount = edhi_edu1
                            
                if (org == 1 and cause_donation == 2):
                    if (edhi_health1 > 0):
                        os.system('cls')
                        pattern()
                        print('''
                             \t\t\t\t----------------------------------------------------------------
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|       Ali Hussain needs ''', edhi_health1, ''' for his stent placement.     |
                             \t\t\t\t|                (press 1)                                     |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                       Your Need is our Need! |
                            \t\t\t\t----------------------------------------------------------------''')
                        healthcase = int(input())
                        if (healthcase == 1):
                            donation_amount()
                            how_much_donated = int(input())
                            need_donation = edhi_health1
                            edhi_health1 = edhi_health1 - how_much_donated #deduction of amount from the data
                            left_amount = edhi_edu1

                if (org == 1 and cause_donation == 3):
                    if (edhi_food1 > 0):
                        pattern()
                        print('''
                             \t\t\t\t----------------------------------------------------------------
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|           Saira khan requires''', edhi_food1, '''for her groceries.       |
                             \t\t\t\t|                       (press 1)                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                       Your Need is our Need! |
                            \t\t\t\t----------------------------------------------------------------''')
                        foodcase = int(input())
                        if (foodcase == 1):
                            
                            donation_amount()
                            how_much_donated = int(input())
                            need_donation = edhi_food1
                            edhi_food1 = edhi_food1 - how_much_donated #deduction of amount from the data
                            left_amount = edhi_food1
                if (org == 2 and cause_donation == 1):
                    if (chaddar_edu1 > 0):
                        os.system('cls')
                        pattern()
                        print('''
                             \t\t\t\t----------------------------------------------------------------
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|      Hadia Ahmad needs ''', chaddar_edu1, ''' to pay her semester fee.      |
                             \t\t\t\t|                (press 1)                                     |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                       Your Need is our Need! |
                            \t\t\t\t----------------------------------------------------------------''')
                        educase = int(input())
                        if (educase == 1):
                           
                            donation_amount()
                            how_much_donated = int(input())
                            need_donation = chaddar_edu1
                            chaddar_edu1 = chaddar_edu1 - how_much_donated #deduction of amount from the data
                            left_amount = chaddar_edu1

                if (org == 2 and cause_donation == 2):
                    if (chaddar_health1 > 0):
                        os.system('cls')
                        pattern()
                        print('''
                             \t\t\t\t----------------------------------------------------------------
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|      Muhammad Saqib needs ''', chaddar_health1, ''' to pay for Chemotherapy.   |
                             \t\t\t\t|                (press 1)                                     |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                       Your Need is our Need! |
                            \t\t\t\t----------------------------------------------------------------''')
                        healthcase = int(input())
                        if (healthcase == 1):
                            
                            donation_amount()
                            how_much_donated = int(input())
                            need_donation = chaddar_health1
                            chaddar_health1 = chaddar_health1 - how_much_donated #deduction of amount from the data
                            left_amount = chaddar_health1
                if (org == 2 and cause_donation == 3): 
                    if (chaddar_food1 > 0):
                        os.system('cls')
                        pattern()
                        print('''
                             \t\t\t\t----------------------------------------------------------------
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|   Javaid Ali requires ''', chaddar_food1, ''' to build a room  in his house  |
                             \t\t\t\t|                (press 1)                                     |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                                              |
                             \t\t\t\t|                                       Your Need is our Need! |
                            \t\t\t\t----------------------------------------------------------------''')
                        foodcase = int(input())
                        if (foodcase == 1):
                            
                            donation_amount()
                            how_much_donated = int(input())
                            need_donation = chaddar_food1
                            chaddar_food1 = chaddar_food1 - how_much_donated #deduction of amount from the data
                            left_amount = chaddar_food1

                if (cause_donation == 1): #Keeping a record of all the donation data in a file
                    record_information = name+"\t\t" + \
                        str(need_donation)+"\t\t" + \
                        str(how_much_donated)+"\t\t"+"Education"
                if (cause_donation == 2):
                    record_information = name+"\t\t" + \
                        str(need_donation)+"\t\t" + \
                        str(how_much_donated)+"\t\t"+"Health"
                if (cause_donation == 3):
                    record_information = name+"\t\t" + \
                        str(need_donation)+"\t\t"+str(how_much_donated) + \
                        "\t\t"+"Food and Shelter"
                fp8 = open("Record.txt", "a") #making changes in record data
                fp8.write(record_information)
                fp8.close()
                get_slip()
                slip = int(input())
                if (slip == 1):
                    thanks_choice()
                    print('''
                          \t\t\t\t---------------------------------------
                          \t\t\t\t|                                     |
                          \t\t\t\t|                                     |
                          \t\t\t\t|            You donated              |
                          \t\t\t\t|               ''', how_much_donated, '''            |
                          \t\t\t\t|           for the cause             |
                          \t\t\t\t|                                     |
                          \t\t\t\t|                                     |
                          \t\t\t\t|                                     |
                          \t\t\t\t---------------------------------------''')
                    byegui()

        if (donation == 2):#If user opts for request
            call_name()
            name = input()
            os.system('cls')
            pattern()
            print('''
                  \t\t\t---------------------------------------------------
                  \t\t\t|                                                 |
                  \t\t\t| Organization you want to request donation from  |
                  \t\t\t|                                                 |
                  \t\t\t|                                                 |
                  \t\t\t|           Edhi Organization (press 1)           |
                  \t\t\t|                                                 |
                  \t\t\t|          Chadar Organization (press2)           |
                  \t\t\t|                                                 |
                  \t\t\t|                          Your Need is our Need! |
                  \t\t\t|--------------------------------------------------''')
            print("\n")
            org = int(input())
            # system("cls");
            if (org == 1 or org == 2): #Pick organization of choice
                pattern()
                print('''
                      \t\t\t---------------------------------------------------
                      \t\t\t|                                                 |
                      \t\t\t|   You want to request donation for what cause   |
                      \t\t\t|                                                 |
                      \t\t\t|                                                 |
                      \t\t\t|              Education (press 1)                |
                      \t\t\t|                                                 |
                      \t\t\t|                Health  (press2)                 |
                      \t\t\t|                                                 |
                      \t\t\t|            Food & Shelter (Press 3)             |
                      \t\t\t|                                                 |
                      \t\t\t|                                                 |
                      \t\t\t|                          Your Need is our Need! |
                      \t\t\t---------------------------------------------------''')
                print("\n")
                cause_donation = int(input())
                if (cause_donation == 1 or cause_donation == 2 or cause_donation == 3):
                    os.system('cls')
                    pattern()
                    print("\n")
                    #Learning the exact purpose, and saving it in a file
                    print('''
                          \t\t\t----------------------------------------------------------------------
                          \t\t\t|                                                                    |
                          \t\t\t|                                                                    |
                          \t\t\t|                                                                    |
                          \t\t\t|                                                                    |
                          \t\t\t|                                                                    |
                          \t\t\t|Mention the exact purpose for your request(e.g to pay hostel dues)  |
                          \t\t\t|       Reason should exceed no more than 290 letters:               |
                          \t\t\t|                                                                    |
                          \t\t\t|                                                                    |
                          \t\t\t|                                                                    |
                          \t\t\t|                                                                    |
                          \t\t\t|                                                                    |
                          \t\t\t|                                             Your Need is our Need! |
                        \t\t\t------------------------------------------------------------------------''')
                    reason = input()
                    os.system('cls')
                    print('''
                          \t\t\t---------------------------------------
                          \t\t\t|                                     |
                          \t\t\t|                                     |
                          \t\t\t|         Enter the desired           |
                          \t\t\t|              amount                 |
                          \t\t\t|                                     |
                          \t\t\t|                                     |
                          \t\t\t|                                     |
                          \t\t\t|                                     |
                          \t\t\t---------------------------------------''')
                    amount = int(input())
                    information = name+" needs " + \
                        str(amount)+ str(reason)+"\n"
                    fp = open("Administration.txt", "a") #A file for Admin to see the requests from
                    fp.write(information)
                    fp.close()
                    os.system('cls')
                    get_slip()
                    slip = int(input())
                    os.system('cls')
                    if (slip == 1):
                        registered_case()
                        byegui()
        if (donation == 3):#Check if rejected
            os.system('cls')
            call_name()
            name = input()
            fp7 = open("Rejection.txt", "r")
            for line in fp7.readlines():
                if name in line:
                    rejection_status()
                else:
                    approval_pending()
            fp7.close()
        elif (donation != 1) and (donation != 2) and (donation != 3):
            pattern()
            valid_key()

            org = int(input())
if (personality == 1): #ADMIN SIDE of the program
    
    print("\tEnter the ADMINISTRATION Password: ")
    entered_password = int(input()) #Checking Password
    os.system('cls')
    if (entered_password == password):
        print("What do you want to do?") #Purpose of the ADMIN
        print('''
              ---------------------------------------------------
              |                                                 |
              |                                                 |
              |                                                 |
              |           FOR APPROVING THE ONES WHO            |
              |                   WANT TO GET DONATIONS         |
              |                 PRESS(1)                        |
              |           FOR GETTING THE RECORD OF             |
              |                   DONATIONS MADE,               |
              |                 PRESS (2)                       |
              |                                                 |
              |                                                 |
              ---------------------------------------------------''')
        approval = int(input())
        if (approval == 1): #Check the requests and approve or reject them
            print("CASES\n")
            fp = open("Administration.txt", "r")
            #statements = fp.readlines()
            for line in fp.readlines():
                print(line)
            fp.close()
            os.system('cls')

            print('''
                \t\t\t\t---------------------------------------------------
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|         What is your decision?                  |
                \t\t\t\t|             PRESS 1                             |
                \t\t\t\t|                                                 |
                \t\t\t\t|            To Accept                            |
                \t\t\t\t|             PRESS 0                             |
                \t\t\t\t|                To Reject                        |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t---------------------------------------------------''')
            decision = int(input())
            os.system('cls')
            if (decision == 1):
                fp3 = open("Approval.txt", "a")
                #Checking which user is rejected or approved
                print('''
                \t\t\t\t---------------------------------------------------
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|         Can you please elaborate                |
                \t\t\t\t|           the name of the user                  |
                \t\t\t\t|             of whom , you have                  |
                \t\t\t\t|               given decision?                   |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t---------------------------------------------------''')
                recipient = input()
                #Confirming the cause for which user made a request
                print('''
                         \t\t\t\t---------------------------------------------------
                         \t\t\t\t|                                                 |
                         \t\t\t\t|         The User requested for what cause:      |
                         \t\t\t\t|                                                 |
                         \t\t\t\t|                                                 |
                         \t\t\t\t|              Education (press 1)                |
                         \t\t\t\t|                Health  (press2)                 |
                         \t\t\t\t|            Food & Shelter (Press 3)             |
                         \t\t\t\t|                                                 |
                         \t\t\t\t|                                                 |
                         \t\t\t\t|                          Your Need is our Need! |
                         \t\t\t\t---------------------------------------------------''')                         
                cause = int(input())
                fp = open("Administration.txt")
                for line in fp.readlines():
                    if recipient in line:
                        sentence = line
                        break
                #separate files for each type of case of the user
                if (cause == 1):
                    fp4 = open("Education.txt", "a")
                    fp4.write(sentence)
                    fp4.close()
                if (cause == 2):
                    fp5 = open("Health.txt", "a")
                    fp5.write(sentence)
                    fp5.close()
                if (cause == 3):
                    fp6 = open("Food and Shelter.txt", "a")
                    fp6.write(sentence)
                    fp6.close()
                fp3.write(sentence)
                fp.close()
                fp3.close()
            print("\n")
            thanks_message()

            if (decision == 0): #If the Admin rejects a request
                os.system('cls')
                fp7 = open("Rejection.txt", "a")
                print('''
                \t\t\t\t---------------------------------------------------
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|         Can you please elaborate                |
                \t\t\t\t|           the name of the user                  |
                \t\t\t\t|             of whom , you have                  |
                \t\t\t\t|               given decision?                   |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t|                                                 |
                \t\t\t\t---------------------------------------------------''')
                recipient = input()
                fp = open("Administration.txt")
                for line in fp.readlines():
                    if recipient in line:
                        sentence = line
                        break
                fp7.write(sentence)
                fp.close()
                fp7.close()
                print("\n")
                byegui()

        if (approval == 2): #Shows admin the record of donations
            print("DONOR\tAMOUNT NEEDED\tAMOUNT DONATED\tLEFT AMOUNT\tPORTFOLIO")
            fp8 = open("Record.txt", "r")
            for line in fp8.readlines():
                record_statement = line
                print(record_statement)
            fp8.close()
            byegui()
elif ((personality != 0) and (personality != 1)):
    while (i < 3):
        print("\n\n\t\t\t\tWrong Password\n")
        print("\t\t\t\tEnter Password: ")
        entered_password = int(input())
        i = i+1
    print("\t\t\t\tNo more Tries!")



