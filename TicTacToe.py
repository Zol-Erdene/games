import random
def tttGame():
    print("============================================")
    print("Tic Tac Toe")
    print("============================================")
    board = newBoard()
    print("Make sure your input consists of only 2 integers: row then column.")
    printBoard(board)
    runGame = True
    while runGame:
        # Player's turn
        while True:
            try:
                inputStr = input("Make your selection: ").replace(" ", "")
                r = int(inputStr[0])
                c = int(inputStr[1])

                if r < 1 or r > 3 or c < 1 or c > 3:
                    print("Values can only be between 1 and 3")
                    continue

                if not isEmpty(board, r, c):
                    print("Chosen cell is already filled.")
                    continue

                modifyBoard(board, r, c, "X")
            except ValueError:
                print("Please only enter integers")
            except:
                print("Invalid input")
            else:
                break
        printBoard(board)

        #Check if for draws
        board_full = True
        for row in range(len(board)):
            for col in range(len(board[row])):
                if isEmpty(board, row + 1, col + 1): 
                    board_full = False
                    break
        if board_full:
            print("Draw!")
            runGame = False
            break

        # Check for winners
        if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") or (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
            print("You win!")
            if input("Another round? ").lower() == "y":
                board = newBoard()
                printBoard(board)
                continue
            else:
                runGame = False
                break
        elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O") or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
            print("You lose!")
            if input("Another round? ").lower() == "y":
                board = newBoard()
                printBoard(board)
                continue
            else:
                runGame = False
                break
            
        # CPU's turn
        while True:
            cpur = random.randrange(1, 4)
            cpuc = random.randrange(1, 4)
            if isEmpty(board, cpur, cpuc):
                modifyBoard(board, cpur, cpuc, "O")
                break

        printBoard(board)
            

def printBoard(b:list):
    print(" _ _ _")
    for row in range(len(b)):
        for col in range(len(b[row])):
            print(f"|{b[row][col]}", end = "")
        print("|")

def modifyBoard(b:list, r:int, c:int, val:str):
    b[r-1][c-1] = val

def isEmpty(b:list, r:int, c:int) -> bool:
    return b[r-1][c-1] == "_"

def newBoard():
    b = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]
    return b


if __name__ == "__main__":
    tttGame()