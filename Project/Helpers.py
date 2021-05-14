
import pandas as pd
import mysql.connector
from pandas import DataFrame

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
    df = DataFrame(records, columns=['ID', 'PartID', 'Count', 'Date', 'Fulfilled', 'EmployeeID', 'CustomerID', 'isDeleted'])
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










