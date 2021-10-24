import sys

def is_mac():
    return sys.platform == 'darwin'

def is_win():
    return sys.platform == 'win32'

def is_linux():
    return sys.platform == 'linux'

def get_class_name(class_name):
    return class_name.__class__.__name__


def gcm(class_obj):
    # get class obj name
    return class_obj.__name__


def get_class(class_name):
    return class_name.__class__


def is_class(class_obj):
    import inspect
    return inspect.isclass(class_obj)


def display_error(error_message):
    print('******** Couldn\'t Complete the operation. ********')
    print('ERROR: {}. '.format(str(error_message)))


# Levenshtein Minimum Edit Distance
def MED(A, B):
    import numpy

    m = len(A)
    n = len(B)
    D = numpy.zeros((m + 1, n + 1))
    for i in range(1, m + 1):
        D[i, 0] = i
    for j in range(1, n + 1):
        D[0, j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                alpha = 0
            else:
                alpha = 2

            D[i, j] = min(D[i - 1, j] + 1,
                          D[i, j - 1] + 1, D[i - 1, j - 1] + alpha)
    return D[m, n]


def multi_choice_dialog(choices):
    print("What do you mean?")

    choice_count = 0
    for choice in choices:
        print("   [{}] {}".format(choice_count, choice))
        choice_count += 1

    selected_option = None

    while selected_option is None or (selected_option > choice_count or selected_option < 0):
        try:
            selected_option = int(input("Select an option: "))
        except Exception as e:
            print('****** ERROR: {}. ******'.format(str(e)))

    return int(selected_option)


def print_w_time(str):
    import datetime
    x = datetime.datetime.now()
    x = x.strftime("%Y:%m:%d %H:%M")

    print("[{}] {}".format(x, str))


def cleanStr(str):
    return ''.join(e for e in str if e.isalnum()).lower()

def say(str, time=False):
    import core.Voice as v

    if time:
        print_w_time(str)
    else:
        print(str)

    v.Voice().say(str)

