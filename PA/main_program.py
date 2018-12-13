"""
The main program should use functions from music_reports and display modules
"""
import os
import music_reports
import display

#---------------------------------------------------
#DICTIONARY WITH MENU OPTIONS FOR USER TO CHOOSE

dict_menu_options = {'1':{'opt':'Show music library',
    'func':music_reports.show_music_library},
'2':{'opt':'Add album to library',
    'func':music_reports.add_album_to_library},
'3':{'opt':'Get album by genre',
'func':music_reports.get_albums_by_genre},
'4':{'opt':'Get the quantity of albums in given genre',
'func':music_reports.get_quantity_by_genres},
'5':{'opt':'Get the oldes album',
'func':music_reports.get_oldest_album},
'6':{'opt':'Get the oldest album of given genre',
'func':music_reports.get_oldest_album_of_genre},
'7':{'opt':'Get the longest album',
'func':music_reports.get_longest_album},
'8':{'opt':'Get total lenght of albums',
'func':music_reports.get_total_albums_length},
'0':{'opt':'Exit program',
'func':music_reports.exit_program}}

#---------------------------------------------------
# FUNCTION EXECUTING USER'S CHOICE OF MENU OPTION

def choose_option():
    display.print_menu(dict_menu_options)
    user_choice = display.get_user_input("What'cha wanna do?: ")

    if user_choice in dict_menu_options.keys():
        dict_menu_options[user_choice]["func"]()
    else:
        display.print_error_message("Hold your horses! No such option.")


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    while(True):
        choose_option()


if __name__ == '__main__':
    main()
