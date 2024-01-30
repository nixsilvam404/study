# "A chess queen can move any number of squares horizontally, 
# vertically, or diagonally. Given two different squares on a 
# chessboard, determine if the queen can move from the first square 
# to the second in one move. For simplicity, you can ignore the case 
# where the given squares are the same.

# Input Format

# The program receives four numbers from 1 to 8 each, specifying 
# the column number and the row number first for the first square, 
# then for the second square.

# Output Format

# The program should output True if the queen can move from the 
# first square to the second in one move. Otherwise, output False."



def queen_turn(s: list) -> bool:
 
    if s[2] - s[0] == s[3] - s[1] \
    or s[0] == s[2] and s[1] != s[3] \
    or s[0] != s[2] and s[1] == s[3]: # Check for diagonnaly,
        # vertically and horizontally turn 
        return True
    else:
        return False
    

print(queen_turn([1, 1, 8, 8]))
print(queen_turn([1, 1, 8, 1]))
print(queen_turn([5, 5, 7, 4]))
