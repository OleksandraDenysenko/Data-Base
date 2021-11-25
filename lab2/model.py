import controller
import time
from view import View

tables = {
    1: 'subject',
    2: 'teacher',
    3: 'student',
    4: 'phone',
    5: 'schedule',
}


class Model:
    @staticmethod
    def show_all():
        connection = controller.connection()
        cursor = connection.cursor()
        for i in range(1, 6):
            table_name = '''"''' + tables[i] + '''"'''
            print(tables[i])
            show_all = 'select * from public.{}'.format(table_name)
            print("Request: ", show_all)
            print('')
            cursor.execute(show_all)
            records = cursor.fetchall()
            object = View(i, records)
            object.show_table()
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def show_table():
        View.list()
        connection = controller.connection()
        cursor = connection.cursor()
        table = '"' + controller.validtable() + '"'
        print(f"Request: SELECT * FROM {table}")
        cursor.execute("""SELECT * from public.{}""".format(table))
        records = cursor.fetchall()
        return records
