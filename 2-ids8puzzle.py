# 8 puzzle ids implementation

# Iterative Deepening Depth First Search
def iddfs(src,target,depth):
    for limit in range(1, depth+1):                  # From 1 to given Depth
        visited_states=[]                            # Memory to Check if site is visited in given Depth "limit"
        if dfs(src,target,limit,visited_states):
            return limit
        print(limit, False)                              # Returns True if Target is reached in given depth
    return False                                     


def dfs(src,target,limit,visited_states):            # Depth first search in search of target
    if src == target:
        print(target) 
        return True

    if limit <= 0 :                                  # Recursion Base Case "number of levels left" becomes 0, your depth limit is reached
        return False

    visited_states.append(src)                       # Add current site to already visited sites, so we dont perform "src == target" again on the same site

    adj = possible_moves(src,visited_states)         # Find possible slides up, down, left right to current empty site

    for move in adj:                                 # For all possible adj(adjacent) moves
        if dfs(move,target,limit-1,visited_states):  # if the "next depth"('limit - 1' till final depth is reached '0') achives the desired target
            return True                              # True if desired target achieved before limit becomes '0'(depth limit is reached) 
    return False


def possible_moves(state,visited_states):            
    b = state.index(-1)                              # Find index of empty spot
    d=[]                                             #'d' : down, 'u': up ..... directions
    pos_moves=[]                                     # if dir is possible to go then add to state to move

    if b<=5:                                         # to go down, empty spot should be in the first 2 rows
        d.append('d')

    if b>=3 :                                        # to go up, empty spots should be in the bottom 2 rows
        d.append('u')

    if b%3 > 0:                                      # to go left, empty spots should be in the right most 2 columns
        d.append('l')

    if b%3 < 2:                                      # to go right, empty spots should be in the left most 2 columns
        d.append('r')

    for i in d:                                      # for i in "all possble directions"

        temp = gen(state, i, b)                      # generate the state if slide empty spot to one of the directions
        
        if temp not in visited_states:               # only check of "src == target" if this temp state has not been checked
            pos_moves.append(temp)                   # add temp to possible moves to check if 
    
    return pos_moves                                 # return array of all possible moves


def gen(state, m, b):                                # m(move) is direction to slide, b(blank) is index of empty spot
    temp=state.copy()                                # create a copy of current state to test the move

    if m == 'l':                                     # if move is to slide empty spot to the left
        temp[b], temp[b-1] = temp[b-1], temp[b]      # switch postions so a = b and b = a

    if m == 'r':                                     # if move is to slide empty spot to the right
        temp[b], temp[b+1] = temp[b+1], temp[b]

    if m == 'u':                                     # if move is to slide empty spot to the top
        temp[b], temp[b-3] = temp[b-3], temp[b]

    if m =='d':                                      # if move is to slide empty spot to the bottom
        temp[b], temp[b+3] = temp[b+3], temp[b]
    
    return temp                                      # return new state with tested move to later check if "src == target"

          






src=[1,2,3,
    -1,4,5,
     6,7,8]
#target=[1,2,3,4,5,-1,6,7,8]         # given target requires depth of 2 to achieve result
target=[1,2,3,
        6,4,5,
        -1,7,8]       # Only one position is changed(to Test)

depth = 1
print(iddfs(src, target, depth)) # Try with 1 and 2 depth

#Maximum Change 
# An Experiemnt I did to try and find the maximum required depth assuming 
# that this was the biggest possible change from src to target

### Uncomment to try
src = [1, 2, 3, 4, 5, 6, 7, 8, -1]
target = [-1, 8, 7, 6, 5, 4, 3, 2, 1]

print(iddfs(src, target, 100))


        
