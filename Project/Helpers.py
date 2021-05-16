
import pandas as pd
import mysql.connector
from pandas import DataFrame
import datetime

#connect to database with my specific login information
db = mysql.connector.connect(
    host="34.94.182.22",
    user="aanguiano@chapman.edu",
    passwd="FooBar!@#$",
    database="aanguiano_db2"
)

mycursor = db.cursor()

def displayTables():
    print("PARTS:")
    mycursor.execute('SELECT * FROM Part WHERE isDeleted is NULL')
    records = mycursor.fetchall()
    df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
    print(df.loc[:, 'ID':'SupplierID'])
    print("\n")

    print("SUPPLIERS:")
    mycursor.execute('SELECT * FROM Supplier WHERE isDeleted is NULL')
    records = mycursor.fetchall()
    df = DataFrame(records, columns=['ID', 'Email', 'Country', 'isDeleted', 'Name'])
    newDF = df[['ID','Name', 'Email', 'Country']]
    print(newDF)
    print("\n")

    print("CUSTOMERS:")
    mycursor.execute('SELECT * FROM Customer WHERE isDeleted is NULL')
    records = mycursor.fetchall()
    df = DataFrame(records, columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
    print(df.loc[:, 'ID':'numOrders'])
    print("\n")

    print("EMPLOYEE:")
    mycursor.execute('SELECT * FROM Employee WHERE isDeleted is NULL')
    records = mycursor.fetchall()
    df = DataFrame(records, columns=['ID', 'Name', 'Email', 'isDeleted'])
    print(df.loc[:, 'ID':'Email'])
    print("\n")

    print("INVOICE:")
    mycursor.execute('SELECT * FROM Invoice WHERE isDeleted is NULL')
    records = mycursor.fetchall()
    df = DataFrame(records,
                   columns=['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID', 'isDeleted'])
    print(df.loc[:, 'ID':'CustomerID'])
    print("\n")


def filterThrough(choice):
    print("\n")
    if choice == "1":
        print("Aspects to filter:")
        print("1. Parts from certain Supplier")
        print("2. Weight less than")
        print("3. Weight greater than")
        theFilter = input("Enter the number of the option you would like to execute: ")
        print("\n")

        if theFilter == "1":
            print("SUPPLIERS:")
            mycursor.execute('SELECT * FROM Supplier WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Email', 'Country', 'isDeleted', 'Name'])
            newDF = df[['ID', 'Name', 'Email', 'Country']]
            print(newDF)
            print("\n")
            supplier = input("Enter the ID number of the Supplier: ")
            print("\n")
            mycursor.execute('SELECT * FROM Part WHERE SupplierID = ' + supplier)
            records = mycursor.fetchall()
            # check if input valid
            if records == []:
                print("Invalid Input. Please Try Again.")
                filterThrough(choice)
                return
            else:
                print("PARTS:")
                df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
                print(df.loc[:, 'ID':'SupplierID'])
                return

        elif theFilter == "2":
            weight = input("Enter the Weight: ")
            mycursor.execute('SELECT * FROM Part WHERE Weight <= ' + weight)
            output = mycursor.fetchall()
            print("PARTS:")
            df = DataFrame(output, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
            print(df.loc[:, 'ID':'SupplierID'])

        elif theFilter == "3":
            weight = input("Enter the Weight: ")
            mycursor.execute('SELECT * FROM Part WHERE Weight >= ' + weight)
            output = mycursor.fetchall()
            print("PARTS:")
            df = DataFrame(output, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
            print(df.loc[:, 'ID':'SupplierID'])

    elif choice == "2":
        print("Filter by country: ")
        print("SUPPLIERS:")
        mycursor.execute('SELECT Country FROM Supplier WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['Country'])
        print(df)
        print("\n")
        country = input("Country ID you would like to filter by (number): ")
        try:
            mycursor.execute('SELECT * FROM Supplier WHERE Country = ' + country)
        except mysql.connector.Error:
            print("Invalid Input. Please Try Again.")
        except TypeError:
            print("Invalid Input. Please Try Again.")
        records = mycursor.fetchall()
        if records == []:
            print("\n")
            print("Invalid Input. Please Try Again.")
            filterThrough(choice)
            return
        else:
            print("\n")
            print("SUPPLIERS:")
            df = DataFrame(records, columns=['ID', 'Email', 'Country', 'isDeleted', 'Name'])
            newDF = df[['ID', 'Name', 'Email', 'Country']]
            print(newDF)
            return

    elif choice == "3":
        print("Filter Customers through number of orders.")
        print("1. Number of orders less than")
        print("2. Number of orders greater than")
        theFilter = input("Enter the number of the option you would like to execute: ")

        if theFilter == "1":
            orderNum = input("Enter the number of orders: ")
            mycursor.execute('SELECT * FROM Customer WHERE numOrders <= ' + orderNum + ' and isDeleted is NULL')
            output = mycursor.fetchall()
            if output == []:
                print("\n")
                print("There is no data that matches your filter.")
                return
            else:
                print("\n")
                print("CUSTOMERS:")
                df = DataFrame(output,
                               columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
                print(df.loc[:, 'ID':'numOrders'])
                print("\n")
                return


        elif theFilter == "2":
            orderNum = input("Enter the number of orders: ")
            mycursor.execute('SELECT * FROM Customer WHERE numOrders >= ' + orderNum + ' and isDeleted is NULL')
            output = mycursor.fetchall()
            if output == []:
                print("\n")
                print("There is no data that matches your filter.")
                return
            else:
                print("\n")
                print("CUSTOMERS:")
                df = DataFrame(output,
                               columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
                print(df.loc[:, 'ID':'numOrders'])
                print("\n")
                return

    elif choice == "4":
        print("There are no queries for Employees currently")

    elif choice == "5":
        print("Which would you like to filter by:")
        print("1. Unfulfilled Orders")
        print("2. Orders of Part")
        print("3. Orders of Customer")
        theFilter = input("Enter the number of the option you would like to execute: ")
        print("\n")

        if theFilter == "1":
            print("INVOICE:")
            mycursor.execute('SELECT * FROM Invoice WHERE Fulfilled = 0 and isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID', 'isDeleted'])
            print(df.loc[:, 'ID':'CustomerID'])
            print("\n")

        elif theFilter == "2":
            print("PARTS:")
            mycursor.execute('SELECT * FROM Part WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
            print(df.loc[:, 'ID':'SupplierID'])
            print("\n")

            part = input("Enter the ID number of the Part: ")
            print("\n")
            mycursor.execute('SELECT * FROM Invoice WHERE PartID = ' + part + ' and isDeleted is NULL')
            records = mycursor.fetchall()
            if records == []:
                print("\n")
                print("There is no data that matches your filter.")
                return
            else:
                print("\n")
                print("INVOICE:")
                df = DataFrame(records,
                               columns=['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID',
                                        'isDeleted'])
                print(df.loc[:, 'ID':'CustomerID'])
                print("\n")
                return

        elif theFilter == "3":
            print("CUSTOMERS:")
            mycursor.execute('SELECT * FROM Customer WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
            print(df.loc[:, 'ID':'numOrders'])
            print("\n")

            customer = input("Enter the ID number of the Customer: ")
            print("\n")
            mycursor.execute('SELECT * FROM Invoice WHERE CustomerID = ' + customer + ' and isDeleted is NULL')
            records = mycursor.fetchall()

            if records == []:
                print("\n")
                print("There is no data that matches your filter.")
                return
            else:
                print("\n")
                print("INVOICE:")
                df = DataFrame(records,
                               columns=['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID',
                                        'isDeleted'])
                print(df.loc[:, 'ID':'CustomerID'])
                print("\n")
                return

    else:
        print("Invalid Input. Please try again.")

def createData(choice):
    if choice == "1":
        theName = input("Name: ")
        theWeight = input("Weight: ")

        print("SUPPLIERS:")
        mycursor.execute('SELECT * FROM Supplier WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Email', 'Country', 'isDeleted', 'Name'])
        newDF = df[['ID', 'Name', 'Email', 'Country']]
        print(newDF)
        print("\n")

        theSupplier = input("ID of the Supplier: ")

        mycursor.execute("SELECT * FROM Supplier WHERE isDeleted is NULL")
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("SUPPLIERS:")
            mycursor.execute('SELECT * FROM Supplier WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Email', 'Country', 'isDeleted', 'Name'])
            newDF = df[['ID', 'Name', 'Email', 'Country']]
            print(newDF)
            print("\n")
            theSupplier = input("ID of the Supplier: ")

        mycursor.execute("INSERT INTO Part(Name, Weight, SupplierID) VALUES(%s, %s, %s)", (theName, theWeight, theSupplier))
        db.commit()
        print("Successfully Added.")

    if choice == "2":
        theName = input("Name: ")
        theEmail = input("Email: ")
        theCountry = input("Country: ")

        mycursor.execute("INSERT INTO Supplier(Name, Email, Country) VALUES(%s, %s, %s)", (theName,theEmail, theCountry))
        db.commit()
        print("Successfully Added.")

    if choice == "3":
        theName = input("Name: ")
        theEmail = input("Email: ")
        while True:
            thePhone = input("Phone Number: ")
            pCount = 0
            for l in thePhone:
                pCount += 1
                if pCount > 11:
                    print("Invalid Input. PLease use up to 11 digits. Try Again")
                    break
            if pCount <= 11:
                break

        theAddress = input("Address: ")

        mycursor.execute("INSERT INTO Customer(Name, Email, PhoneNumber, Address, numOrders) VALUES(%s, %s, %s, %s, %s)", (theName,theEmail,thePhone,theAddress,0))
        db.commit()
        print("Successfully Added.")

    if choice == "4":
        theName = input("Name: ")
        theEmail = input("Email: ")

        mycursor.execute("INSERT INTO Employee(Name, Email) VALUES(%s, %s)", (theName, theEmail))
        db.commit()
        print("Successfully Added.")

    if choice == "5":
        print("PARTS:")
        mycursor.execute('SELECT * FROM Part WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
        print(df.loc[:, 'ID':'SupplierID'])
        print("\n")

        thePart = input("Part ID of Order: ")
        mycursor.execute('SELECT * FROM Part WHERE ID = ' + thePart + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("PARTS:")
            mycursor.execute('SELECT * FROM Part WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
            print(df.loc[:, 'ID':'SupplierID'])
            print("\n")
            thePart = input("Part ID of Order: ")

        theCount = input("Order Amount: ")

        print("EMPLOYEE:")
        mycursor.execute('SELECT * FROM Employee WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Name', 'Email', 'isDeleted'])
        print(df.loc[:, 'ID':'Email'])
        print("\n")

        theEmployee = input("ID of the Employee who took order: ")
        mycursor.execute('SELECT * FROM Employee WHERE ID = ' + theEmployee + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("EMPLOYEE:")
            mycursor.execute('SELECT * FROM Employee WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Email', 'isDeleted'])
            print(df.loc[:, 'ID':'Email'])
            print("\n")
            theEmployee = input("ID of the Employee who took order: ")

        print("CUSTOMERS:")
        mycursor.execute('SELECT * FROM Customer WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
        print(df.loc[:, 'ID':'numOrders'])
        print("\n")

        theCustomer = input("ID of the Customer who made the order: ")
        mycursor.execute('SELECT * FROM Customer WHERE ID = ' + theCustomer + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("CUSTOMERS:")
            mycursor.execute('SELECT * FROM Customer WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
            print(df.loc[:, 'ID':'numOrders'])
            print("\n")
            theCustomer = input("ID of the Customer who made the order: ")

        mycursor.execute("INSERT INTO Invoice(PartID, Count, Date, Fulfilled, EmployeeID, CustomerID) VALUES(%s,%s,%s,%s,%s,%s)", (thePart,theCount,str(datetime.date.today()),0,theEmployee,theCustomer))
        db.commit()
        print("Successfully Added.")









