#expense tracker project

expensesList= [] # list of  expenses in form of dictionary
print("welcome to Expense Tracker: ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View ALL Expenses" )
    print("3. View Total Expenses ")
    print("4. Exit")

    choice= int(input("Please Enter your Choice: "))

# ADD Expense


    if(choice ==1):
        date= input("On which date  was the expenditure made ?: ")
        category= input("What type of expenses? (Food , Travel, Games, Books): ")
        description= input("Give more details: ")
        amount= float(input("Enter the Amount: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n DONE bro. Expense is added successfully")


# 2. VIEW ALL EXPENSES


    elif(choice==2): 
        if(len(expensesList)==0):
            print("No Expense Added. Go Spend first. ")
        else:
            print("==== THIS IS ALL YOUR EXPENSES ====")
            count= 1
            for eachKharcha in expensesList:
                print(f"kharcha  Number {count} -> {eachKharcha["date"]}, {eachKharcha["category"]} {eachKharcha["description"]}, {eachKharcha["amount"]} ")  
                count= count+1

# 3. VIEW TOTAL  SPENDING


    elif(choice==3):
        total= 0
        for eachKharcha in expensesList:
            total= total + eachKharcha["amount"]

            print("\n TOTAL EXPENSE= ", total)

# EXIT


    elif(choice== 4):
        print(" Thank you for making our system Work")
        break
    else:
        print("INVALID CHOICE. TRY AGAIN")














