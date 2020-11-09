# Given 4 x 4 grid(floor), agent starts in random position

def clean(floor, row, col):
    m = 4
    n = 4
    no_of_tiles = m * n

    tiles_checked = 0

    # GO to starting pos in second row
    while col != 0:
        print_floor(floor, row, col)
        print('---------------')
        col -= 1

    
    while row != 1:
        print_floor(floor, row, col)
        print('---------------')
        if row > 1:
            row -= 1
        else:
            row += 1
    
    # Clean until 3 rows are cleaned 
    while tiles_checked < 3*4: # 3 rows
        # Current position
        print_floor(floor, row, col)

        # Suck if dirty
        if floor[row][col] == 1:
            floor[row][col] = 0
            print('Sucked the dirt')
        else:
            print('Already Clean')
        
    
        # Next tile
        if row % 2 == 0:
            if 0 < col:
                col -= 1
            else:
                row += 1        
              
        
        else:
            if col < m-1:
                col += 1
            else:
                row += 1 
            
        
        tiles_checked += 1
        print('---------------')
    
    print('Cleaned!!!')
        

        
def print_floor(floor, row, col):
    temp = floor[row][col]
    floor[row][col] = 'VC'
    for x in floor:
        print(x)
    
    floor[row][col] = temp



floor = [[1, 0, 0, 0], # '1' represents dirty and '0' represents clean
         [0, 1, 0, 1],
         [1, 0, 1, 1],
         [0, 0, 0, 1]]
# Random Starting point
row, col = 2, 1
clean(floor, row, col) 



