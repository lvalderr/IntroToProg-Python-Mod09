# ---------------------------------------------------------------------------------------------------------------------#
# Title: Test Harness
# Description: A module for testing
# Change Log: (Who, When, What)
# LValderrama, 8.30.2021, Created File
# ---------------------------------------------------------------------------------------------------------------------#


# Test IO classes
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith", "Project A", "01/01/2021", "2")
objP2 = Emp(2, "Sue", "Jones", "Project B", "01/01/2021", "3")
lstTable = [objP1, objP2]
# for row in lstTable:
#     print(row.to_string(), type(row))

# Test processing module
Fp.save_data_to_file("EmployeeProjectHours.csv", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeProjectHours.csv")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2], line[3], line[4], line[5].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())


