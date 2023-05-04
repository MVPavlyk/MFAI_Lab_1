import random
import math

N = 20  # встановлюємо розмір дошки


def copy_board(source, dest):
    for i in range(N):
        for j in range(N):
            dest[i][j] = source[i][j]


def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()


def initialize_board():
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        board[i][i] = 1
    return board


def generate_neighbor(board):
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    neighbor = [row[:] for row in board]
    neighbor[i][j] = 1
    for k in range(N):
        if k != j:
            neighbor[i][k] = 0
    return neighbor


def calculate_score(board):
    row_counts = [0] * N
    col_counts = [0] * N
    diag1_counts = [0] * (2 * N - 1)
    diag2_counts = [0] * (2 * N - 1)
    score = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                row_counts[i] += 1
                col_counts[j] += 1
                diag1_counts[i + j] += 1
                diag2_counts[N - 1 - i + j] += 1
    for i in range(N):
        score += (row_counts[i] * (row_counts[i] - 1)) // 2
        score += (col_counts[i] * (col_counts[i] - 1)) // 2
    for i in range(2 * N - 1):
        score += (diag1_counts[i] * (diag1_counts[i] - 1)) // 2
        score += (diag2_counts[i] * (diag2_counts[i] - 1)) // 2
    return score


def main():
    board = initialize_board()
    print("Значення N = ", N)
    print("Початкова розстановка:")
    print_board(board)
    T = 100
    coolingRate = 0.0001
    best_solution = [row[:] for row in board]
    best_score = calculate_score(best_solution)
    while T > 0.1:
        neighbor = generate_neighbor(board)
        neighbor_score = calculate_score(neighbor)
        delta = neighbor_score - best_score
        if delta < 0:
            board = [row[:] for row in neighbor]
            best_score = neighbor_score
            if best_score < calculate_score(best_solution):
                copy_board(board, best_solution)
        elif math.exp(-delta / T) > random.random():
            board = [row[:] for row in neighbor]
        T *= 1 - coolingRate
    print("Результат алгоритму:")
    print_board(best_solution)


main()
