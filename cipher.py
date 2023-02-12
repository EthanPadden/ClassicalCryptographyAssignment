import numpy as np
import sys

if __name__ == '__main__':
    # *** parsing command line arguments and sanity check of strings ***

    # check arguments from command line
    if len(sys.argv) < 2:
        raise Exception('not enough arguments')

    plaintext = sys.argv[0]
    key = sys.argv[1]

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789 '

    # check that all characters in the plaintext and key are in our alphabet
    for character in plaintext:
        if character not in alphabet:
            raise Exception('character ' + str(character) + ' not in alphabet')

    for character in key:
        if character not in alphabet:
            raise Exception('character ' + str(character) + ' not in alphabet')


    # plaintext = 'MARY HAS A LITTLE LAMB ITS FLEECE AS WHITE AS SNOW'
    # key = 'TOMATOJUICE'

    # ***  setting up the grid, based on the keyword entered ***
    grid = np.empty((6, 6))     # create empty 6x6 matrix

    # remove duplicate letters from key
    grid_array = []
    for letter in key:
        if letter not in grid_array:
            grid_array.append(letter)

    # now we have an array that starts with the key
    # we need to populate the rest of the array until it reaches 6x6 = 36 characters

    for letter in alphabet:
        # we want to ignore letters that we already have in the grid array
        if letter not in grid_array:
            grid_array.append(letter)
            # TODO: remove hard coded values like this
            if len(grid_array) >= 36:
                break

    grid = np.reshape(grid_array, (6,6))

    # *** preprocessing the plaintext string
    # check if there is an even number of characters
    if len(plaintext) % 2 != 0:
        raise Exception('plaintext must have an even number of characters')
    else:
        # split the plaintext into pairs of characters
        pairs = []
        i = 0
        while i < len(plaintext):
            pairs.append([
                plaintext[i],
                plaintext[i + 1]
            ])
            i += 2

        # find duplicate letters and replace the 2nd with X
        # in the same loop, convert any occurrence of 0 to O
        for pair in pairs:
            if pair[0] == pair[1]:
                pair[1] = 'X'

            # this will not change the Xs back into 0s or Os
            if pair[0] == '0':
                pair[0] = 'O'
            if pair[1] == '0':
                pair[1] = 'O'
        # TODO: pair replaced with X may be wrong - go over

        # apply Playfair rules
        # iterate through pairs
        print(grid)
        # for pair in pairs:
        for pair in pairs:
            # find where the first element is in the grid
            location1 = np.where(grid == pair[0])
            location2 = np.where(grid == pair[1])

            # these are zero indexed
            # the second [0] is simply to convert the result from a list to an int
            # e.g. [5] to 5
            row1_index = location1[0][0]
            column1_index = location1[1][0]
            row2_index = location2[0][0]
            column2_index = location2[1][0]

            # check are they in the same row
            if row1_index == row2_index:
                print('row')
                # get the row of the grid as a list
                row = grid[row1_index]

                # the column vars are the indexes of the list, so replace them with the following character in the row
                pair[0] = row[(column1_index + 1) % 6]
                pair[1] = row[(column2_index + 1) % 6]

            # check are they in the same column
            elif column1_index == column2_index:
                print('column')
                # get the column of the grid as a list
                column = grid[:, column1_index]

                # the row vars are the indexes of the list, so replace them with the following character in the column
                pair[0] = row[(row1_index + 1) % 6]
                pair[1] = row[(row2_index + 1) % 6]

            # otherwise apply the last rule - Otherwise each letter gets replaced by the letter in its row but in the other
            # letters column
            else:
                print('neither')
                row1 = grid[row1_index]
                row2 = grid[row2_index]

                pair[0] = row1[column2_index]
                pair[1] = row2[column1_index]

        # join ciphertext together into string
        joined_pair_strs = []
        for pair in pairs:
            joined_pair_str = ''.join(pair)
            joined_pair_strs.append(joined_pair_str)

        ciphertext = ''.join(joined_pair_strs)
        print(ciphertext)
        if len(ciphertext) != len(plaintext):
            raise Exception('something went wrong')
#TODO: 0 to O