import sqlite3

db_name = "customer.db"

def connect_to_db():
    db_conn = sqlite3.connect(db_name)
    db_cursor = db_conn.cursor()
    print("Conneceted to DB.")
    return db_conn, db_cursor

def drop_table(db_cursor):
    sql = "drop table if exists customer"
    db_cursor.execute(sql)

def create_table(db_cursor):
    sql = "create table customer(customer_id nt, customer_name text, postal_code int, address text, city text, country text)"
    db_cursor.execute(sql)
    print("Created table.")
def select_all(db_cursor):
    sql = "select * from customer"
    result_set = db_cursor.execute(sql)
    print("\ntable has the following rows:")
    print("CustomerID, Customer Name, postalcode, address, city, country")
    for row in result_set:
        print(row)
    print()

def insert_row(db_cursor):
    sql = "insert into customer values(?, ?, ?, ?, ?, ?)"
    customer_id = int(input("Enter the customer number (int)\n>"))
    customer_name = input("Enter the customer name\n>")
    postal_code = int(input("Enter the customer postal code\n>"))
    address = input("Enter the customer address\n>")
    city = input("Enter the customer city\n>")
    country = input("Enter customer country\n>")
    tuple_of_values = (customer_id, customer_name, postal_code, address, city, country)
    db_cursor.execute(sql, tuple_of_values)
    print("inserted row into table")

def select_row(db_cursor):
    sql = "select * from customer where customerid = ?"
    custid = int(input("Enter the customer id that you want to find\n>"))
    tuple_of_value = (custid, )

    results_set = db.cursor.execute(sql, tuple_of_value)
    print("\nHere are your results:")
    for row in result_set:
        print(row)
    print()

def update_row(db_cursor):
    sql = "update customer set customer_name = ?, address =?, where customer_id = ?"
    custid = int(input("Enter the customer id (int) that you wish to update:\n>"))
    custname = input("Enter the new customer name\n>")
    address = input("Enter new address\n>")
    tuple_of_values = (custname, address, custid)
    db_cursor.execute(sql, tuple_of_values)
    print("Row updated")

def delete_row(db_cursor):
    sql = "delete customer where customerid = ?"
    custid = int(input("Enter the customer id that you wish to delete\n>"))
    tuple_of_values = (custid, )
    db_cursor.execute(sql, tuple_of_values)
    print(f"Row with {custid} deleted")

def display_menu(db_conn, db_cursor):
    print("Welcome to my database program")
    print("Menu:")
    while True:
        print("Menu:")
        print("Enter S to get started and create a new database")
        print("Enter C to create a new row")
        print("Enter R to retrieve data")
        print("Enter U to update a row")
        print("Enter D to delete a row")
        print("Enter Q to quit the program")
        choice = input("Enter your choice\n>").upper()
        if choice == "S":
            drop_table(db_cursor)
            create_table(db_cursor)
        elif choice == "C":
            insert_row(db_cursor)
        elif choice == "R":
            select_row(db_cursor)
        elif choice == "U":
            update_row(db_cursor)
        elif choice == "D":
            delete_row(db_cursor)
        elif choice == "Q":
            print("goodbye")
            break
        else:
            print("invalid")
        db_conn.commit()
        select_all(db_cursor)


def main():
    db_conn, db_cursor = connect_to_db()
    display_menu(db_conn, db_cursor)
    db_conn.close()

main()
