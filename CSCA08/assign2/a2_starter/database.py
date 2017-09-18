class NoTiltleError(Exception):
    '''An error to be raised when user wanst to get the value in dictionary,
    but the searched key is not in dict'''


class Table():
    '''A class to represent a SQuEaL table'''

    def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType

        Populate this table with the data in new_dict.
        The input dictionary must be of the form:
            column_name: list_of_values
        '''
        self._table = new_dict

    def get_dict(self):
        '''(Table) -> dict of {str: list of str}

        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
        return self._table

    def print_csv(self):
        '''(Table) -> NoneType
        Print a representation of table in csv format.
        '''
        # no need to edit this one, but you may find it useful (you're welcome)
        dict_rep = self.get_dict()
        columns = list(dict_rep.keys())
        print(','.join(columns))
        rows = self.num_rows()
        for i in range(rows):
            cur_column = []
            for column in columns:
                cur_column.append(dict_rep[column][i])
            print(','.join(cur_column))

    def __init__(self):
        ''' (Table) -> NoneType
        Initialize the table as a dictionary.
        '''
        self._table = {}

    def num_rows(self):
        ''' (Table) -> int
        Return the number of total rows.
        REQ: self._table is form of {str: list}
        '''
        # no matter which column should have same num of rows
        # so we can get any column to get the num of rows
        titles = self.get_title()
        column = titles[0]
        return len(self._table[column])

    def store_table_list(self, titles, content):
        ''' (Table, list of str, list of str list) -> list of str list

        The function will receive two lists as parameters and store two lists.
        The first list is the title of the table and the second list is
        the content of each table.
        The function will create a matrix which is list of str list
        to distinguish each title and matching content.
        Finally, the function will return this list

        REQ: titles must be the type of list
        REQ: content must be the type of list of str list
        '''
        # create a list to store content
        table_list = []
        # loop through each title, put them as a list into the table_list
        for title in titles:
            # put each title as a list into the table_list
            table_list.append([title])
        # loop through each line from the file
        for line in content:
            # loop through each element, and matching each element with titles
            index = 0
            # check if the line is blank
            while index < len(table_list) and (line != ['']):
                table_list[index].append(line[index])
                index += 1
        return table_list

    def add_new_row(self, key, value):
        ''' (Table, str, list of str) -> NoneType

        The function will receive two parameters which are key and value.
        The function will and the key and matching value into self._table.

        REQ: key is not in self._table, or it will not add a new row
        '''
        self._table[key] = value

    def get_one_value(self, title, row_num):
        ''' (Table, str, int) -> str

        The function will return specific value of the input title and
        input row_num.

        REQ: title in self._table
        REQ: roe_num < len(self._table[title])
        RAISES: NoTiltleError if title not in self._table
        '''
        # if title not in self._table, then raise NoTiltleError
        if not(title in self._table):
            raise NoTiltleError('can not find searched column')
        return self._table[title][row_num]

    def get_row(self, titles, row_num):
        ''' (Table, list of str, int) -> list of str

        The function will return specific row based on two input parameters.
        REQ: each element in titles must be in self._table
        REQ: row_num can not go out of the range
        '''
        data = []
        for title in titles:
            data.append(self._table[title][row_num])
        return data

    def get_column(self, column_name):
        ''' (Table, str) -> list of str
        The function will return a list of str which is one column in the
        table.
        What column wwould be returned is based on another parameter,
        which is column_name.

        REQ: column_name in self._table
        RAISES: NoTiltleError if column_name not in self._table
        '''
        # create list to store this column
        column = []
        # if column_name not in self._table, then raise NoTiltleError
        if not(column_name in self._table):
            raise NoTiltleError('can not find searched column')
        # add the column name and rows
        column.append(column_name)
        column = column + self._table[column_name]
        return column

    def get_title(self):
        ''' (Table) -> list of str
        The function will return all the title names.
        '''
        titles = []
        for title in self._table:
            titles.append(title)
        return titles


class Database():
    '''A class to represent a SQuEaL database'''

    def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        new_dict must have the format:
            table_name: table
        '''
        self._database = new_dict

    def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        return self._database

    def __init__(self):
        ''' (Database) -> NoneType
        Initialize a database as a dictionary.
        '''
        self._database = {}

    def get_table_name(self, old_names):
        ''' (Database, list of str) -> list of str
        The functio will get the table's names by delete ".csv".

        REQ: str in old_names must end by '.csv'
        '''
        # create an empty list to store table names
        table_names = []
        # for each file, delete ".csv" to create a table name
        for name in old_names:
            name = name[:-4]
            # add name into the list
            table_names.append(name)
        return table_names

    def add_new_table(self, file_list, tables):
        ''' (Database, list of str, Table) -> NoneType

        The function will add new tables into self._database.
        The name of the table is exactly the name of the file without
        ".csv".

        REQ: str in file_list can not be repeted, or can not add new table
        '''
        # get the table name first
        table_names = self.get_table_name(file_list)
        index = 0
        # loop through each table and add into database
        while index < len(table_names):
            self._database[table_names[index]] = tables[index]
            index += 1

    def get_table(self, table_name):
        ''' (Database, str) -> Table
        The function will receive the table's name, and then return the table.

        REQ: table_name in self._database
        RAISES: NoTiltleError if seached table is not in self._database
        '''
        # raise NoTiltleError when seached table is not in self._database
        if not (table_name in self._database):
            raise NoTiltleError('can not find searched table')
        return self._database[table_name]
