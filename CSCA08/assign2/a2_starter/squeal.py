from reading import *
from database import *


# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results
class DatabaseTypeError(Exception):
    '''An error to be raised when input in run_query is not a databse.'''


class QuerySyntaxError(Exception):
    '''An error to be raised when query is not in the correct syntax.'''


class InputTypeError(Exception):
    '''An error to be raised when input parameter does not matching
    excepted.'''


def connect_words(str_list):
    ''' (list of str) -> str

    The function will connect two str in the list togetehr and then return
    a str.

    RAISES: InputTypeError if element in str_list isn't a str

    >>> connect_words(['a', 'b', 'c'])
    'a b c'
    >>> connect_words(['a'])
    'a'
    >>> connect_words(['1', '2', '3'])
    '1 2 3'
    '''
    # initialize the result
    result = ''
    # loop through each str and add them together
    for string in str_list:
        # if string is not str, then raise InputTypeError
        if type(string) != str:
            raise InputTypeError('''all the elements in input list should
            be str type''')
        result = result + string + ' '
    # delete the uneless space
    result = result[:-1]
    return result


def split_comma(string):
    ''' (str) -> list of str

    The function will split ',' in input string and return a list.
    If there is no ',' in the string, then put the str into a list and return
    it.

    RAISES: InputTypeError if input parameter string is not the type of str

    >>> split_comma('CSCA,08')
    ['CSCA', '08']
    >>> split_comma('good morning')
    ['good morning']
    >>> split_comma('CSCA,08, should , be, an, interesting,  course!')
    ['CSCA', '08', ' should ', ' be', ' an', ' interesting', '  course!']
    '''
    # if string is not the type of str, then raise InputTypeError
    if type(string) != str:
        raise InputTypeError('input parameter should be the type of str')
    # when there is a comma in the str, then split in comma
    if ',' in string:
        result = string.split(',')
    # when there isn't a comma, then let result be a list of one str
    else:
        result = [string]
    return result


def can_be_float(string):
    ''' (str) -> bool
    The function will return a boolean which says wheather the input string
    can be converted into float type or not.
    True mean that it can change to float, false means can't.

    REQ: isinstance(string, str) == True

    >>> can_be_float('CSC')
    False
    >>> can_be_float('A08')
    False
    >>> can_be_float('CSCA08!')
    False
    >>> can_be_float('138')
    True
    >>> can_be_float('324.234')
    True
    '''
    # initialize result
    result = True
    # try to convert to a float
    try:
        float(string)
    # if is unpossible, then result will be false
    except:
        result = False
    return result


def finding_operators(database, query):
    ''' (Database, str) -> list of list of str

    The function will find operators in query.
    Two operators are mendatory, which are 'select' and 'from'.
    Another operator optional, which is 'where'.

    REQ: query should have correct syntax

    >>> a = Table()
    >>> b = Table()
    >>> a.set_dict({'a': ['b', 'c']})
    >>> b.set_dict({'d': ['e', 'f'], 'g': ['h', 'i']})
    >>> database = Database()
    >>> database.set_dict({'a': a, 'b': b})

    >>> finding_operators(database, 'select * from a')
    [['a'], ['a']]
    >>> result = finding_operators(database, 'select * from b')
    >>> ('g' in result[0]) and ('d' in result[0])
    True

    >>> result = finding_operators(database, 'select d,g from b')
    >>> ('g' in result[0]) and ('d' in result[0])
    True

    >>> finding_operators(database, 'select d,g from b where a>b,c>d')
    [['d', 'g'], ['b'], ['a>b', 'c>d']]

    >>> finding_operators(database, "select * from a where a>'28'")
    [['a'], ['a'], ["a>'28'"]]

    >>> finding_operators(database, "select * from a where a>' 28'")
    [['a'], ['a'], ["a>' 28'"]]
    '''
    # create a list to store content in query
    operator = []
    # split query by space
    query = query.split()
    # determine whether the token 'where' is in the query
    # if is possible, find its index
    # by the squeal syntax, the index of select and from must be 0 and 2
    found_where = False
    if 'where' in query:
        found_where = True
        where_index = query.index('where')
    # check whether there are only one element between 'select' and 'from'
    else:
        where_index = len(query)
    # if is possible, split the str after select but precede from
    operator.append(split_comma(query[1]))
    # order maybe split in a wrong way
    # check if there is more than one element in from order
    # if no, then return itself
    if where_index-2 == 2:
        from_order = query[3]
    # if yes, then connect the order into a list of one str
    elif where_index-2 > 2:
        from_order = connect_words(query[3:where_index])
    # if is possible, split the str of from_order
    operator.append(split_comma(from_order))
    # when the query has where, then store it into operator
    if found_where:
        # order maybe split in a wrong way
        # check if there is more than one element in where order
        # if no, then return itself
        if len(query)-where_index == 2:
            where_order = query[where_index+1]
        # if yes, then connect the order into a list of one str
        elif len(query)-where_index > 2:
            where_order = connect_words(query[where_index+1:])
        # if is possible, split the str of where_order
        operator.append(split_comma(where_order))
    # if use the shortcut *
    if operator[0] == ['*']:
        # loop through each file in the second order
        for file_name in operator[1]:
            # get the specific table and their title names
            table = database.get_table(file_name)
            operator[0] += table.get_title()
        # clean the '*'
        operator[0] = operator[0][1:]
    return operator


def get_column(database, operator):
    ''' (Database, list of str list) -> Table

    The function will receive the database and operator.
    Based on the operator, we will select specific columns from database.
    Then, the function will return a table.
    If there is only one table in operator[1], then it will only give
    selected columns.
    If there are more than one table, then the function will get a table
    of cartesian product of all the tables, and finally only give selected
    columns.

    REQ: operator must be the form of list of str list

    >>> a = Table()
    >>> b = Table()
    >>> c = Table()
    >>> d = Table()
    >>> e = Table()
    >>> a.set_dict({'CSC': ['A08', 'A67'], 'MAT': ['A31', 'A23']})
    >>> b.set_dict({'c.A08': ['term work', 'term tests', 'final', 'homework']})
    >>> c.set_dict({'c.A67': ['homework', 'midterm', 'final', 'exercise']})
    >>> d.set_dict({'m.A31': ['homework', 'midterm', 'final']})
    >>> e.set_dict({'m.A23': []})
    >>> database = Database()
    >>> database.set_dict({'a': a, 'b': b, 'c': c, 'd': d, 'e': e})
    >>> operator = [['c.A08', 'm.A23'], ['a', 'b', 'c', 'd', 'e']]
    >>> result = get_column(database, operator).get_dict()
    >>> result == {'c.A08': [], 'm.A23': []}
    True

    >>> operator = [['CSC', 'MAT', 'c.A08', 'm.A31'], ['a', 'b', 'd']]
    >>> result = get_column(database, operator)
    >>> result.num_rows()
    24

    >>> operator = [['CSC', 'MAT'], ['a']]
    >>> result = get_column(database, operator)
    >>> result.num_rows()
    2

    >>> operator = [['c.A67', 'MAT', 'c.A08'], ['a', 'b', 'c']]
    >>> result = get_column(database, operator)
    >>> result.num_rows()
    32

    >>> operator = [['c.A67', 'MAT', 'c.A08'], ['a', 'b', 'c'], ["CSC='A08'"]]
    >>> result = get_column(database, operator)
    >>> result.num_rows()
    32

    >>> operator = [['CSC'], ['a', 'b']]
    >>> result = get_column(database, operator)
    >>> result.num_rows()
    8
    '''
    # create a table
    table = Table()
    # create a table_list to store info
    table_list = []
    # when there is only one file in the operator[1]
    if len(operator[1]) == 1:
        # get the table based on the file name in operator[1]
        input_table = database.get_table(operator[1][0])
        # get all the titles in the table
        titles = input_table.get_title()
        # loop through each name in operator[0]
        for column_name in operator[0]:
            # when the column names in operator[0] appear in titles
            # then, get the column
            if column_name in titles:
                table_list.append(input_table.get_column(column_name))
    # when there are more than one file in the operator[1]
    elif len(operator[1]) > 1:
        # calling the function multi_cartisian_product to get the new table
        join_table = multi_cartesian_product(database, operator[1])
        # get all the titles in the table
        titles = join_table.get_title()
        # loop through each name in operator[0]
        for column_name in operator[0]:
            # when the column names in operator[0] appear in titles
            # then, get the column
            if column_name in titles:
                table_list.append(join_table.get_column(column_name))
    # add all the info stored in table_list into the table
    for element in table_list:
        table.add_new_row(element[0], element[1:])
    return table


def run_query(database, query):
    ''' (Database, str) -> Table

    This function is the main function, other functions are helper functions
    which help this function to get it's prupose.
    The function will take a databse and a query as two parameters.
    The function will run the input query on the input database and finally
    return a table based on two given parameters.

    REQ: query should have correct syntax

    RAISES: DatabaseTypeError if the first parameter is not a database
    RAISES: QuerySyntaxError if query has incorrect syntax

    >>> a = Table()
    >>> b = Table()
    >>> c = Table()
    >>> d = Table()
    >>> e = Table()
    >>> a.set_dict({'CSC': ['A08', 'A67'], 'MAT': ['A31', 'A23']})
    >>> b.set_dict({'c.A08': ['term work', 'term tests', 'final', 'homework']})
    >>> c.set_dict({'c.A67': ['homework', 'midterm', 'final', 'exercise']})
    >>> d.set_dict({'m.A31': ['homework', 'midterm', 'final']})
    >>> e.set_dict({'m.A23': []})
    >>> database = Database()
    >>> database.set_dict({'a': a, 'b': b, 'c': c, 'd': d, 'e': e})
    >>> query = 'select * from a,b,c,d'
    >>> result = run_query(database, query)
    >>> result.num_rows()
    96

    >>> query = 'select c.A08 from a,b,c,d'
    >>> result = run_query(database, query)
    >>> 'c.A08' in result.get_dict()
    True

    >>> query = "select * from a,b,c where CSC='A08'"
    >>> result = run_query(database, query)
    >>> result.num_rows()
    16

    >>> query = "select * from a,b,c,d where CSC='A08',MAT>CSC"
    >>> result = run_query(database, query)
    >>> result.num_rows()
    48

    >>> query = "select * from a,b,c,d where CSC='A08',CSC>'A30',m.31='final'"
    >>> result = run_query(database, query)
    >>> result.num_rows()
    0
    >>> len(result.get_title())
    5

    >>> query = "select * from a,b,c,d where c.A08='term work'"
    >>> result = run_query(database, query)
    >>> result.num_rows()
    24
    '''
    # initialize the result table
    result_table = Table()
    # if the first parameter is not a database
    if type(database) != Database:
        raise DatabaseTypeError('Should input a database')
    # if the query does not have tokens
    if not ('select' in query and 'from' in query):
        raise QuerySyntaxError('should enter query with correct syntax')
    # get the operator
    operator = finding_operators(database, query)
    # get the target table
    target_table = get_column(database, operator)
    # if there is no 'where', then just return the column
    if len(operator) == 2:
        # would return the unselected table
        result_table = target_table
    # if there is 'where', then go through all the constraints
    elif len(operator) == 3:
        result_table = process_all_constraints(target_table, operator[2])
    return result_table


def process_one_constraint(target_table, constraint):
    ''' (Table, str) -> Table

    The function will only select table row once based on the input constraint.
    The function will select rows on input table and finally return a selected
    table.

    REQ: constraint should have correct syntax

    >>> a = Table()
    >>> a.set_dict({'a.0': ['a', 'b', 'c'], 'a.1': ['4.2', '4.2', '4.2']})
    >>> constraint = "a.0='a'"
    >>> result = process_one_constraint(a, constraint)
    >>> len(result.get_dict())
    2
    >>> 'a.0' in result.get_dict()
    True
    >>> 'a.1' in result.get_dict()
    True
    >>> 'a' in result.get_dict()['a.0']
    True
    >>> '4.2' in result.get_dict()['a.1']
    True

    >>> constraint = 'a.0=a.1'
    >>> result = process_one_constraint(a, constraint)
    >>> result.num_rows()
    0

    >>> constraint = "a.1>'3'"
    >>> result = process_one_constraint(a, constraint)
    >>> result.num_rows()
    3

    >>> constraint = 'a.0>a.1'
    >>> result = process_one_constraint(a, constraint)
    >>> result_dict = result.get_dict()
    >>> result_dict == {'a.0': ['a', 'b', 'c'], 'a.1': ['4.2', '4.2', '4.2']}
    True

    >>> constraint = 'a.1>a.0'
    >>> result = process_one_constraint(a, constraint)
    >>> result_dict = result.get_dict()
    >>> result_dict == {'a.1': [], 'a.0': []}
    True
    '''
    # get the titles in the input table
    titles = target_table.get_title()
    # initialize the result table
    result = Table()
    # if the operator is '='
    if '=' in constraint:
        rows = equal_compare(target_table, constraint)
    # if the operator is '>'
    elif '>' in constraint:
        rows = greater_compare(target_table, constraint)
    # get the table_list
    table_list = target_table.store_table_list(titles, rows)
    # loop through each element in new_table_list
    # and add titles and data into the result_table
    for element in table_list:
        result.add_new_row(element[0], element[1:])
    return result


def equal_compare(target_table, constraint):
    ''' (Table, str) -> list of str list

    The function will select all the rows which are satasfy the constraint.
    The function will only compare two items with '=' sign.
    The function will return a list of str list which contains all the rows
    that satasfy the constraint.

    REQ: '=' in constraint

    >>> a = Table()
    >>> a.set_dict({'a.0': ['a', 'b', 'c'], 'a.1': ['4.2', '4.2', '4.2']})
    >>> constraint = "a.0='a'"
    >>> result = equal_compare(a, constraint)
    >>> '4.2' in result[0]
    True
    >>> 'a' in result[0]
    True

    >>> constraint = "a.1='4.2'"
    >>> len(equal_compare(a, constraint))
    3

    >>> a.set_dict({'a.0': ['a', 'b', 'c'], 'a.1': [' 4.2', ' 4.2', ' 4.2']})
    >>> constraint = "a.1='4.2'"
    >>> len(equal_compare(a, constraint))
    3

    >>> constraint = 'a.0=a.1'
    >>> equal_compare(a, constraint)
    []
    '''
    # get the titles in the input table
    titles = target_table.get_title()
    # initialize rows which stores all the rows that satasfy the constraint
    rows = []
    # split two items which should be compared
    compared_items = constraint.split('=')
    # compare two columns
    if compared_items[1] in titles:
        # loop through each rows
        for row_num in range(target_table.num_rows()):
            # get two values from two column
            col1_value = target_table.get_one_value(compared_items[0], row_num)
            col2_value = target_table.get_one_value(compared_items[1], row_num)
            # if the columns in one row has the same value, then add the row
            if col1_value.strip() == col2_value.strip():
                rows.append(target_table.get_row(titles, row_num))
    # compare a column with a value
    else:
        # clean the value
        compared_items[1] = compared_items[1][1:-1]
        # loop through each rows
        for row_num in range(target_table.num_rows()):
            # get the value from the first column
            col1_value = target_table.get_one_value(compared_items[0], row_num)
            # if the column equals to the value, then add the row
            if col1_value.strip() == compared_items[1]:
                rows.append(target_table.get_row(titles, row_num))
    return rows


def greater_compare(target_table, constraint):
    ''' (Table, str) -> list of str list

    The function will select all the rows which are satasfy the constraint.
    The function will only compare two items with '>' sign.
    The function will return a list of str list which contains all the rows
    that satasfy the constraint.

    REQ: '>' in constraint

    >>> a = Table()
    >>> a.set_dict({'a.year': ['1998', '2014'], 'a.title': ['CSC', 'A08']})
    >>> constraint = "a.year>'2000'"
    >>> len(greater_compare(a, constraint))
    1

    >>> constraint = "a.year>'1898'"
    >>> len(greater_compare(a, constraint))
    2

    >>> constraint = "a.year>a.title"
    >>> greater_compare(a, constraint)
    []

    >>> constraint = "a.title>'AAAAA'"
    >>> result = greater_compare(a, constraint)
    >>> '1998' in result[0]
    True
    >>> 'CSC' in result[0]
    True
    >>> len(greater_compare(a, constraint))
    1

    >>> constraint = "a.title>'A000000'"
    >>> len(greater_compare(a, constraint))
    2

    >>> a.set_dict({'a.year': [' 1998', '2014 '], 'a.title': ['CSC', 'A08']})
    >>> constraint = "a.year>'1898'"
    >>> len(greater_compare(a, constraint))
    2
    >>> constraint = "a.year>a.title"
    >>> greater_compare(a, constraint)
    []
    '''
    # get the titles in the input table
    titles = target_table.get_title()
    # initialize rows which stores all the rows that satasfy the constraint
    rows = []
    # split two items which should be compared
    compared_items = constraint.split('>')
    # compare two columns
    if compared_items[1] in titles:
        # loop through each rows
        for row_num in range(target_table.num_rows()):
            # get two values from two columns
            col1_value = target_table.get_one_value(compared_items[0], row_num)
            col2_value = target_table.get_one_value(compared_items[1], row_num)
            # if two column value can change to float, then change it
            if can_be_float(col1_value) and can_be_float(col2_value):
                col1_value = float(col1_value.strip())
                col2_value = float(col2_value.strip())
            # if is unpossible, then clean each line to compare as str
            else:
                col1_value = col1_value.strip()
                col2_value = col2_value.strip()
            # if in one row, the value in first column is greater than the
            # value from the second column, then add the row
            if col1_value > col2_value:
                rows.append(target_table.get_row(titles, row_num))
    # compare a column with a value
    else:
        # get the compared value and clean the value, since it has quotation
        compare_value = compared_items[1][1:-1]
        # loop through each rows
        for row_num in range(target_table.num_rows()):
            # get the value from the first column
            col1_value = target_table.get_one_value(compared_items[0], row_num)
            # if column value and compared value can change to float,
            # then change both of them
            if can_be_float(col1_value) and can_be_float(compare_value):
                col1_value = float(col1_value.strip())
                compare_value = float(compare_value)
            # if is unpossible, then clean column value to compare as str
            else:
                col1_value = col1_value.strip()
            # if in one row the value from the first column is greater than
            # the compared value, then add the row
            if col1_value > compare_value:
                rows.append(target_table.get_row(titles, row_num))
    return rows


def process_all_constraints(target_table, constraints):
    ''' (Table, list of str) -> Table

    The function will select the table rows several times
    by going through all constraints.
    The function will select rows on input table by calling
    process_one_constraint function, and finally return a selected table.

    REQ: element in constraints should have correct syntax

    >>> a = Table()
    >>> a.set_dict({'a.0': ['a', 'b', 'c'], 'a.1': ['4.2', '4.2', '4.2']})
    >>> constraints = ["a.1='4.2'", "a.0='a'"]
    >>> result = process_all_constraints(a, constraints).get_dict()
    >>> result == {'a.0': ['a'], 'a.1': ['4.2']}
    True

    >>> constraints = ["a.1>'4'", "a.0>'a'"]
    >>> result = process_all_constraints(a, constraints).get_dict()
    >>> result == {'a.0': ['b', 'c'], 'a.1': ['4.2', '4.2']}
    True

    >>> constraints = ["a.0>'a'"]
    >>> result = process_all_constraints(a, constraints).get_dict()
    >>> result == {'a.0': ['b', 'c'], 'a.1': ['4.2', '4.2']}
    True

    >>> constraints = ["a.1='4.2'", "a.0>'b'"]
    >>> result = process_all_constraints(a, constraints).get_dict()
    >>> result == {'a.0': ['c'], 'a.1': ['4.2']}
    True
    '''
    # initialize result, and let it be the target_table
    result = target_table
    # loop through each constraint
    for constraint in constraints:
        # select rows by calling process_one_constraint function
        result = process_one_constraint(result, constraint)
    return result


def multi_cartesian_product(database, table_names):
    ''' (Database, list of str) -> Table

    The function will receieve a database and a list which has table names.
    The function will call cartesian_product several times based on
    how many table names in table_names.

    REQ: element in table_names must be in database

    >>> a = Table()
    >>> b = Table()
    >>> c = Table()
    >>> a.set_dict({'a': ['b', 'c']})
    >>> b.set_dict({'d': ['e', 'f'], 'g': ['h', 'i']})
    >>> c.set_dict({'x': ['y', 'z', 'haha']})
    >>> my_data = Database()
    >>> my_data.set_dict({'a': a, 'b': b, 'c': c})

    >>> isinstance(multi_cartesian_product(my_data, ['a', 'b', 'c']), Table)
    True
    >>> result = multi_cartesian_product(my_data, ['a', 'b', 'c'])
    >>> result.num_rows()
    12

    >>> isinstance(multi_cartesian_product(my_data, ['a', 'c']), Table)
    True
    >>> result = multi_cartesian_product(my_data, ['a', 'c'])
    >>> result.num_rows()
    6

    >>> d = Table()
    >>> d.set_dict({'1': ['2', '3', '4', '5', '999']})
    >>> my_data.set_dict({'a': a, 'b': b, 'c': c, 'd': d})
    >>> result = multi_cartesian_product(my_data, ['a', 'b', 'c', 'd'])
    >>> result.num_rows()
    60

    >>> e = Table()
    >>> my_data.set_dict({'a': a, 'b': b, 'c': c, 'd': d, 'e': e})
    >>> result = multi_cartesian_product(my_data, ['a', 'b', 'c', 'd', 'e'])
    >>> result = result.get_dict()
    >>> result == {'x': [], '1': [], 'a': [], 'd': [], 'g': []}
    True
    >>> 'x' in result
    True

    >>> e.set_dict({'CSCA': []})
    >>> result = multi_cartesian_product(my_data, ['a', 'b', 'c', 'd', 'e'])
    >>> result.num_rows()
    0
    >>> 'CSCA' in result.get_dict()
    True
    '''
    # create a table as the result, and let result be the first table
    result = database.get_table(table_names[0])
    # initialize index as 0
    index = 0
    # while loop through each file name in table_names
    while index < len(table_names)-1:
        # and the new table
        new_table = database.get_table(table_names[index+1])
        # let result be the product of result and new_table
        # result will be multiply by all the tables
        result = cartesian_product(result, new_table)
        index += 1
    return result


def cartesian_product(table_1, table_2):
    ''' (Table, Table) -> Table

    The function will receive two tables and return a table which is the
    product of two input tables.
    For each row from table_1, matching every rows from table_2, and the
    total number of row in output table should be the product of the number
    of rows in table_1 and table_2.

    >>> a = Table()
    >>> b = Table()
    >>> a.set_dict({'a': ['b', 'c']})
    >>> b.set_dict({'d': ['e', 'f'], 'g': ['h', 'i']})

    >>> isinstance(cartesian_product(a, b), Table)
    True
    >>> result = cartesian_product(a, b).get_dict()
    >>> result == {'g': ['h', 'i', 'h', 'i'], 'a': ['b', 'b', 'c', 'c'],\
    'd': ['e', 'f', 'e', 'f']}
    True

    >>> a.set_dict({'a': ['b', 'c', 'd']})
    >>> b.set_dict({'d': ['e', 'f'], 'g': ['h', 'i']})
    >>> isinstance(cartesian_product(a, b), Table)
    True
    >>> result = cartesian_product(a, b).get_dict()
    >>> result == {'g': ['h', 'i', 'h', 'i', 'h', 'i'],\
    'a': ['b', 'b', 'c', 'c', 'd', 'd'], 'd': ['e', 'f', 'e', 'f', 'e', 'f']}
    True

    >>> a.set_dict({'a': ['b', 'c', 'd', 'z']})
    >>> b.set_dict({'d': ['e'], 'g': ['h']})
    >>> isinstance(cartesian_product(a, b), Table)
    True
    >>> result = cartesian_product(a, b).get_dict()
    >>> result == {'g': ['h', 'h', 'h', 'h'], 'a': ['b', 'c', 'd', 'z'],\
    'd': ['e', 'e', 'e', 'e']}
    True

    >>> a.set_dict({'a': []})
    >>> isinstance(cartesian_product(a, b), Table)
    True
    >>> result = cartesian_product(a, b).get_dict()
    >>> result == {'g': [], 'a': [], 'd': []}
    True

    >>> c = Table()
    >>> isinstance(cartesian_product(c, b), Table)
    True
    >>> result = cartesian_product(c, b)
    >>> result.num_rows()
    0

    >>> d = Table()
    >>> isinstance(cartesian_product(c, d), Table)
    True
    >>> result = cartesian_product(c, d)
    >>> result.get_dict()
    {}
    '''
    # create a new table as a result
    result_table = Table()
    # get all of two input table's titles
    title_1 = table_1.get_title()
    title_2 = table_2.get_title()
    # get all of two inpur table's content
    data_1 = []
    data_2 = []
    # initialize the total_datas as a product of two data from two input table
    result_data = []
    # when only title_1 is empty
    if len(title_1) == 0 and len(title_2) != 0:
        result_title = title_2
    # when only title_2 is empty
    elif len(title_2) == 0 and len(title_1) != 0:
        result_title = title_1
    # when two titles are all empty
    elif len(title_1) == 0 and len(title_2) == 0:
        result_title = []
    # when all of titles are not empty
    else:
        # loop through each row in first table to get its data
        for i in range(table_1.num_rows()):
            data_1.append(table_1.get_row(title_1, i))
        # loop through each row in second table to get its data
        for i in range(table_2.num_rows()):
            data_2.append(table_2.get_row(title_2, i))
        # the result_title should be the sum of two titles from input tables
        result_title = title_1 + title_2
        # loop through data_1 and data_2 to get the cartesian product
        for first_data in data_1:
            for second_data in data_2:
                # add the final data into result_data
                result_data.append(first_data + second_data)
    # use method from Table to store table_list
    new_table_list = result_table.store_table_list(result_title, result_data)
    # loop through each element in new_table_list
    # and add titles and data into the result_table
    for element in new_table_list:
        result_table.add_new_row(element[0], element[1:])
    return result_table


if(__name__ == "__main__"):
    # ask for the query
    query = input("Enter a SQuEaL query, or a blank line to exit:")
    # loop to keey asking query until enter nothing
    while query != '':
        # get the database by reading all the files
        database = read_database()
        # get the new table and print the table
        result_table = run_query(database, query)
        result_table.print_csv()
        # ask for query again
        query = input("Enter a SQuEaL query, or a blank line to exit:")
