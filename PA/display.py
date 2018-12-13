import os #clearing in error message function
import file_handling
import sys
import music_reports

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#FUNCTIONS PRINTING COLORED TABLE

#helping variables for table printing section
max_width_column = []
line_horizon_color = "\033[96m-\033[00m"   # sea-blue color
line_left_colored = "\033[96m/\033[00m"
line_right_colored = "\033[96m\\\033[00m"
line_vertical_color = "\033[96m|\033[00m"


# Define max length for colums in table

'''
This function parses through every row in every column
on the list of lists, comparing lenght of every item in column
with the preceding one. Temporarily longest item is stored under
local variable 'temp'. Number of colums is known by the lenght 
of the title_list

parameters: table (list of lists), title_list(list)

returns: list with one integer

'''
def max_width(table, title_list):
    max_width_column = []
    for column in range(len(title_list)):
        temp = 0
        for row in range(len(table)):
            if len(str(table[row][column])) > temp:
                temp = len(str(table[row][column]))
                temp = int(temp)
        max_width_column.append(temp)
    return max_width_column


# Define total width of the table

'''
This function sums up the width of all the colums, basing on their 
max width with.

parameters: max_width_column (list), title_list(list)

returns: integer

'''
def sum_width_table(max_width_column, title_list):
    sum_length = len(title_list)*2
    for i in range(len(max_width_column)):
        sum_length += max_width_column[i]
    return sum_length


# function prints upper border of the table
def print_top_border(sum_length):
    print(line_left_colored, (line_horizon_color*(sum_length-3)), line_right_colored)


# function prints middle part of the table
def print_middle_border(sum_length):
    print(line_vertical_color, (line_horizon_color*(sum_length-3)), line_vertical_color)


# prints bottom border of the table
def print_bottom_border(sum_length):
    print(line_right_colored, (line_horizon_color*(sum_length-3)), line_left_colored)


# prints headers from title_list into colums
def print_columns_title(title_list, max_width_column):
    for col_i in range(len(title_list)):
        col = title_list[col_i]
        width = max_width_column[col_i]
        print(line_vertical_color, col.center(width), end='')
    print(line_vertical_color)


# prints data from file to the table
def print_items_table(table, max_width_column, sum_length, title_list):
    row_number = 1
    for row in table:
        print_middle_border(sum_length)
        for col_i in range(len(row)):
            col = row[col_i]
            width = max_width_column[col_i]
            if col_i == 0:
                print(line_vertical_color, str(row_number).center(width),  end='')
            else:
                print(line_vertical_color, col.center(width),  end='')
        row_number += 1
        print(line_vertical_color)


# print table based on tilte list and table from imported file
def print_table(table, title_list):
    """
    Prints table with data.
    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers
    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    max_width_column = []
    temp_table = table.copy()
    temp_table.append(title_list)
    max_width_column = max_width(temp_table, title_list)
    sum_length = sum_width_table(max_width_column, title_list)
    print_top_border(sum_length)
    print_columns_title(title_list, max_width_column)
    print_items_table(table, max_width_column, sum_length, title_list)
    print_bottom_border(sum_length)

#--------------------------------------------------------
#FUNCTION PRINTING MAIN MENU
def print_menu(dict_menu_options):
    print("")
    print("Codecool MUSIC LIBRARY Menu:")
    for key, value in dict_menu_options.items():
        print(key, value["opt"])
        

#--------------------------------------------------------
#PRINTING RESULTS OF FUNCTIONS FROM MUSIC REPORTS

def print_result(comment, result):
    print(f"{comment}: {result}")

#--------------------------------------------------------
# PRINTING ERROR MESSAGE

def print_error_message(sentence):
    os.system("clear")
    print(sentence)

#---------------------------------------------------------
#GETTING INPUT FROM USER

def get_user_input(sth_user_writes):
    return input(sth_user_writes)

#FOOLPROOF FOR GENRES
def check_genre(user_choice):
    genres = music_reports.get_all_genres_in_library()
    if user_choice not in genres:
        print("Blind shot! No such genre.")
        