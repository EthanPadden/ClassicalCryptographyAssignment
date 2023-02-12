import numpy as np

if __name__ == '__main__':
    plaintext = 'MARY HAS A LITTLE LAMB ITS FLEECE AS WHITE AS SNOW'
    key = 'TOMATOJUICE'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789 '

    # CREATING GRID
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

