"""
A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
"""

def knights_tour(n: int) -> int:

    visited = [[0] * n] * n

    return start_browsing(n, visited, 0, 0, 1)

def start_browsing(n, visited, i, j, cnt):

    if cnt == n*n:
        return 1

    if i < 0 or j < 0:
        return 0

    if i >= n or j >= n:
        return 0

    visited[i, j] = 1

    paths = start_browsing(n, visited, i , j - 1, cnt)
    paths += start_browsing(n, visited, i , j + 1, cnt)
    paths += start_browsing(n, visited, i - 1, j + 1, cnt)
    paths += start_browsing(n, visited, i + 1 , j, cnt)

    return paths

