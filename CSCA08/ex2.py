# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
# HINT: Your code should be using these values, if I change them (and I will)
# your output should change accordingly
a0_weight = 5
a1_weight = 7
a2_weight = 8
term_tests_weight = 20
exam_weight = 45
exercises_weight = 10
quizzes_weight = 5

a0_max_mark = 25
a1_max_mark = 50
a2_max_mark = 100
term_tests_max_mark = 50
exam_max_mark = 100
exercises_max_mark = 10
quizzes_max_mark = 5
exam_pass_mark = 40
overall_pass_mark = 50


def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name must be one of: a0,a1,a2,exerises,midterm,exam
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of E2.
    if(component_name == 'a0'):
        result = a0_max_mark
    elif(component_name == 'a1'):
        result = a1_max_mark
    elif(component_name == 'a2'):
        result = a2_max_mark
    elif(component_name == 'exercises'):
        result = exercises_max_mark
    elif(component_name == 'term tests'):
        result = term_tests_max_mark
    elif(component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result


def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_max <= max_mark
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    '''
    return raw_mark / max_mark * 100


def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: weight >= 0
    >>> contribution(13.5, 15, 10)
    9.0
    '''
    # start your own code here
    return (raw_mark / max_mark) * weight


def term_work_mark(a0, a1, a2, exercises, quizzes, test):
    '''(float, float, float，float, float, float) -> float
    Given the term work mark by using the default weights
    This will return a maximum result of 55
    REQ: 0 <= a0 <= 25
    REQ: 0 <= a1 <= 50
    REQ: 0 <= a2 <= 100
    REQ: 0 <= exercises <= 10
    REQ: 0 <= quizzes <= 5
    REQ: 0 <= test <= 50
    >>> term_work_mark(17, 40, 76, 9, 3, 30)
    39.08
    >>> term_work_mark(25, 50, 100, 10, 5, 50)
    55.0
    '''
    # calculation of each default weight
    c_a0 = contribution(a0, a0_max_mark, a0_weight)
    c_a1 = contribution(a1, a1_max_mark, a1_weight)
    c_a2 = contribution(a2, a2_max_mark, a2_weight)
    c_exercises = contribution(exercises, exercises_max_mark, exercises_weight)
    c_quizzes = contribution(quizzes, quizzes_max_mark, quizzes_weight)
    c_test = contribution(test, term_tests_max_mark, term_tests_weight)
    overall = c_a0 + c_a1 + c_a2 + c_exercises + c_quizzes + c_test
    return overall


def final_mark(a0, a1, a2, exercises, quizzes, test, exam):
    '''(float, float, float，float, float, float, float) -> float
    Given the term work mark by using the default weights within the exam
    This will return a maximun result of 100
    REQ: 0 <= a0 <= 25
    REQ: 0 <= a1 <= 50
    REQ: 0 <= a2 <= 100
    REQ: 0 <= exercises <= 10
    REQ: 0 <= quizzes <= 5
    REQ: 0 <= test <= 50
    RED: 0 <= exam <= 100
    >>> final_mark(25, 50, 100, 10, 5, 50, 100)
    100.0
    >>> final_mark(20, 40, 90, 5, 5, 40, 99)
    87.35
    '''
    # calculation of exam
    c_exam = contribution(exam, exam_max_mark, exam_weight)

    # the sum of term work mark and exam
    total = term_work_mark(a0, a1, a2, exercises, quizzes, test) + c_exam
    return total


def is_pass(a0, a1, a2, exercises, quizzes, test, exam):
    '''(float, float, float，float, float, float, float) -> boolean
    Given all the marks student got
    including assignment 0, 1, 2, exercises, quizzes, tests and exam
    This will return a boolean which shows that wether the grade entered pass
    or not.
    The requirement is passing the course:
    A final overall mark of 50 or greater, and a dinal exam mark of 40 or
    greater.
    REQ: 0 <= a0 <= 25
    REQ: 0 <= a1 <= 50
    REQ: 0 <= a2 <= 100
    REQ: 0 <= exercises <= 10
    REQ: 0 <= quizzes <= 5
    REQ: 0 <= test <= 50
    RED: 0 <= exam <= 100
    >>> is_pass(20, 40, 90, 5, 5, 40, 99)
    True
    >>> is_pass(20, 40, 90, 5, 5, 40, 38)
    False
    >>> is_pass(5, 12, 30, 10, 0, 20, 50)
    False
    '''
    # whether the final overall mark is greater or equal than 50
    b_final = final_mark(a0, a1, a2, exercises, quizzes, test, exam) >= 50
    # whether the exam grade is greater or equal than 40
    b_exam = exam >= 40
    return b_final and b_exam


# Here is my test
# print(percentage(15, 20))
# print(percentage(4.5, 4.5))
#
# print(contribution(13.5, 15, 10))
#
# print(term_work_mark(25, 50, 100, 10, 5, 50))
# print(term_work_mark(20, 45, 70, 8, 4, 40))
#
# print(final_mark(25, 50, 100, 10, 5, 50,100))
# print(final_mark(20, 45, 70, 8, 4, 40, 73))
#
# print(is_pass(20, 45, 70, 8, 4, 40, 41))
# print(is_pass(20, 45, 70, 8, 4, 40, 39))
# print(is_pass(10, 21, 12, 2, 1, 15, 23))
