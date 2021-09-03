# -------------------------------------------------------------------------------------------------------------------- #
# Title: IO Classes
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# LValderrama, 8.30.2021, created File
# -------------------------------------------------------------------------------------------------------------------- #


if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
else:
    import DataClasses as DC


class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items():

        input_menu_options():

        print_current_list_items(list_of_rows):

        input_employee_data():

        remove_employee_from_list():

        input_press_to_continue():

    changelog: (When,Who,What)
        LValderrama,8.30.2021,Created Class:
    """

    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options
        1) Show current employee data
        2) Add new employee data
        3) Remove employee data
        4) Save employee data to File
        5) Exit program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        print("******* The current items employees are: *******")
        for row in list_of_rows:
            print(
                str(row.employee_id) + ", " + row.first_name + " " + row.last_name + ", " + row.project_name + ", " +
                row.full_date + ", " + str(row.hours_worked))
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_employee_data():
        """ Gets data for a employee object

        :return: (employee) object with input data
        """
        global emp
        try:
            employee_id = (input("What is the employee Id? - ").strip())
            first_name = str(input("What is the employee First Name? - ").strip())
            last_name = str(input("What is the employee Last Name? - ").strip())
            project_name = str(input("What is the Project Name? - ").strip())
            full_date = str(input("What is the date? - ").strip())
            hours_worked = str(input("What is the Number of Hours Worked? - ").strip())
            print()  # Add an extra line for looks
            emp = DC.Employee(employee_id, first_name, last_name, project_name, full_date, hours_worked)
        except Exception as e:
            print(e)
        return emp

    @staticmethod
    def remove_employee_from_list():
        """ Removes employees from list

                :return" employee removed
        """
        # global emp
        remove_employee = input("Enter the employee ID of the employee you would like to remove - ")
        return remove_employee

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press [Enter] to continue')
