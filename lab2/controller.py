import psycopg2
from view import View


def connection():
    return psycopg2.connect(
        user="postgres",
        password="1111",
        host="localhost",
        port="5432",
        database="postgres",
    )


def disconnect(connection):
    connection.commit()
    connection.close()


def message(text):
    return print(text)


def validate_table_input():
    while True:
        table = input('Choose table number: ')
        if table.isdigit():
            table = int(table)
            if 0 < table < 6:
                break
            else:
                print('Please, enter number from 1 to 5: ')
        else:
            print('Please, enter number: ')
    return table


def validate_input_items(name):
    if name == "id":
        value = View.enter_item("ID")
        if value.isdecimal():
            return value
        else:
            message("enter only number")
            validate_input_items("id")
    elif name == "name":
        value = View.enter_item("name")
        if value.isalpha() is False:
            return validate_input_items(name)
        return value
    elif name == "firstname":
        value = View.enter_item("First Name")
        if value.isalpha() is False:
            return validate_input_items(name)
        return value
    elif name == "lastname":
        value = View.enter_item("Last Name")
        if value.isalpha() is False:
            return validate_input_items(name)
        return value
    elif name == "phonenumber":
        value = View.enter_item("phone number")
        if value.isdigit() is False:
            print("Enter like in example: 0998889999")
            return validate_input_items(name)
        else:
            if len(value) != 10:
                print("Phone should have 10 numbers")
                return validate_input_items(name)
            return str("+38" + value)
    elif name == "day":
        value = View.enter_item("day")
        if value.isalpha() is False:
            return validate_input_items(name)
        return value
    elif name == "time":
        value = View.enter_item("time")
        li = list(value.split(":"))
        li_hour = li[0]
        li_min = li[1]
        if li_hour.isdecimal() and li_min.isdecimal():
            if 20 > int(li_hour) > 7 and -1 < int(li_min) < 60:
                li = [li_hour, li_min]
                return ':'.join(li)
            else:
                message("Please, enter hours from 7 to 20 and minutes from 0 to 59")
                return validate_input_items(name)
        else:
            message("Please, enter only digits with : between")


def validtable():
    incorrect = True
    while incorrect:
        table = input('Choose table number => ')
        if table.isdigit():
            table = int(table)
            if 1 <= table <= 5:
                incorrect = False
            else:
                print('Incorrect input, try again.')
        else:
            print('Incorrect input, try again.')
    return table

