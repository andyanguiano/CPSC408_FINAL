#Andy Anguiano
#CPSC408-01
#FINAL

#import necessary files
import Helpers
import mysql.connector

#connect to database with my specific login information
db = mysql.connector.connect(
    host="34.94.182.22",
    user="aanguiano@chapman.edu",
    passwd="FooBar!@#$",
    database="aanguiano_db2"
)

# main menu
def menu():
    while True:
        print("TOP ELECTRONICS")
        print("----------------")
        print("1. Display All Tables")
        print("2. Filter Through Data")
        print("3. Create New Records")
        print("4. Edit Records")
        print("5. Delete Records")
        print("6. Generate Reports")
        print("7. Exit Program")
        choice = input("Enter the number of the option you would like to execute: ")
        if choice == "1":
            print("\n")
            Helpers.displayTables()
        elif choice == "2":
            print("\n")
            filterMenu()
        elif choice == "3":
            print("\n")
            createMenu()
        elif choice == "4":
            print("\n")
            editMenu()
        elif choice == "5":
            print("\n")
            deleteMenu()
        elif choice == "6":
            print("\n")
            reportMenu()
        elif choice == "7":
            print("\n")
            print("Exiting")
            #mycursor.execute('DELETE FROM Student')
            #conn.commit()
            break
        else:
            print("\n")
            print("Invalid input. Try Again")
            print("\n")
            continue

#menu for filters
def filterMenu():
    print("Which table to filter through:")
    print("1. Parts")
    print("2. Suppliers")
    print("3. Customers")
    print("4. Employees")
    print("5. Invoices")
    print("6. Back to main menu")
    choice = input("Enter the number of the option you would like to execute: ")
    if choice != "6":
        Helpers.filterThrough(choice)
        print("\n")
        return
    elif choice == "6":
        return
    else:
        print("Invalid Option. Try Again")
        filterMenu()
        return

#menu for creating data
def createMenu():
    print("Which table to add to:")
    print("1. Parts")
    print("2. Suppliers")
    print("3. Customers")
    print("4. Employees")
    print("5. Invoices")
    print("6. Back to main menu")
    choice = input("Enter the number of the option you would like to execute: ")
    if choice != "6":
        Helpers.createData(choice)
        print("\n")
        return
    elif choice == "6":
        return
    else:
        print("Invalid Option. Try Again")
        createMenu()
        return

#menu for editing data
def editMenu():
    print("Which table to edit records:")
    print("1. Parts")
    print("2. Suppliers")
    print("3. Customers")
    print("4. Employees")
    print("5. Invoices")
    print("6. Back to main menu")
    choice = input("Enter the number of the option you would like to execute: ")
    if choice != "6":
        Helpers.editData(choice)
        print("\n")
        return
    elif choice == "6":
        return
    else:
        print("Invalid Option. Try Again")
        editMenu()
        return

#menu for deleting data
def deleteMenu():
    print("Which table to delete records:")
    print("1. Parts")
    print("2. Suppliers")
    print("3. Customers")
    print("4. Employees")
    print("5. Invoices")
    print("6. Back to main menu")
    choice = input("Enter the number of the option you would like to execute: ")
    if choice != "6":
        Helpers.deleteData(choice)
        print("\n")
        return
    elif choice == "6":
        return
    else:
        print("Invalid Option. Try Again")
        deleteMenu()
        return

#menu for exporting reports
def reportMenu():
    print("")
    print("Reports to Export:")
    print("1. All Unfulfilled Orders")
    print("2. Invoices Requiring Parts from Certain Country")
    print("3. Contact Information of customers for all Unfulfilled Orders")
    print("4. Back to main menu")

    choice = input("Enter the number of the option you would like to execute: ")
    if choice == "4":
        return
    elif choice == "1":
        Helpers.generateReports(choice)
        print("\n")
        return
    elif choice == "2":
        Helpers.generateReports(choice)
        print("\n")
        return
    elif choice == "3":
        Helpers.generateReports(choice)
        print("\n")
        return
    else:
        print("Invalid Option. Try Again")
        reportMenu()
        return