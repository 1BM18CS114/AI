# Given M x N grid(floor) create an agent that moves around the grid until the entire grid is clean

floor = [[1, 0, 0, 0], # '1' represents dirty and '0' represents clean
         [0, 1, 0, 1],
         [1, 0, 1, 1]]


def clean(floor):
    m = len(floor[0]) # no of cols
    n = len(floor)    # no of rows
    no_of_tiles = m * n

    tiles_checked = 0

    row = 0
    col = 0
    while tiles_checked < no_of_tiles:
        # Current position
        print_floor(floor, row, col)

        # Suck if dirty
        if floor[row][col] == 1:
            floor[row][col] = 0
            print('Sucked the dirt')
        else:
            print('Already Clean')
        
    
        # Next tile
        if row % 2 == 0:          # Even rows the bot moves right to the next tile
            if col < m-1:
                col += 1
            else:
                row += 1  # Move to next row if we reached the last col
        
        elif row % 2 == 1:        # Odd rows the bot moves left to the next tile
            if 0 < col:
                col -= 1
            else:
                row += 1  # Move to next row if we reached the last col
        
        tiles_checked += 1
        print('---------------')
    
    print('Cleaned!!!')
        

        
def print_floor(floor, row, col):
    temp = floor[row][col]
    floor[row][col] = 'VC'
    for x in floor:
        print(x)
    
    floor[row][col] = temp

# For above floor
clean(floor) # Comment this to try next floor

# New floor
# Uncomment to try

# floor = [[1, 1, 0, 0, 1, 0, 0], # '1' represents dirty and '0' represents clean
#          [0, 0, 0, 1, 0, 0, 0],
#          [0, 1, 1, 1, 1, 1, 1],
#          [0, 1, 0, 1, 0, 1, 0]]

# clean(floor)

