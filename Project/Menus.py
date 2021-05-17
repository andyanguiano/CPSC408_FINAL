#Andy Anguiano
#CPSC408-01
#FINAL

#import necessary files
import Helpers
import mysql.connector
import csv
import pandas as pd
from pandas import DataFrame
import datetime

#connect to database with my specific login information
db = mysql.connector.connect(
    host="34.94.182.22",
    user="aanguiano@chapman.edu",
    passwd="FooBar!@#$",
    database="aanguiano_db2"
)

def test():
    mycursor = db.cursor()
    #mycursor.execute("CREATE TABLE Supplier(ID INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(60), Email VARCHAR(80), Country VARCHAR(60), isDeleted SMALLINT)")
    #db.commit()
    #mycursor.execute("CREATE TABLE Invoice(ID INT PRIMARY KEY AUTO_INCREMENT, PartID INT, Count INT, Date DATE, Fulfilled SMALLINT, EmployeeID INT, CustomerID INT, isDeleted SMALLINT,"
                     #"FOREIGN KEY (PartID) REFERENCES Part(ID), FOREIGN KEY (EmployeeID) REFERENCES Employee(ID), FOREIGN KEY (CustomerID) REFERENCES Customers(ID))")
    #db.commit()
    #mycursor.execute("INSERT INTO Supplier(Name, Email, Country) VALUES('South Coast Parts', 'jondoe@scparts.com', 'United States')")
    #mycursor.execute("INSERT INTO Part(Name, Weight, SupplierID) VALUES('Black Bearing Ring', '0.5', 1)")
    #db.commit()
    mycursor.execute("Describe Invoice")

    print(mycursor.fetchall())
    print(datetime.date.today())

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

def reportMenu():
    print("")
    print("Reports to Export:")
    print("")

    choice = input("Enter the number of the option you would like to execute: ")
    if choice != "6":
        Helpers.generateReports(choice)
        print("\n")
        return
    elif choice == "6":
        return
    else:
        print("Invalid Option. Try Again")
        reportMenu()
        return