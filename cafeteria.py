import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cafeteria"
)


def Create():
    if conexion.is_connected():
        cursor = conexion.cursor()

        customerName = input("Enter customer name: ")
        productName = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        orderType = input(
            "Enter order type (Regular, Student, Teacher): "
        )

        if orderType == "Student":
            discount = 10
        elif orderType == "Teacher":
            discount = 15
        elif orderType == "Regular":
            discount = 0
        else:
            print("Invalid order type.")
            cursor.close()
        price = float(input("Enter price per product: "))
        total = quantity * price
        total = total - (total * discount / 100)

        query = """
        INSERT INTO pedidos (customerName, productName, quantity, orderType, discount, total)VALUES (%s, %s, %s, %s, %s, %s) """

        values = (
            customerName, productName, quantity,
            orderType, discount, total
        )

        cursor.execute(query, values)
        conexion.commit()

        print("Order registered successfully.")
        print("Discount:", discount, "%")
        print("Total to pay:", round(total, 2))



def Read():
    if conexion.is_connected():
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM pedidos")
        results = cursor.fetchall()

        for order in results:
            print(order)


def Update():
    if conexion.is_connected():
        cursor = conexion.cursor()

        id = int(input("Enter order ID to update: "))

        customerName = input("Enter customer name: ")
        productName = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        orderType = input(
            "Enter order type (Regular, Student, Teacher): "
        )

        if orderType == "Student":
            discount = 10
        elif orderType == "Teacher":
            discount = 15
        elif orderType == "Regular":
            discount = 0
        else:
            print("Invalid order type.")
            cursor.close()
            return

        price = float(input("Enter price per product: "))

        total = quantity * price
        total = total - (total * discount / 100)

        query = """UPDATE pedidos SET customerName = %s, productName = %s,quantity = %s,orderType = %s,discount = %s,total = %s WHERE id = %s """

        values = (
            customerName, productName, quantity,
            orderType, discount, total, id
        )

        cursor.execute(query, values)
        conexion.commit()

        if cursor.rowcount > 0:
            print("Order updated successfully.")
        else:
            print("Order ID not found.")


def Delete():
    if conexion.is_connected():
        cursor = conexion.cursor()
        id = int(input("Enter order ID to delete: "))
        query = "DELETE FROM pedidos WHERE id = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        if cursor.rowcount > 0:
            print("Order deleted successfully.")
        else:
            print("Order ID not found.")


def menu():
    while True:
        print("\n--- CAFETERIA ORDER SYSTEM ---")
        print("1. Create Order")
        print("2. Read Orders")
        print("3. Update Order")
        print("4. Delete Order")
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                Create()
            elif option == 2:
                Read()
            elif option == 3:
                Update()
            elif option == 4:
                Delete()
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")


menu()