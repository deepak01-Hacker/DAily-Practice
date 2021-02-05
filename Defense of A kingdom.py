"""
DEFKIN - Defense of a Kingdom
no tags 

Theodore implements a new strategy game “Defense of a Kingdom”. On each level a player defends the Kingdom that is represented by a rectangular grid of cells. The player builds crossbow towers in some cells of the grid. The tower defends all the cells in the same row and the same column. No two towers share a row or a column.

The penalty of the position is the number of cells in the largest undefended rectangle. For example, the position shown on the picture has penalty 12.

This position has a penalty of 12.

Help Theodore write a program that calculates the penalty of the given position.
Input

The first line of the input file contains the number of test cases.

Each test case consists of a line with three integer numbers: w — width of the grid, h — height of the grid and n — number of crossbow towers (1 ≤ w, h ≤ 40 000; 0 ≤ n ≤ min(w, h)).

Each of the following n lines contains two integer numbers xi and yi — the coordinates of the cell occupied by a tower (1 ≤ xi ≤ w; 1 ≤ yi ≤ h).
Output

For each test case, output a single integer number — the number of cells in the largest rectangle that is not defended by the towers.

"""


def defenseOfKingdom(arr,x,y,n):
    arr_x = [arr[i][0] for i in range(n)]
    arr_y = [arr[i][1] for i in range(n)]

    arr_x.sort()
    arr_y.sort()

    arr_x.insert(0,0)
    arr_y.insert(0,0)
    arr_x.append(x)
    arr_y.append(y)

    x_mac,y_mac = 0,0

    for i in range(1,n+2):
        x_mac = max(x_mac,arr_x[i]-arr_x[i-1]-1)
        y_mac = max(y_mac,arr_y[i]-arr_y[i-1]-1)

    return x_mac*y_mac
