
import pandas as pd
import mysql.connector
from pandas import DataFrame
import datetime
import csv

#connect to database with my specific login information
db = mysql.connector.connect(
    host="34.94.182.22",
    user="aanguiano@chapman.edu",
    passwd="FooBar!@#$",
    database="aanguiano_db2"
)

pd.set_option('display.max_columns', None)
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
        mycursor.execute('SELECT Country FROM Supplier WHERE isDeleted is NULL GROUP BY Country')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['Country'])
        print(df)
        print("\n")
        #country = input("Country ID you would like to filter by (number): ")
        #mycursor.execute('SELECT * FROM Supplier WHERE Country = ' + country + ' and isDeleted is NULL')
        country = input("Country to filter by: ")
        mycursor.execute("SELECT * FROM Supplier WHERE Country = '" + country + "' and isDeleted is NULL")

        records = mycursor.fetchall()
        if records == []:
            print("\n")
            print("Invalid Input. Please Try Again.")
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

def editData(choice):
    if choice == "1":
        print("PARTS:")
        mycursor.execute('SELECT * FROM Part WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
        print(df.loc[:, 'ID':'SupplierID'])
        print("\n")

        IDChange = input("ID of Part to edit: ")
        mycursor.execute('SELECT * FROM Part WHERE ID = ' + IDChange + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("PARTS:")
            mycursor.execute('SELECT * FROM Part WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
            print(df.loc[:, 'ID':'SupplierID'])
            print("\n")
            IDChange = input("ID of Part to edit: ")

        print("Options to edit: ")
        print("1. Name")
        print("2. Weight")
        print("3. Supplier")
        change = input("Enter the number of the option you would like to execute: ")

        if change == "1":
            newName = input("New name: ")
            mycursor.execute("UPDATE Part SET Name = %s WHERE ID = %s", (newName, IDChange))
            db.commit()
            print("Successfully Updated")
        elif change == "2":
            try:
                newWeight = int(input("New weight: "))
            except ValueError:
                print("Try again with only digits")
                newWeight = input("New weight: ")
            mycursor.execute("UPDATE Part SET Weight = %s WHERE ID = %s", (newWeight, IDChange))
            db.commit()
            print("Successfully Updated")

        elif change == "3":
            print("")
            print("SUPPLIERS:")
            mycursor.execute('SELECT * FROM Supplier WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Email', 'Country', 'isDeleted', 'Name'])
            newDF = df[['ID', 'Name', 'Email', 'Country']]
            print(newDF)
            print("\n")

            theSupplier = input("ID of the new Supplier: ")
            mycursor.execute("SELECT * FROM Supplier WHERE ID = " + theSupplier + " and isDeleted is NULL")
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
                theSupplier = input("ID of the new Supplier: ")

            mycursor.execute("UPDATE Part SET SupplierID = %s WHERE ID = %s", (theSupplier, IDChange))
            db.commit()
            print("Successfully Updated")
        else:
            print("Invalid Input. Try Again")

    if choice == "2":
        print("SUPPLIERS:")
        mycursor.execute('SELECT * FROM Supplier WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Email', 'Country', 'isDeleted', 'Name'])
        newDF = df[['ID', 'Name', 'Email', 'Country']]
        print(newDF)
        print("\n")

        IDChange = input("ID of the Supplier to change: ")
        mycursor.execute("SELECT * FROM Supplier WHERE ID = " + IDChange + " and isDeleted is NULL")
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
            IDChange = input("ID of the Supplier to change: ")

        print("Options to edit: ")
        print("1. Name")
        print("2. Email")
        print("3. Country")
        change = input("Enter the number of the option you would like to execute: ")

        if change == "1":
            newName = input("New name: ")
            mycursor.execute("UPDATE Supplier SET Name = %s WHERE ID = %s", (newName, IDChange))
            db.commit()
            print("Successfully Updated")
        elif change == "2":
            newEmail = input("New email: ")
            mycursor.execute("UPDATE Supplier SET Email = %s WHERE ID = %s", (newEmail, IDChange))
            db.commit()
            print("Successfully Updated")
        elif change == "3":
            newCountry = input("New country: ")
            mycursor.execute("UPDATE Supplier SET Country = %s WHERE ID = %s", (newCountry, IDChange))
            db.commit()
            print("Successfully Updated")
        else:
            print("Invalid Input. Try Again")

    elif choice == "3":
        print("CUSTOMERS:")
        mycursor.execute('SELECT * FROM Customer WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
        print(df.loc[:, 'ID':'numOrders'])
        print("\n")

        IDChange = input("ID of the Customer to change: ")
        mycursor.execute('SELECT * FROM Customer WHERE ID = ' + IDChange + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("CUSTOMERS:")
            mycursor.execute('SELECT * FROM Customer WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
            print(df.loc[:, 'ID':'numOrders'])
            print("\n")
            IDChange = input("ID of the Customer to change: ")

        print("Options to edit: ")
        print("1. Name")
        print("2. Email")
        print("3. Phone Number")
        print("4. Address")
        print("5. numOrders")
        change = input("Enter the number of the option you would like to execute: ")

        if change == "1":
            newName = input("New name: ")
            mycursor.execute("UPDATE Customer SET Name = %s WHERE ID = %s", (newName, IDChange))
            db.commit()
            print("Successfully Updated")

        elif change == "2":
            newEmail = input("New email: ")
            mycursor.execute("UPDATE Customer SET Email = %s WHERE ID = %s", (newEmail, IDChange))
            db.commit()
            print("Successfully Updated")

        elif change == "3":
            newPhone = input("New Phone Number: ")
            while True:
                newPhone = input("New Phone Number: ")
                pCount = 0
                for l in newPhone:
                    pCount += 1
                    if pCount > 11:
                        print("Invalid Input. PLease use up to 11 digits. Try Again")
                        break
                if pCount <= 11:
                    break

            mycursor.execute("UPDATE Customer SET PhoneNumber = %s WHERE ID = %s", (newPhone, IDChange))
            db.commit()
            print("Successfully Updated")

        elif change == "4":
            newAddress = input("New Address: ")
            mycursor.execute("UPDATE Customer SET Address = %s WHERE ID = %s", (newAddress, IDChange))
            db.commit()
            print("Successfully Updated")

        elif change == "5":
            newNumOrders = input("New number of orders: ")
            mycursor.execute("UPDATE Customer SET numOrders = %s WHERE ID = %s", (newNumOrders, IDChange))
            db.commit()
            print("Successfully Updated")

        else:
            print("Invalid Input. Please try again.")

    elif choice == "4":
        print("EMPLOYEES:")
        mycursor.execute('SELECT * FROM Employee WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Name', 'Email', 'isDeleted'])
        print(df.loc[:, 'ID':'Email'])
        print("\n")

        IDChange = input("ID of the Employee to change: ")
        mycursor.execute('SELECT * FROM Employee WHERE ID = ' + IDChange + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("EMPLOYEE:")
            mycursor.execute('SELECT * FROM Employee WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Email', 'isDeleted'])
            print(df.loc[:, 'ID':'Email'])
            print("\n")
            IDChange = input("ID of the Employee to change: ")

        print("Options to edit: ")
        print("1. Name")
        print("2. Email")
        change = input("Enter the number of the option you would like to execute: ")

        if change == "1":
            newName = input("New name: ")
            mycursor.execute("UPDATE Employee SET Name = %s WHERE ID = %s", (newName, IDChange))
            db.commit()
            print("Successfully Updated")

        elif change == "2":
            newEmail = input("New email: ")
            mycursor.execute("UPDATE Employee SET Email = %s WHERE ID = %s", (newEmail, IDChange))
            db.commit()
            print("Successfully Updated")

    elif choice == "5":
        print("INVOICE:")
        mycursor.execute('SELECT * FROM Invoice WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records,
                       columns=['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID', 'isDeleted'])
        print(df.loc[:, 'ID':'CustomerID'])
        print("\n")

        IDChange = input("ID of the Invoice to change: ")
        mycursor.execute('SELECT * FROM Invoice WHERE ID = ' + IDChange + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("INVOICE:")
            mycursor.execute('SELECT * FROM Invoice WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records,
                           columns=['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID',
                                    'isDeleted'])
            print(df.loc[:, 'ID':'CustomerID'])
            print("\n")
            IDChange = input("ID of the Invoice to change: ")

        print("Options to edit: ")
        print("1. Part Ordered")
        print("2. Count of Order")
        print("3. Fulfillment")
        print("4. Customer")
        change = input("Enter the number of the option you would like to execute: ")

        if change == "1":
            print("PARTS:")
            mycursor.execute('SELECT * FROM Part WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
            print(df.loc[:, 'ID':'SupplierID'])
            print("\n")

            newIDPart = input("New Part ID of Order: ")
            mycursor.execute('SELECT * FROM Part WHERE ID = ' + newIDPart + ' and isDeleted is NULL')
            if mycursor.fetchall() == []:
                print("Invalid ID. Try Again.")
                print("\n")
                print("PARTS:")
                mycursor.execute('SELECT * FROM Part WHERE isDeleted is NULL')
                records = mycursor.fetchall()
                df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
                print(df.loc[:, 'ID':'SupplierID'])
                print("\n")
                newIDPart = input("New Part ID of Order: ")

            mycursor.execute("UPDATE Invoice SET PartID = %s WHERE ID = %s", (newIDPart, IDChange))
            db.commit()
            print("Successfully Updated")

        elif change == "2":
            newCount = input("New Count of the order: ")
            mycursor.execute("UPDATE Invoice SET Count = %s WHERE ID = %s", (newCount, IDChange))
            db.commit()
            print("Successfully Updated")

        elif change == "3":
            while True:
                ifFul = input("Is this order fulfilled(f) or not fulfilled(nf)")
                if ifFul == "f":
                    mycursor.execute("UPDATE Invoice SET Fulfilled = %s WHERE ID = %s", (1, IDChange))
                    db.commit()
                    print("Successfully Updated")
                    break
                elif ifFul == "nf":
                    mycursor.execute("UPDATE Invoice SET Fulfilled = %s WHERE ID = %s", (0, IDChange))
                    db.commit()
                    print("Successfully Updated")
                    break
                else:
                    print("Invalid input. Try Again.")

        elif change == "4":
            print("CUSTOMERS:")
            mycursor.execute('SELECT * FROM Customer WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
            print(df.loc[:, 'ID':'numOrders'])
            print("\n")

            newIDCust = input("ID of the new Customer: ")
            mycursor.execute('SELECT * FROM Customer WHERE ID = ' + newIDCust + ' and isDeleted is NULL')
            if mycursor.fetchall() == []:
                print("Invalid ID. Try Again.")
                print("\n")
                print("CUSTOMERS:")
                mycursor.execute('SELECT * FROM Customer WHERE isDeleted is NULL')
                records = mycursor.fetchall()
                df = DataFrame(records,
                               columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
                print(df.loc[:, 'ID':'numOrders'])
                print("\n")
                newIDCust = input("ID of the new Customer: ")

            mycursor.execute("UPDATE Invoice SET Customer = %s WHERE ID = %s", (newIDCust, IDChange))
            db.commit()
            print("Successfully Updated")

    else:
        print("Invalid Input. Try Again.")

def deleteData(choice):
    if choice == "1":
        print("PARTS:")
        mycursor.execute('SELECT * FROM Part WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
        print(df.loc[:, 'ID':'SupplierID'])
        print("\n")

        IDDelete = input("ID of Part to delete: ")
        mycursor.execute('SELECT * FROM Part WHERE ID = ' + IDDelete + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("PARTS:")
            mycursor.execute('SELECT * FROM Part WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Weight', 'SupplierID', 'isDeleted'])
            print(df.loc[:, 'ID':'SupplierID'])
            print("\n")
            IDDelete = input("ID of Part to edit: ")

        mycursor.execute("UPDATE Part SET isDeleted = %s WHERE ID = %s", (1, IDDelete))
        db.commit()
        print("Successfully Deleted")

    elif choice == "2":
        print("SUPPLIERS:")
        mycursor.execute('SELECT * FROM Supplier WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Email', 'Country', 'isDeleted', 'Name'])
        newDF = df[['ID', 'Name', 'Email', 'Country']]
        print(newDF)
        print("\n")

        IDDelete = input("ID of the Supplier to deelete: ")
        mycursor.execute("SELECT * FROM Supplier WHERE ID = " + IDDelete + " and isDeleted is NULL")
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
            IDDelete = input("ID of the Supplier to delete: ")

        mycursor.execute("UPDATE Supplier SET isDeleted = %s WHERE ID = %s", (1, IDDelete))
        db.commit()
        print("Successfully Deleted")

    elif choice == "3":
        print("CUSTOMERS:")
        mycursor.execute('SELECT * FROM Customer WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
        print(df.loc[:, 'ID':'numOrders'])
        print("\n")

        IDDelete = input("ID of the Customer to delete: ")
        mycursor.execute('SELECT * FROM Customer WHERE ID = ' + IDDelete + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("CUSTOMERS:")
            mycursor.execute('SELECT * FROM Customer WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Email', 'PhoneNumber', 'Address', 'numOrders', 'isDeleted'])
            print(df.loc[:, 'ID':'numOrders'])
            print("\n")
            IDDelete = input("ID of the Customer to delete: ")

        mycursor.execute("UPDATE Customer SET isDeleted = %s WHERE ID = %s", (1, IDDelete))
        db.commit()
        print("Successfully Deleted")

    elif choice == "4":
        print("EMPLOYEES:")
        mycursor.execute('SELECT * FROM Employee WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['ID', 'Name', 'Email', 'isDeleted'])
        print(df.loc[:, 'ID':'Email'])
        print("\n")

        IDDelete = input("ID of the Employee to change: ")
        mycursor.execute('SELECT * FROM Employee WHERE ID = ' + IDDelete + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("EMPLOYEE:")
            mycursor.execute('SELECT * FROM Employee WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records, columns=['ID', 'Name', 'Email', 'isDeleted'])
            print(df.loc[:, 'ID':'Email'])
            print("\n")
            IDDelete = input("ID of the Employee to change: ")

        mycursor.execute("UPDATE Employee SET isDeleted = %s WHERE ID = %s", (1, IDDelete))
        db.commit()
        print("Successfully Deleted")

    elif choice == "5":
        print("INVOICE:")
        mycursor.execute('SELECT * FROM Invoice WHERE isDeleted is NULL')
        records = mycursor.fetchall()
        df = DataFrame(records,
                       columns=['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID', 'isDeleted'])
        print(df.loc[:, 'ID':'CustomerID'])
        print("\n")

        IDDelete = input("ID of the Invoice to delete: ")
        mycursor.execute('SELECT * FROM Invoice WHERE ID = ' + IDDelete + ' and isDeleted is NULL')
        if mycursor.fetchall() == []:
            print("Invalid ID. Try Again.")
            print("\n")
            print("INVOICE:")
            mycursor.execute('SELECT * FROM Invoice WHERE isDeleted is NULL')
            records = mycursor.fetchall()
            df = DataFrame(records,
                           columns=['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID',
                                    'isDeleted'])
            print(df.loc[:, 'ID':'CustomerID'])
            print("\n")
            IDDelete = input("ID of the Invoice to delete: ")

        mycursor.execute("UPDATE Invoice SET isDeleted = %s WHERE ID = %s", (1, IDDelete))
        db.commit()
        print("Successfully Deleted")

    else:
        print("Invalid Input. Try Again.")

def generateReports(choice):
    if choice == "1":
        fileName = "unfulfilledOrders.csv"
        mycursor.execute('SELECT ID,PartID, Count, Date, Fulfilled,EmployeeID, CustomerID FROM Invoice WHERE Fulfilled = 0 and isDeleted is NULL')
        records = mycursor.fetchall()

        file = open(fileName, "w")
        add = csv.writer(file)

        # adds the title row of all variables in datasheet
        add.writerow(['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID'])
        for rec in records:
            add.writerow([rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]])

        print("Successfully exported as 'unfulfilledOrders.csv'")
        print("\n")

    elif choice == "2":
        fileName = "countryInvoices.csv"
        print("SUPPLIERS:")
        mycursor.execute('SELECT Country FROM Supplier WHERE isDeleted is NULL GROUP BY Country')
        records = mycursor.fetchall()
        df = DataFrame(records, columns=['Country'])
        print(df)
        print("\n")

        country = input("Country to filter by: ")
        mycursor.execute("SELECT * FROM Supplier WHERE Country = '" + country + "' and isDeleted is NULL")

        records = mycursor.fetchall()
        if records == []:
            print("\n")
            print("Invalid Input. Please Try Again.")
            return
        else:
            print("\n")
            mycursor.execute("SELECT Invoice.ID,PartID, Count, Date, Fulfilled,EmployeeID, CustomerID,Country FROM Invoice JOIN Part ON Invoice.PartID = Part.ID JOIN Supplier ON Part.SupplierID = Supplier.ID WHERE Fulfilled = 0 and Invoice.isDeleted is NULL and Supplier.isDeleted is NULL and Part.isDeleted is NULL and Country = '" + country + "'")
            records = mycursor.fetchall()
            file = open(fileName, "w")
            if records == []:
                print("\n")
                print("There are no unfulfilled order from that country.")
                return
            else:
                add = csv.writer(file)

                # adds the title row of all variables in datasheet
                add.writerow(['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID','Part Origin'])
                for rec in records:
                    add.writerow([rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7]])

                print("Successfully exported as 'countryInvoices.csv'")
                return
    else:
        print("Invalid Input. Try Again.")



