# ---------------------------------------------------------------------------------------------------------------------#
# Title: Main Module
# Description: A module for testing
# Change Log: (Who, When, What)
# LValderrama, 8.30.2021, created Main Module
# LValderrama, 8.28.2021, added imported processing and IO modules, while loop.
# ---------------------------------------------------------------------------------------------------------------------#

# Objective:
# 1. The Main.py script is designed to:
#       a. Present a menu of choices for the user to select from.
#       b. Execute the program based on the choice made by the user.
#       c. Use Try/Catch Error Handling.
#       d. Use Class objects.
#       e. Work with other modules

# Pseudo-Code:
# Data --------------------------------------------------------------------------------------------------------------- #
# Step 1: Declare variables

strChoice = ""  # Captures the user option selection
strFileName = 'EmployeeProjectHours.csv'  # The name of the data file
lstTable = []  # A list that acts as a 'table' of rows

# Step 2: Import Module ---------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("There was an error while importing the scripts")

# Main Body of Script  ----------------------------------------------------------------------------------------------- #
# Step 3: Load data from file into a list of employee objects when script starts ------------------------------------- #

lstFileData = Fp.read_data_from_file(strFileName)
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2], line[3], line[4], line[5].strip()))

# Step 4: Calling the functions from DataClasses, IOClasses, ProcessingClasses --------------------------------------- #
while True:
    try:
        # Show user a menu of options -------------------------------------------------------------------------------- #
        Eio.print_menu_items()

        # Get user's menu option choice ------------------------------------------------------------------------------ #
        strChoice = Eio.input_menu_options()

        # Show user current data in the list of employee objects ----------------------------------------------------- #
        if strChoice == '1':
            Eio.print_current_list_items(lstTable)
            continue

        # Let user add data to the list of employee objects ---------------------------------------------------------- #
        elif strChoice == '2':
            newEmployee = Eio.input_employee_data()
            lstTable.append(newEmployee)
            Eio.print_current_list_items(lstTable)
            continue

        # Let user save current data to file ------------------------------------------------------------------------- #
        elif strChoice == '3':
            print('\n Would you like to save your data?')
            strSaveToFileInput = input("Enter 'y' or 'n': ")
            if strSaveToFileInput == 'n':
                print('Data not saved!')
            if strSaveToFileInput == 'y':
                Fp.save_data_to_file(strFileName, lstTable)
                print('\nYour data is saved to', strFileName)
            continue

        # Let user exit program -------------------------------------------------------------------------------------- #
        elif strChoice == '4':
            print("Goodbye!")
            EndProgram = input('\n(Press Enter to End Program)')
            break
        else:
            print('\nInvalid entry. Please enter a number from 1 to 4')
    except ValueError:
        print('\nInvalid entry. Please enter a number from 1 to 4')
