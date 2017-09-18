def create_dict(filehandle):
    ''' (io.TextIOWrapper) -> dict of {str: [str, str, str, int ,str]}

    The function will receive a text file and retun a dictionary which
    is based on the text file.
    The dictionary will keep username as a key and value is an list
    which includes last name, first name, e-mail, age and gender.
    '''
    # read the filhandle by lines
    lines = filehandle.readlines()
    # initialize a dictionary
    result = {}
    # read each line
    for line in lines:
        # delete \n and split in the sapce
        line = line.strip('\n').split()
        # add infomation into result in the particular order
        result[line[0]] = [line[2], line[1], line[5], int(line[3]), line[4]]
    return result


def get_the_index(field):
    ''' (str) -> int

    The function will return the index of the dictionary created in the first
    function.
    The index for last name, first name, e-mail address, age and gender are
    0, 1, 2, 3, and 4.

    REQ: field should only be 'LAST', 'FIRST', 'E-MAIL', 'AGE', or 'GENDER'

    >>> get_the_index('LAST')
    0
    >>> get_the_index('AGE')
    3
    >>> get_the_index('FIRST')
    1
    >>> get_the_index('E-MAIL')
    2
    >>> get_the_index('GENDER')
    4
    '''
    # initialize index
    index = 0
    # for each field has a special index number
    if field == 'LAST':
        index = 0
    elif field == 'FIRST':
        index = 1
    elif field == 'E-MAIL':
        index = 2
    elif field == 'AGE':
        index = 3
    elif field == 'GENDER':
        index = 4
    return index


def update_field(dictionary, username, field, value):
    ''' (dict, str, str, int or str) -> NoneType

    The function will receive four parameters which are dictionary, username,
    the name of field (one of: 'LAST', 'FIRST', 'E-MAIL', 'AGE', 'GENDER'),
    and a new value to replace.
    The function will return nothing but mutate the input dict.

    REQ: field should only be 'LAST', 'FIRST', 'E-MAIL', 'AGE', or 'GENDER'

    >>> my_dict = {'sclause':['Clause','Santa','santa@christmas.np',450,'M']}
    >>> update_field(my_dict, 'sclause', 'AGE', 999)
    >>> my_dict == {'sclause':['Clause','Santa','santa@christmas.np',999,'M']}
    True
    >>> my_dict == {'sclause':['Clause','Santa','santa@christmas.np',994,'M']}
    False
    '''
    # search the infomation of the specific username
    info = dictionary[username]
    # call the get_the_index function to gat the index
    index = get_the_index(field)
    # replace the value
    info[index] = value
    # add new infomation into the dictionay
    dictionary[username] = info
    return None


def select(dictionary, select_field, check_field, check_value):
    ''' (dict, str, str, str or int) -> set
    The function will return a set of all the data elements from the selected
    fields of people whose checked fields were equal to the checked value.

    REQ: select_field should only be 'LAST', 'FIRST', 'E-MAIL', 'AGE', or
    'GENDER'
    REQ: check_field should only be 'LAST', 'FIRST', 'E-MAIL', 'AGE', or
    'GENDER'

    >>> my_dict = {'sclause':['Clause','Santa','santa@christmas.np',450,'M'],\
    'ebunny':['Bunny','Easter','bunny@easter.hop',99,'M'],\
    'tfairy':['Fairy','Tooth','fairy@money4teech.net',0,'F']}
    >>> select(my_dict, 'E-MAIL', 'GENDER', 'M')
    {'santa@christmas.np', 'bunny@easter.hop'}
    '''
    # initialize the result set
    result = set()
    # call the get_the_index function to get index
    select_index = get_the_index(select_field)
    check_index = get_the_index(check_field)
    # traverse the dictionary and search the value
    for key in dictionary:
        if dictionary[key][check_index] == check_value:
            # add the matching value into the set
            result.add(dictionary[key][select_index])
    return result
