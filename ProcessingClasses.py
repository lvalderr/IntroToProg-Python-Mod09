# -------------------------------------------------------------------------------------------------------------------- #
# Title: Processing Classes
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# LValderrama, 8.24.2021, created File
# LValderrama, 9.03.2021, added option to remove employees from list
# -------------------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

        remove_employee_from_list(remove_employee: str, list_of_rows: list):

    changelog: (When,Who,What)
        LValderrama,8.27.2021,Created Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_rows: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_rows: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_rows:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                row = line.split(",")
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

    @staticmethod
    def remove_employee_from_list(remove_employee: str, list_of_rows: list):
        """Removes row from the list of rows based on user input

                :param remove_employee: (string) employee to remove from list
                :param list_of_rows: (list) of objects data saved to file
                :return: list_of_rows: (list) of objects data saved to filet
                        count_check: indication of if a formerEmployeeID was deleted,
                        status status of the function
                """

        identified = ""
        for row in list_of_rows:
            if row.employee_id.lower() == remove_employee.lower():
                list_of_rows.remove(row)
                break
            else:
                continue
        else:
            identified = "not"
        return list_of_rows, identified, 'Success'
