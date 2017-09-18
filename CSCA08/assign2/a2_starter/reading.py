# Functions for reading tables and databases

import glob
from database import *


# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING
# Write the read_table and read_database functions below
def read_table(file_name):
    ''' (str) -> Table

    The function will receive a parameter which is a file's name.
    The function will build and return an object based on the input file.
    The first line in the file should be the title in the Table, and
    other lines should the value in the dictionary.

    REQ: file_name must end with 'csv.'
    '''
    # create an object of Table
    table = Table()
    # read the file, read lines and finally close it
    filehandle = open(file_name, 'r')
    first_line = filehandle.readline()
    lines = filehandle.readlines()
    filehandle.close()
    # clean the all the lines by str method -- strip and split
    first_line = first_line.strip('\n').split(',')
    data = []
    for line in lines:
        data.append(line.strip('\n').split(','))
    # store all content in a list by calling the method in Table
    # pass two lists with cleaned data to the class method
    table_list = table.store_table_list(first_line, data)
    # loop through element in table_list, which include titles and infos
    for element in table_list:
        # use method in Table to add the table into a dict
        table.add_new_row(element[0], element[1:])
    return table


def read_database():
    ''' () -> Database

    The function will read all the files inder the same direction.
    For each file it read, the function will create an object of Table
    and store all the tables into an object of Database.
    The function will finally return database.
    '''
    # create an object of Database
    database = Database()
    # get all the file in a list
    file_list = glob.glob('*.csv')
    # create a empty list to store tables
    tables = []
    # loop through each file name to get the objects of Table
    index = 0
    while index < len(file_list):
        tables.append(read_table(file_list[index]))
        index += 1
    # add all the tables into database
    database.add_new_table(file_list, tables)
    return database
