import time

print("Please insert Your CARD")

#for card processing
time.sleep(3)

password = 1234

#taking atm pin from user
pin = int(input("enter your atm pin "))

#user account balance
balance = 500000

#checking pin is valid or not 
if pin == password:
    #loop will run user get free 
    while True:

        #Showing  info to user

        print(""" 
			1 == balance
			2 == withdraw balance
			3 == deposit balance
			4 == exit
			5 == change pin
			"""
              )

        try:    
             #taking an option from user
            option = int(input("Please enter your choise "))
        except:
            print("Please enter valid option")
        
        #for option 1        
        if option == 1:
            print(f"Your current balance is {balance}")
                                     
        if option == 2:

            withdraw_amount = int(input("please enter withdraw_amount "))

            

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            

            print(f"your updated balance is {balance}")
            print("Do you want receipt")

            ans=input("""
                         1-yes
                         2-no
                         """
                      )

            if ans=="1":
                print("printing the receipt please wait")
                time.sleep(3)
            elif ans=="2":
                print("Thank you")

            

        if option == 3:

            deposit_amount = int(input("please enter deposit_amount"))

            balance = balance + deposit_amount

            

            print(f"{deposit_amount} is credited to your account")



            print(f"your updated balance is {balance}")



        if option == 4:
            print("Thankyou for using our services")

            break

    
        if option== 5:
            
            v=int(input("please enter current pin"))
            
            if v==password:
                
                password=int(input("enter new pin"))
                
                print("new password updated",password)

                
            else:
                print("please enter the correct pin")


else:
    print("wrong pin Please try again")
