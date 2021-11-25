import controller
from view import View
from view import Menu
# from menu import Menu


connection = controller.connection()
cursor = connection.cursor()
Menu.menu()
cursor.close()
connection.close()
print("PostgreSQL connection is closed")
