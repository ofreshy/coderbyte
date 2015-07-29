"""
Using the Python language,
have the function NoughtsDeterminer(strArr) take the strArr parameter being passed
which will be an array of size eleven.
The array will take the shape of a Tic-tac-toe board with
spaces strArr[3] and strArr[7] being the separators ("<>")
 between the rows,
 and the rest of the spaces will be either "X", "O", or "-" which signifies an empty space.
  So for example strArr may be
  ["X","O","-","<>","-","O","-","<>","O","X","-"].
   This is a Tic-tac-toe board with each row separated double arrows ("<>").
    Your program should output the space in the array by which any player could win by putting down either an "X" or "O".
    In the array above, the output should be 2 because if an "O" is placed in strArr[2] then one of the players wins.
    Each board will only have one solution for a win, not multiple wins.
    You output should never be 3 or 7 because those are the separator spaces.


"""

wins = [
    (0,1,2), (4,5,6), (8,9,10), #rows
    (0,4,8), (1,5,9), (2,6,10), #cols
    (0,5,10), (2,5,8) #diags
]
def NoughtsDeterminer(strArr):
    for win in wins:
        seq = [strArr[i] for i in win]
        if seq.count('-') == 1 and (seq.count('X') == 2 or seq.count('O') == 2):
            o = win[seq.index('-')]
            return o
    return None


print NoughtsDeterminer(["X","O","-","<>","-","O","-","<>","O","X","-"])
print NoughtsDeterminer(["X","-","O","<>","-","-","O","<>","-","-","X"])
print NoughtsDeterminer(["X","O","X","<>","-","O","O","<>","X","X","O"])