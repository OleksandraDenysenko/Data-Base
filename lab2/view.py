import controller
from model import Model
import pandas as pd


class View:
    def __init__(self, table, records):
        self.table = table
        self.records = records

    @staticmethod
    def enter_item(item):
        data = input("Enter {}: ".format(item))
        return data

    @staticmethod
    def list():
        print('''
        1 -> subject
        2 -> teacher
        3 -> student
        4 -> phone
        5 -> schedule
        ''')

    @staticmethod
    def columns(table):
        if table == 1:
            print('''
                1 -> name
            ''')
        elif table == 2:
            print('''
                1 -> firstname
                2 -> lastname
            ''')
        elif table == 3:
            print('''
                1 -> firstname
                2 -> lastname
            ''')
        elif table == 4:
            print('''
                1 -> phone number
                2 -> student ID
            ''')
        elif table == 5:
            print('''
                1 -> day
                2 -> time
                3 -> subject ID
                4 -> student ID
                5 -> teacher Id
            ''')

    def show_table(self):
        print("____________________")
        if self.table == 1:
            print("Table 'Subject'")
            print("____________________")
            for row in self.records:
                print("ID = ", row[0])
                print("Name = ", row[1])
                print("____________________")
        elif self.table == 2:
            print("Table 'Teacher'")
            print("____________________")
            for row in self.records:
                print("ID = ", row[0])
                print("First name = ", row[1])
                print("Last name = ", row[2])
                print("____________________")
        elif self.table == 3:
            print("Table 'Student'")
            print("____________________")
            for row in self.records:
                print("ID = ", row[0])
                print("First name = ", row[1])
                print("Last name = ", row[2])
                print("____________________")
        elif self.table == 4:
            print("Table 'Phone'")
            print("____________________")
            for row in self.records:
                print("ID = ", row[0])
                print("Phone = ", row[1])
                print("Student with this phone = ", row[2])
                print("____________________")
        elif self.table == 5:
            print("Table 'Schedule'")
            print("____________________")
            for row in self.records:
                print("ID = ", row[0])
                print("Day = ", row[1])
                print("Time = ", row[2])
                print("Student ID = ", row[3])
                print("Teacher ID = ", row[4])
                print("Subject ID = ", row[5])
                print("____________________")

    def show_search(self):
        if self.table == 1:
            for row in self.records:
                print("Last name = ", row[0])
                print("First name = ", row[1])
                print("Phone number = ", row[2])
                print("_______________________")
        elif self.table == 2:
            for row in self.records:
                print("Last name = ", row[0])
                print("Subject = ", row[1])
                print("First name of the teacher = ", row[2])
                print("Last name of the teacher = ", row[3])
                print("_______________________")
        elif self.table == 3:
            for row in self.records:
                print("Subject = ", row[0])
                print("Last name of the student = ", row[1])
                print("Day of subject = ", row[2])
                print("Time of subject = ", row[3])
                print("_______________________")

    @staticmethod
    def search():
        print('''
                1 -> Search first name and phone number of the student with last name
                2 -> Search subject and teacher first and last name of the student with last name
                3 -> Search student last name, day and time of the subject with subject name
                ''')


class Menu:
    @staticmethod
    def menu():
        while True:
            print('''
                    Main menu
                    0 - Show one table
                    1 - Show all tables
                    2 - Insert data
                    3 - Delete data
                    4 - Update data
                    5 - Search data
                    6 - Insert random data
                    7 - Exit
                    ''')
            choice = input('Choose an option: ')
            if choice == '0':
                list()
                table_num = controller.validtable()
            elif choice == '1':
                Model.show_all()
            elif choice == '2':
                end_insert = False
                while not end_insert:
                    Model.insert()
                    incorrect = True
                    while incorrect:
                        answer = input('Continue working with insert? Enter Yes or No ')
                        if answer == 'No':
                            end_insert = True
                            incorrect = False
                        elif answer == 'Yes':
                            incorrect = False
                            pass
                        else:
                            print('Please, enter Yes or No')
            elif choice == '3':
                end_delete = False
                while not end_delete:
                    Model.delete()
                    incorrect = True
                    while incorrect:
                        answer = input('Continue working with delete? Enter Yes or No ')
                        if answer == 'No':
                            end_delete = True
                            incorrect = False
                        elif answer == 'Yes':
                            incorrect = False
                            pass
                        else:
                            print('Please, enter Yes or No ')
            elif choice == '4':
                end_update = False
                while not end_update:
                    Model.update()
                    incorrect = True
                    while incorrect:
                        answer = input('Continue working with update? Enter Yes or No ')
                        if answer == 'No':
                            end_update = True
                            incorrect = False
                        elif answer == 'Yes':
                            incorrect = False
                            pass
                        else:
                            print('Please, enter Yes or No ')
            elif choice == '5':
                end_search = False
                while not end_search:
                    Model.search()
                    incorrect = True
                    while incorrect:
                        answer = input('Continue working with search? Enter Yes or No ')
                        if answer == 'No':
                            end_search = True
                            incorrect = False
                        elif answer == 'Yes':
                            incorrect = False
                            pass
                        else:
                            print('Please, enter Yes or No ')
            elif choice == '6':
                end_insert = False
                while not end_insert:
                    Model.random()
                    go_on = True
                    while go_on:
                        answer = input('Continue working with random data? Enter Yes or No: ')
                        if answer == 'No':
                            end_insert = True
                            go_on = False
                        elif answer == 'Yes':
                            go_on = False
                            pass
                        else:
                            print('Please, enter Yes or No ')
            elif choice == '7':
                break
            else:
                print('Please, enter valid number')
