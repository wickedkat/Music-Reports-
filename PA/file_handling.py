import os # for os.system("clear")
import sys # for sys.exit(0)
import display # for printing data

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FUNCTION FOR IMPORTATION CONTENT FROM TXT FILE


def import_data(filename='albums_data.txt'):
    """
    Import data from a file to a list. Expected returned data format:
        ["David Bowie", "Low", "1977", "rock", "38:26"],
        ["Britney Spears", "Baby One More Time", "1999", "pop", "42:20"],
        ...]

    :param str filename: optional, name of the file to be imported

    :returns: list of lists representing albums' data
    :rtype: list
    """
    check_if_file_exists(filename)
    result = []
    with open(filename, 'r') as datafile:
        for line in datafile.readlines():
            result.append(line.strip().split(','))
    return result

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FUNCTION CHECKS IF FILE EXISTS


def check_if_file_exists(filename):
    if os.path.isfile(filename) is False:
        print("There is no file at all!")
        sys.exit(0)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FUNCTION FOR EXPORTING FILE INTO EXTERNAL FILE (NOT USED IN THIS PA)


def export_data(albums, filename='albums_data.txt', mode='a'):
    """
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list albums: albums' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    if mode not in ['a', 'w']:
        raise ValueError('Wrong write mode')
    with open(filename, mode) as datafile:
        for album in albums:
            datafile.write(','.join(album) + '\r\n')
