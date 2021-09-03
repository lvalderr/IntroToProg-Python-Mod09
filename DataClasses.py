# -------------------------------------------------------------------------------------------------------------------- #
# Title: Data Classes
# Description: A module of data classes
# ChangeLog (Who,When,What):
# LValderrama, 8.30.2021, created File
# -------------------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


class Employee(object):  # Inherits from object
    """Stores data about an Employee:

    properties:
        employee_id: (int) with the employee's ID

        first_name: (string) with the employee's first name

        last_name: (string) with the employee's last name

        project_name: (string) with the name of the project assigned to the employee

        full_date: (string) with the date

        hours_worked: (string) with the hours worked
    methods:
        to_string() returns comma separated product data (alias for __str__())
    changelog: (When,Who,What)
        LValderrama,8.30.2021,Created Class
    """

    def __init__(self, employee_id, first_name, last_name, project_name, full_date, hours_worked):
        # Attributes

        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__project_name = project_name
        self.__full_date = full_date
        self.__hours_worked = hours_worked

    # --Properties--
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        if str(value).isnumeric():
            self.__last_name = value
        else:
            raise Exception("IDs must be numbers")

    @property
    def first_name(self):
        return str(self.__first_name).title()

    @first_name.setter
    def first_name(self, value):
        if not str(value).isnumeric():
            self.__first_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def last_name(self):
        return str(self.__last_name).title()

    @last_name.setter
    def last_name(self, value):
        if not str(value).isnumeric():
            self.__last_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def project_name(self):
        return self.__project_name

    @project_name.setter
    def project_name(self, value):
        if str(value).isalnum():
            self.__project_name = value
        else:
            raise Exception("Projects may or may not be numbers")

    @property
    def full_date(self):
        return self.__full_date

    @full_date.setter
    def full_date(self, value):
        if str(value).isnumeric():
            self.__full_date = value
        else:
            raise Exception("Please present dates as mm/dd/yyyy")

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if float(value):
            self.__hours_worked = value
        else:
            raise Exception("Hours worked must be numbers")

    # --Methods--
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def __str__(self):
        """ Implicitly returns field data """
        return self.__employee_id + ',' + self.first_name + ',' + self.last_name + ',' + self.project_name + ',' + self.full_date + ',' + self.hours_worked
        # --End of Class --
