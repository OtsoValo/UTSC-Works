def function_name(filehandle):
    '''(io.TextIOWrapper) -> list or str
    The function will open the input filehandle and only return all the
    functions mentioned in the file.

    >>> function_name('ex5.py')
    ['function_name', 'justified', 'section_average']
    >>> function_name('ex4.py')
    ['insert', 'up_to_first', 'cut_list']
    >>> function_name('ex3.py')
    ['percent_to_gpv', 'card_namer', 'my_str']
    '''
    # open the filehandle and read all the lines of it
    file = open(filehandle, 'r')
    lines = file.readlines()
    file.close()
    # define a final result
    result = []
    for each_line in lines:
        # if the begining of the line is def, then it must be a function name
        if each_line.startswith('def'):
            end_index = each_line.index('(')
            # add the function names into result
            result.append(each_line[4:end_index])
    return result


def justified(filehandle):
    '''(io.TextIOWrapper) -> list or str
    The function will read the input filehandle by lines and return a
    boolean which decides if the file is left justified, return True
    if the file is left justified.

    >>> justified('ex5_grade_file.txt')
    True
    '''
    # open the file and read it by lines
    file = open(filehandle, 'r')
    lines = file.readlines()
    file.close()
    # let the result be True initially
    result = True
    # let the number of lines be zore
    line_num = 0
    # check left justified line by line
    while (line_num < len(lines)) and (result is True):
        # if one line is not left justified then stop the while loop
        if lines[line_num].startswith(' '):
            result = False
        line_num += 1
    return result


def section_average(mid_marks, input_sec_name):
    '''(io.TextIOWrapper, str) -> float or Nonetype
    This function will read the filehandle and store the grades by
    section names.
    The second parameter is to search the section name, if there exist
    the grades that belongs to the input section then return all the grades.
    If these is no name that is same with the input section name, then return
    a string which is 'None'

    >>> section_average('ex5_grade_file.txt','LEC03')
    >>> section_average('ex5_grade_file.txt','LEC02')
    18.5
    >>> section_average('ex5_grade_file.txt','LEC01')
    16.5
    >>> section_average('ex5_grade_file.txt','joey')
    >>> section_average('ex5_grade_file.txt', 'LEC30')
    15.0
    '''
    # open the file and read by lines
    file = open(mid_marks, 'r')
    lines = file.readlines()
    file.close
    # define a list that store all the grades and section names
    grade_list = []
    # check all the section names and grades line by line and store them
    for each_line in lines:
        each_line = each_line.strip('\n')
        sec_num = each_line.index('LEC')
        sec_name = each_line[sec_num: sec_num+5]
        # store all the grades after their section names
        if sec_name in grade_list:
            each_line = each_line.split(' ')
            while each_line[len(each_line)-1] == '':
                each_line.pop()
            grade = float(each_line[len(each_line)-1])
            grade_list.insert(grade_list.index(sec_name)+1, grade)
        # store all the section names
        else:
            grade_list.append(sec_name)
    # Now, it is going to search input section name
    # and return all the grades.
    # initial the average mark, and total mark
    ave_mark = 0
    total_mark = 0
    # if the input section anme is in the storage
    if input_sec_name in grade_list:
        sec_index = grade_list.index(input_sec_name) + 1
        # define a list only including grades which is going to be returned
        output_grade_list = []
        is_float = True
        # Put all the number which is belongs to the input section name
        # into the result list.
        while (sec_index < len(grade_list)) and (is_float is True):
            if type(grade_list[sec_index]) == float:
                output_grade_list.append(grade_list[sec_index])
            else:
                is_float = False
            sec_index += 1
    # calculate average mark
        for all_num in output_grade_list:
            total_mark += all_num
        ave_mark = total_mark / len(output_grade_list)
    # if the input section anme is in the storage, then return 'None'
    else:
        ave_mark = None
    return ave_mark
