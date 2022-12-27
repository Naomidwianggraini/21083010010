def main():
# The main function
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2) # The function that starts the game is also in here.
    


def intro():
# This function introduces the rules of the game Tic Tac Toe
    print("   ")
    print("================================================================================")
    print(" __    __                                    _______   ")
    print("|  |  |  |ELLO!, Selamat datang dipermainan |__   __|        ")
    print("|  |__|  |                                     | |   ic          ")
    print("|   __   |                                     | |   ac       ")
    print("|  |  |  |                                     |_|   oe GAME!!!        ")
    print("|__|  |__|                                                               ")
    print("                   ")
    print("================================================================================")
    print("\n")
    print("Deskripsi Permainan : ")
    print("Terdapat pemain 1 dan pemain 2, Pemain dipersilahkan  memilih X atau O sebagai pertanda disebuah "
          "kotak yang berdimensi 3*3. pemain dinyatakan menang jika bisa membuat garis di"
          "tiga keadaan yaitu horizontal, vertical, atau  diagonal.")
    print("\n")
    input("enter to continue.")
    print("\n")


def create_grid():
# This function creates a blank playboard
    print("Berikut papann permainan: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board

def sym():
# This function decides the players' symbols
    symbol_1 = input("Pemain 1, silahkan untuk memilih  X atau O? ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Pemain 2, kamu adalah O. ")
    else:
        symbol_2 = "X"
        print("Pemain 2, kamu adalah X. ")
    input("enter to continue.")
    print("\n")
    return (symbol_1, symbol_2)



def startGamming(board, symbol_1, symbol_2, count):
# This function starts the game.

    # Decides the turn
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Pemain "+ player + ", ini giliran kamu. ")
    row = int(input("[Pilih baris:"
                    "[baris atas: enter 0, baris tengah: enter 1, baris bawah: enter 2]:"))
    column = int(input("PIlih kolom:"
                       "[kolom kiri: enter 0, kolom tengah: enter 1, kolom kanan: enter 2]"))


    # Check if players' selection is out of range
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Pilih baris[baris atas:"
                        "[enter 0, baris tengah: enter 1, baris bawah: enter 2]:"))
        column = int(input("Pilih kolom:"
                           "[Kolom kiri: enter 0, kolom tengah: enter 1, kolom kanan: enter 2]"))

        # Check if the square is already filled
    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Pilih baris[baris atas:"
                        "[enter 0, baris tengah: enter 1, baris bawah: enter 2]:"))
        column = int(input("Pilih kolom:"
                            "[Kolom kiri: enter 0, kolom tengah: enter 1, kolom kanan: enter 2]"))    
        
    # Locates player's symbol on the board
    if player == symbol_1:
        board[row][column] = symbol_1
            
    else:
        board[row][column] = symbol_2
    
    return (board)



def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
# This function check if the board is full
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)
        
        if count == 9:
            print("Papan permainan penuh. Game over.")
            if winner == True:
                print("There is a tie. ")

        # Check if here is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game over.")
        
    # This is function gives a report 
    report(count, winner, symbol_1, symbol_2)



def outOfBoard(row, column):
# This function tells the players that their selection is out of range
    print("Out of boarder. Pick another one. ")
    
    

def printPretty(board):
# This function prints the board nice!
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board



def isWinner(board, symbol_1, symbol_2, count):
# This function checks if any winner is winning
    winner = True
    # Check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Pemain " + symbol_1 + ", Kamu menang!")
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Pemain " + symbol_2 + ", Kamu menang!")
            
            
    # Check the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Pemain " + symbol_1 + ", kamu menang!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Pemain " + symbol_2 + ", Kamu menang!")

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Pemain " + symbol_1 + ", Kamu menang!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Pemain " + symbol_2 + ", Kamu menang!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Pemain " + symbol_1 + ", Kamu menang!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Pemain " + symbol_2 + ", Kamu menang!")

    return winner
    


def illegal(board, symbol_1, symbol_2, row, column):
    print("kotak sudah terisi, pilih kotak yang lain.")

    
def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Enter untuk melihat kesimpulan. ")
    if (winner == False) and (count % 2 == 1 ):
        print("Pemenang : Pemain " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Pemenang : Pemain " + symbol_2 + ".")
    else:
        print("Thre is a Tie. ")

# Call Main
main()
