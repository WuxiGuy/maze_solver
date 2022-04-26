'''
Yuhao Hua
2022 April 1
CS5001, Spring 2022
HW 6 -- Maze Solver

This program is to test some functions in maze_solver.py
'''


from maze_solver import input_maze_size, read_maze_file, input_maze


from maze_solver import build_maze_map, exit_point, find_path


import random


def test_input_maze_size():
    '''
    Function: Test function input_maze_size
    Return: True if test passed
            False if test failed
    '''

    print("Test function input_maze_size:")
    failure_time = 0

    # Test with random input
    expected_width = random.randint(3, 120)
    expected_height = random.randint(3, 40)
    input_size = str(expected_width) + ' ' + str(expected_height)
    actual_width, actual_height = input_maze_size(input_size)
    if expected_width != actual_width or expected_height != actual_height:
        print("Test failed!")
        print("Actual:", actual_width, actual_height)
        print("Expected:", expected_width, expected_height)
        return False
    else:
        print("Test passed!")
        return True


def test_read_maze_file():
    '''
    Function: Test function read_maze_file
    Return: True if test passed
            False if test failed
    '''

    print("Test function read_maze_file:")
    failure_time = 0

    # Test 1: input_file = "maze-barrier.txt"
    # Expected: ['13 7', 'XXXXXXXXXXXXX', 'X           X', 'X           X', 
    # 'X           X', 'X  XXXXXXX  X', 'X           X', 'XXXXXXEXXXXXX']
    expected = ['13 7', 'XXXXXXXXXXXXX', 'X           X', 'X           X',
                'X           X', 'X  XXXXXXX  X', 'X           X',
                'XXXXXXEXXXXXX']
    actual = read_maze_file("maze-barrier.txt")
    if expected != actual:
        print("Test failed!")
        print("Actual:", actual)
        print("Expected:", expected)
        failure_time += 1
        return False

    # Test 2: input_file = "maze-just-walls.txt"
    # Expected: ['13 7', 'XXXXXXXXXXXXX', 'X           X', 'X           X',
    # 'X           X', 'X           X', 'X           X', 'XXXXXXEXXXXXX']
    expected = ['13 7', 'XXXXXXXXXXXXX', 'X           X', 'X           X',
                'X           X', 'X           X', 'X           X',
                'XXXXXXEXXXXXX']
    actual = read_maze_file("maze-just-walls.txt")
    if expected != actual:
        print("Test failed!")
        print("Actual:", actual)
        print("Expected:", expected)
        failure_time += 1
        return False

    # Test 3: input_file = "maze-snake.txt"
    # Expected: ['13 7', 'XXXXXXXXXXXXX', 'X           X', 'X XXXXXXXXXXX',
    # 'X           X', 'XXXXXXXXXXX X', 'X           X', 'XEXXXXXXXXXXX']
    expected = ['13 7', 'XXXXXXXXXXXXX', 'X           X', 'X XXXXXXXXXXX',
                'X           X', 'XXXXXXXXXXX X', 'X           X',
                'XEXXXXXXXXXXX']
    actual = read_maze_file("maze-snake.txt")
    if expected != actual:
        print("Test failed!")
        print("Actual:", actual)
        print("Expected:", expected)
        failure_time += 1
        return False

    if failure_time == 0:
        print("Test passed!")
        return True


def test_input_maze():
    '''
    Function: Test function input_maze
    Return: True if test passed
            False if test failed
    '''

    print("Test function input_maze:")
    failure_time = 0

    # Test 1: input = ['13 7', 'XXXXXXXXXXXXX', 'X           X',
    # 'X           X','X           X', 'X  XXXXXXX  X', 'X           X',
    # 'XXXXXXEXXXXXX']
    # Expected: ['XXXXXXXXXXXXX', 'X           X', 'X           X',
    # 'X           X', 'X  XXXXXXX  X', 'X           X', 'XXXXXXEXXXXXX']
    read_maze = ['13 7', 'XXXXXXXXXXXXX', 'X           X', 'X           X',
                 'X           X', 'X  XXXXXXX  X', 'X           X',
                 'XXXXXXEXXXXXX']
    expected = ['XXXXXXXXXXXXX', 'X           X', 'X           X',
                'X           X', 'X  XXXXXXX  X', 'X           X',
                'XXXXXXEXXXXXX']
    actual = input_maze(read_maze)
    if expected != actual:
        print("Test failed!")
        print("Actual:", actual)
        print("Expected:", expected)
        failure_time += 1
        return False

    # Test 2: input = ['13 7', 'XXXXXXXXXXXXX', 'X           X',
    # 'X           X', 'X           X', 'X           X', 'X           X',
    # 'XXXXXXEXXXXXX']
    # Expected: ['XXXXXXXXXXXXX', 'X           X', 'X           X',
    # 'X           X', 'X           X', 'X           X', 'XXXXXXEXXXXXX']
    read_maze = ['13 7', 'XXXXXXXXXXXXX', 'X           X', 'X           X',
                 'X           X', 'X           X', 'X           X',
                 'XXXXXXEXXXXXX']
    expected = ['XXXXXXXXXXXXX', 'X           X', 'X           X',
                'X           X', 'X           X', 'X           X',
                'XXXXXXEXXXXXX']
    actual = input_maze(read_maze)
    if expected != actual:
        print("Test failed!")
        print("Actual:", actual)
        print("Expected:", expected)
        failure_time += 1
        return False

    # Test 3: input = ['13 7', 'XXXXXXXXXXXXX', 'X           X', 'X XXXXXXXXXXX',
    # 'X           X', 'XXXXXXXXXXX X', 'X           X', 'XEXXXXXXXXXXX']
    # Expected: ['XXXXXXXXXXXXX', 'X           X', 'X XXXXXXXXXXX',
    # 'X           X', 'XXXXXXXXXXX X', 'X           X', 'XEXXXXXXXXXXX']
    read_maze = ['13 7', 'XXXXXXXXXXXXX', 'X           X', 'X XXXXXXXXXXX',
                 'X           X', 'XXXXXXXXXXX X', 'X           X',
                 'XEXXXXXXXXXXX']
    expected = ['XXXXXXXXXXXXX', 'X           X', 'X XXXXXXXXXXX',
                'X           X', 'XXXXXXXXXXX X', 'X           X',
                'XEXXXXXXXXXXX']
    actual = input_maze(read_maze)
    if expected != actual:
        print("Test failed!")
        print("Actual:", actual)
        print("Expected:", expected)
        failure_time += 1
        return False

    if failure_time == 0:
        print("Test passed!")
        return True


def test_build_maze_map():
    '''
    Function: Test function build_maze_map
    Return: True if test passed
            False if test failed
    '''

    print("Test function build_maze_map:")

    # Test: input = ['XXX', 'X X', 'XXX']
    # Expected: {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (1, 0): 'X',
    # (1, 1): ' ', (1, 2): 'X', (2, 0): 'X', (2, 1): 'X', (2, 2): 'X'}
    maze = ['XXX', 'X X', 'XXX']
    expected = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (1, 0): 'X',
                (1, 1): ' ', (1, 2): 'X', (2, 0): 'X', (2, 1): 'X',
                (2, 2): 'X'}
    actual = build_maze_map(maze)
    if expected != actual:
        print("Test failed!")
        print("Actual:", actual)
        print("Expected:", expected)
        failure_time += 1
        return False
    else:
        print("Test passed!")
        return True


def test_exit_point():
    '''
    Function: Test function exit_point
    Return: True if test passed
            False if test failed
    '''

    print("Test function exit_point:")
    failure_time = 0

    # Test 1: input = {(0, 0): 'X', (0, 1): 'E', (0, 2): 'X', (1, 0): 'X',
    # (1, 1): 'S', (1, 2): 'X', (2, 0): 'X', (2, 1): 'E', (2, 2): 'X'}
    # Expected: [(0, 1), (2, 1)]
    maze_dictionary = {(0, 0): 'X', (0, 1): 'E', (0, 2): 'X', (1, 0): 'X',
                       (1, 1): ' ', (1, 2): 'X', (2, 0): 'X', (2, 1): 'E',
                       (2, 2): 'X'}
    expected = [(0, 1), (2, 1)]
    actual = exit_point(maze_dictionary)
    if expected != actual:
        print("Test failed!")
        print("Actual:", actual)
        print("Expected:", expected)
        failure_time += 1
        return False

    # Test 2: input = {(0, 0): 'X', (0, 1): 'E', (0, 2): 'X', (1, 0): 'X',
    # (1, 1): 'S', (1, 2): 'X', (2, 0): 'X', (2, 1): 'X', (2, 2): 'X'}
    # Expected: [(0, 1), (2, 1)]
    maze_dictionary = {(0, 0): 'X', (0, 1): 'E', (0, 2): 'X', (1, 0): 'X',
                       (1, 1): ' ', (1, 2): 'X', (2, 0): 'X', (2, 1): 'X',
                       (2, 2): 'X'}
    expected = [(0, 1)]
    actual = exit_point(maze_dictionary)
    if expected != actual:
        print("Test failed!")
        print("Actual:", actual)
        print("Expected:", expected)
        failure_time += 1
        return False


    # Test 3: input = {(0, 0): 'X', (0, 1): 'E', (0, 2): 'X', (1, 0): 'E',
    # (1, 1): 'S', (1, 2): 'X', (2, 0): 'X', (2, 1): 'X', (2, 2): 'X'}
    # Expected: [(0, 1), (1, 0), (2, 1)]
    maze_dictionary = {(0, 0): 'X', (0, 1): 'E', (0, 2): 'X', (1, 0): 'E',
                       (1, 1): ' ', (1, 2): 'X', (2, 0): 'X', (2, 1): 'E',
                       (2, 2): 'X'}
    expected = [(0, 1), (1, 0), (2, 1)]
    actual = exit_point(maze_dictionary)
    if expected != actual:
        print("Test failed!")
        print("Actual:", actual)
        print("Expected:", expected)
        failure_time += 1
        return False


    if failure_time == 0:
        print("Test passed!")
        return True


def test_find_path():
    '''
    Function: Test function exit_point
    Return: True if test passed
            False if test failed
    '''

    print("Test function exit_point:")
    failure_time = 0

    # Test 1: input = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X',
    # (1, 0): 'X', (1, 1): 'S', (1, 2): 'X', (1, 3): 'E',
    # (2, 0): 'X', (2, 1): 'X', (2, 2): 'X', (2, 3): 'X'}
    # Expected_find_exit = (1, 3)
    # Expected_movement = {(1, 2): 'L', (1, 3): 'L'}
    # Expected_distance = 2
    maze_dictionary = {(0, 0): 'X', (0, 1): 'X', (0, 2): 'X', (0, 3): 'X',
                       (1, 0): 'X', (1, 1): 'S', (1, 2): 'X', (1, 3): 'E',
                       (2, 0): 'X', (2, 1): 'X', (2, 2): 'X', (2, 3): 'X'}
    beginning = (1, 1)
    maze_exit = [(1, 3)]
    expected_find_exit = (1, 3)
    expected_movement = {(1, 2): 'L', (1, 3): 'L'}
    expected_distance = 2
    actual_find_exit, actual_movement, actual_distance = \
                      find_path(maze_dictionary, beginning, maze_exit)
    if expected_find_exit != actual_find_exit or expected_movement != \
       actual_movement or expected_distance != actual_distance:
        print("Test failed!")
        print("Actual:", actual_find_exit, actual_movement, actual_distance,
              sep='\n')
        print("Expected:", expected_find_exit, expected_movement,
              expected_distance, sep='\n')
        return False
    else:
        print("Test passed!")
        return True


def main():
    print("Let's test all functions:")
    failure_time = 0

    if test_input_maze_size() is False:
        failure_time += 1
    if test_read_maze_file() is False:
        failure_time += 1
    if test_input_maze() is False:
        failure_time += 1
    if test_build_maze_map() is False:
        failure_time += 1
    if test_exit_point() is False:
        failure_time += 1

    if failure_time == 0:
        print("Tests all passed!")
    else:
        print("Something was wrong")


if __name__ == "__main__":
    main()
