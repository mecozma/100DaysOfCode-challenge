""" Grid traveler challenge. Find the path in a m X n grid."""


def grid_traveler(m, n, memo={}):
    """
    The grid_traveler function takes the coordinates of a map and returns all
    paths in a grid.
        Parameters:
            m (int): A decimal integer.
            n (int): A decimal integer.
        Returns:
            memo[key] (int): The number of paths.
    """
    key = str(m) + "," + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n-1, memo)
    return memo[key]


print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
