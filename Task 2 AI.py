import math
import random

WIN_COMBINATIONS = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def print_board(board):
    def cell(i):
        return board[i] if board[i] is not None else str(i+1)
    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()

def check_winner(board):
    for a,b,c in WIN_COMBINATIONS:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    if all(cell is not None for cell in board):
        return "Draw"
    return None

def available_moves(board):
    return [i for i,cell in enumerate(board) if cell is None]

def minimax(board, ai_player, human_player, maximizing, alpha, beta):
    result = check_winner(board)
    if result == ai_player:
        return (1, None)
    elif result == human_player:
        return (-1, None)
    elif result == "Draw":
        return (0, None)

    if maximizing:
        best_score = -math.inf
        best_move = None
        for move in available_moves(board):
            board[move] = ai_player
            score, _ = minimax(board, ai_player, human_player, False, alpha, beta)
            board[move] = None
            if score > best_score:
                best_score, best_move = score, move
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return (best_score, best_move)
    else:
        best_score = math.inf
        best_move = None
        for move in available_moves(board):
            board[move] = human_player
            score, _ = minimax(board, ai_player, human_player, True, alpha, beta)
            board[move] = None
            if score < best_score:
                best_score, best_move = score, move
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return (best_score, best_move)

def ai_move(board, ai_player, human_player):
    # If board empty, choose a corner or center randomly for variety
    if all(cell is None for cell in board):
        return random.choice([0,2,4,6,8])
    _, move = minimax(board, ai_player, human_player, True, -math.inf, math.inf)
    return move

def human_turn(board, human_player):
    while True:
        try:
            choice = int(input(f"Enter your move (1-9): ")) - 1
            if choice < 0 or choice > 8:
                print("Choose a number from 1 to 9.")
            elif board[choice] is not None:
                print("That cell is already taken.")
            else:
                return choice
        except ValueError:
            print("Please enter a valid number.")

def play():
    print("Tic-Tac-Toe (Human vs AI)")
    board = [None]*9

    human_player = ""
    while human_player not in ("X","O"):
        human_player = input("Pick your symbol (X/O): ").upper()
    ai_player = "O" if human_player == "X" else "X"

    first = ""
    while first not in ("H","A"):
        first = input("Who plays first? (H for Human / A for AI): ").upper()

    current = "H" if first == "H" else "A"
    print_board(board)

    while True:
        if current == "H":
            move = human_turn(board, human_player)
            board[move] = human_player
        else:
            print("AI is thinking...")
            move = ai_move(board, ai_player, human_player)
            board[move] = ai_player
            print(f"AI chooses position {move+1}")

        print_board(board)
        winner = check_winner(board)
        if winner is not None:
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        current = "A" if current == "H" else "H"

if __name__ == "__main__":
    play()
