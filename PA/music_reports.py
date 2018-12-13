import os
import file_handling
import display
import sys

ARTIST = 0
ALBUM = 1
YEAR = 2
GENRE = 3
DURATION = 4
#---------------------------------------------------------------
#VARIABLES FOR SPECIAL FUNCTIONS

table= file_handling.import_data()
title_list = ['ARTIST','ALBUM','YEAR','GENRE','DURATION']

#-------------------------------------------------------------
#MENU FUNCTIONS

#Shows data in a neat table
def show_music_library():
    display.print_table(table, title_list)
    

def add_album_to_library():
    pass



#FUNCTION RETURNS LIST OF ALBUMS FROM GIVEN GENRE IN SEPARATE LINES
def get_albums_by_genre():
    '''FUNCTION RETURNS LIST OF ALBUMS FROM 
    GIVEN GENRE IN SEPARATE LINES''' #zdjąć caps lock
    
    user_genre = display.get_user_input('Please choose from:')
    display.print_result("",get_all_genres_in_library())
    display.check_genre(user_genre) #foolprof

    for single_line in table:
        if user_genre == single_line[GENRE]:
            display.print_result("This album is in given genre",
                                 single_line[ALBUM])



#FUNCTION GETS THE QUANTITY OF ALBUMS IN GENRES AND RETURNS PAIRS IN DICTIONARY
def get_quantity_by_genres():
    dict_quantity_in_genres = {}

    for single_line in table:
        if single_line[GENRE] not in dict_quantity_in_genres.keys():
            dict_quantity_in_genres[single_line[GENRE]] = 1
        else:
            dict_quantity_in_genres[single_line[GENRE]] += 1

    for genre, amount in dict_quantity_in_genres.items():
        display.print_result(genre, amount)



#FUNCTION RETURNS THE ALBUM WITH THE EARLIES RELEASE YEAR
def get_oldest_album():

   #assigning earliest year to a variable with conversion to string type
    earliest_release_year = int(table[0][YEAR])
  
    # searching earlies year in datatable by parsing through every row and comparing values
    for single_line in table:
        single_line[YEAR] = int(single_line[YEAR]) 

        if single_line[YEAR] < earliest_release_year:
            earliest_release_year = single_line[YEAR]

    oldest_albums = []
    for single_line in table:
        if single_line[YEAR] == earliest_release_year:
            oldest_albums.append(single_line[ALBUM])

    #presenting result from the very latest
    display.print_result("The oldest albums in library :",
                         oldest_albums[::-1]) 




def get_oldest_album_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """
    return get_last_oldest(get_albums_by_genre(albums,genre))



def get_longest_album(albums):
    """
    Get album with biggest value in length field

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    result = albums[0]
    for album in albums:
        if to_time(album[DURATION]) > to_time(result[DURATION]):
            result = album
    return result

def to_time(str):
    """
    converts time in format "minutes:seconds" (string) to seconds (int)
    """
    SEC_IN_MIN = 60
    min_sec = str.split(':')
    return int(min_sec[0])*SEC_IN_MIN + int(min_sec[1])


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    durations = map(lambda album: to_time(album[DURATION]), albums)
    total = sum(durations)
    return int(total / 60) + ((total % 60)/ 60)

def get_all_genres_in_library():
    all_genres =[]
    for line in table:
        if line[GENRE] not in all_genres:
            all_genres.append(line[GENRE])
    return all_genres

#----------------------------------------------
#EXIT FUNCTION

def exit_program():
    sys.exit(0)
