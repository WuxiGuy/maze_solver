'''
Yuhao Hua
2022 April 1
CS5001, Spring 2022
HW 6 -- Maze Solver

This program is to input a maze which can be created by user or
read from a maze file. User can choose a position to start in the maze.
Then the program will find out the shortest path to the nearest exit.
'''


import os


def input_maze_size(input_size):
    '''
    Function: 
        ask user to input the width and height of the maze
        seperated by white space.
    Parameter:
        input_size: a string starts with an integer between 3 and 120
                    followed by a white space, and ends with 
                    an integer between 3 and 40.
    Return: 
        width: an integer between 3 and 120
        height: an integer between 3 and 40
    '''

    size = input_size.split()

    while len(size) != 2:
        print(ValueError, "Please only enter two number.")
        input_size = input("Please try again:")
        size = input_size.split()
    while size[0].isdigit() is False or size[1].isdigit() is False:
        print(ValueError, "Width and height should be integers.")
        input_size = input("Please try again:")
        size = input_size.split()
    width, height = int(size[0]), int(size[1])
    while not (3 <= width <= 120 and 3 <= height <= 40):
        print(ValueError, "The value of width or length is out of range.")
        input_size = input("Please try again:")
        size = input_size.split()
    width, height = int(size[0]), int(size[1])

    return width, height


def diy_maze(width, height):
    '''
    Function: 
        Ask user to creat a maze line by line based on the size determined
        by the input width and height of the maze. User can use 'X' for
        boundaries and walls inside the maze, 'E' for exit which can only
        be used on boundaries, white space for space in the maze.
    Parameters:
        width: an integer for the width of the maze
        height: an integer for the height of the maze
    Return:
        lines_list: a list of strings. Each string store a line of maze.
    '''

    print("Let's draw a maze by hand with \'X\' as walls,",
          "\'E\' as exit and \' \' for space. The width of the maze is",
          width, "and the height of the maze is:", height)
    lines_list = []

    # draw the first line
    maze_line = str(input("Let's draw line 1:\n"))
    while len(maze_line) != width:
        print(ValueError, "The width of the line isn't correct.")
        maze_line = str(input("Please try again:\n"))
    for item in range(len(maze_line)):
        while maze_line[item] not in ['E', 'X']:
            print(ValueError, "The wall should only be built with \'X\'",
                  "and \'E\'.\n")
            maze_line = str(input("Please try again:\n"))
    lines_list.append(maze_line)

    # draw the second line to height - 1 line
    for line in range(2, height):
        print("Let's draw line", str(line) + ":")
        maze_line = str(input())
        while len(maze_line) != width:
            print(ValueError, "The width of the line isn't correct.")
            maze_line = input("Please try again:")
        while maze_line[0] not in ['X', 'E']:
            print(ValueError, "Something wrong with the wall.")
            maze_line = input("Please try again:")
        while maze_line[width - 1] not in ['X', 'E']:
            print(ValueError, "Something wrong with the wall.")
            maze_line = input("Please try again:")
        for count in range(1, width - 1):
            while maze_line[count] not in ['X', ' ']:
                print(ValueError, "Something wrong within the maze.")
                maze_line = str(input("Please try again:\n"))
        lines_list.append(maze_line)

    # draw the last line
    print("Let's draw the last line:")
    maze_line = str(input())
    while len(maze_line) != width:
        print(ValueError, "The width of the line isn't correct.")
        maze_line = str(input("Please try again:\n"))
    for item in maze_line:
        while item not in ['E', 'X']:
            print(ValueError, "The wall should only be built with \'X\'",
                  "and \'E\'.\n")
            maze_line = str(input("Please try again:\n"))
    lines_list.append(maze_line)

    return lines_list


def read_maze_file():
    '''
    Function:
        Ask user to input the name of a maze file.
        Read and store each line as a string from a maze file to a list.
    Parameters:
    Return:
        lines_list: a list of strings. Each string contains a line of
            the maze file.
    '''

    try:
        file_name = input("Please enter the file name of a maze:")
        input_file = open(file_name, 'r')
        file_data = input_file.readlines()
        input_file.close()

        lines_list = []
        for line in file_data:
            line_updated = line.replace('\n', '')
            lines_list.append(line_updated)
        # a string contains width and height
        size_line = lines_list[0]
        return lines_list, size_line

    except FileNotFoundError or PermissionError or OSError:
        print(ValueError, "Error occurred reading the maze file. Try again")
        lines_list, size_line = read_maze_file()
        return lines_list, size_line


def input_maze(read_maze):
    '''
    Function: 
        Input a list of strings called read_maze storing the lines of
        a maze file. Then remove '\n' from all the strings in the list.
    Parameter:
        read_maze: a list of strings. Each string contains a line of
            the maze file in order.
    Return:
        lines_list: a list of strings which copied from read_maze with
            all '\n' have been removed.
    '''

    if not isinstance(read_maze, list):
        raise TypeError("It should be a list as a parameter.")

    lines_list = []
    for line in range(1, len(read_maze)):
        lines_list.append(read_maze[line])

    return lines_list


def build_maze_map(maze):
    '''
    Function:
        Input a list of string storing the information of a maze.
        Creat a dictionary which use tuples as keys to represent the
        locations(x, y) in the maze. Each location represents a part of
        the maze which is 'X', or 'E' or ' '.
    Parameter: 
        maze: a list of string. Each string is a row of the maze in order.
    Return:
        maze_dictionary: a dictionary stores information of the maze
            keys: locations(tuple) in the maze
            values: the corresponding part(string) of maze
    '''

    if not isinstance(maze, list):
        print(TypeError, "It should be a list as a parameter.")
        maze = input("Please enter a vaild maze:")
    maze_dictionary = {}
    for line in range(len(maze)):
        for count in range(len(maze[line])):
            position = (line, count)
            maze_dictionary[position] = maze[line][count]

    return maze_dictionary


def start_point(maze_dictionary, width, height):
    '''
    Function:
        User chooses a start position inside the maze. Then print
        the maze including the start position.
    Parameter:
        maze_dictionary: a dictionary stores information of the maze
            keys: locations(tuple) in the maze
            values: the corresponding part(string) of maze
        width: an integer
        height: an integer
    Return:
        beginning: a tuple for the start position
        maze_dictionary: a dictionary which is also used as parameter
            but the information of the start position has been updated
    '''

    print("The top left corner of the maze is (0, 0).\n",
          "Please select a position(x, y) in the maze to start.\n",
          "Note:\n",
          "x represent line which should be an integer between 1 to ",
          height - 2, " .\n",
          "y represent column which should be an integer between 1 to ",
          width - 2, " .", sep='')

    value_x = input("Please input x:")
    value_y = input("Plese input y:")

    while not value_x.isdigit() & value_y.isdigit():
        print(TypeError, "x and y should be integers.")
        value_x = input("Please input x:")
        value_y = input("Plese input y:")

    while 1 <= int(value_x) <= height - 2 is False:
        print(ValueError, "x are out of range.")
        value_x = input("Please input x:")

    while 1 <= int(value_y) <= width - 2 is False:
        print(ValueError, "y are out of range.")
        value_y = input("Plese input y:")

    beginning = (int(value_x), int(value_y))
    while maze_dictionary[beginning] != ' ':
        print("This is not a blank space in maze.\n",
              "Please select another position.", sep='')
        value_x = input("Please input x:")
        value_y = input("Plese input y:")
        beginning = (int(value_x), int(value_y))

    maze_dictionary[beginning] = 'S'

    updated_maze = []
    for x in range(height):
        maze_line = ''
        for y in range(width):
            maze_line += maze_dictionary[(x, y)]
        updated_maze.append(maze_line)
    for line in updated_maze:
        print(line)

    return beginning, maze_dictionary


def exit_point(maze_dictionary):
    '''
    Function: 
        Find the locations of exit(s) of the maze by searching the keys
        with values 'E' in the dictionary which stores the locations
        of parts of maze
    Parameter:
        maze_dictionary: a dictionary stores information of the maze
                including start position
            keys: locations(tuple) in the maze
            values: the corresponding part(string) of maze
    Return:
        maze_exit: a list of tuples which represent the location(s)
            of exit(s)
    '''

    maze_exit = []
    for key in maze_dictionary.keys():
        if maze_dictionary[key] == "E":
            maze_exit.append(key)
    return maze_exit


def find_path(maze_dictionary, beginning, maze_exit):
    '''
    Function:
        Find the shortest path from the start position to the nearest exit
        and calculate the distance.
    Parameters:
        maze_dictionary: a dictionary stores the locations
            and the corresponding parts of the maze.
        beginning: a tuple of the start position
        maze_exit: a list of tuples which are locations of exit
    Returns:
        find_exit: a tuple of the location of the nearest exit
        movement: a dictionary
            keys: tuples which represent the locations of all steps
                that the program has tried
            values: one string for each key which is one character of
                the direction(U, D, R, L) that can be used by the function
                draw_shortest_path to find the way back from exit to 
                the start position
    '''

    # store all the positons that the point have moved and the direction
    movement = {}
    # the beginning point(s) of each movement step
    previous_positions = [beginning]
    # the positions that the point(s) moved to in current step
    current_positions = []
    # store the distance from the beginning
    distance = 0

    for item in maze_exit:
        while item not in movement.keys():
            for position in previous_positions:
                # move to the right position
                if (position[0], position[1] + 1) not in movement.keys():
                    if maze_dictionary[position[0], position[1] + 1] == ' ':
                        current_positions.append((position[0],
                                                  position[1] + 1))
                        movement[(position[0], position[1] + 1)] = 'L'
                    elif maze_dictionary[position[0], position[1] + 1] == 'E':
                        find_exit = (position[0], position[1] + 1)
                        current_positions.append((position[0],
                                                  position[1] + 1))
                        movement[(position[0], position[1] + 1)] = 'L'
                        distance += 1
                        return find_exit, movement, distance

                # move to the left positon
                if (position[0], position[1] - 1) not in movement.keys():
                    if maze_dictionary[position[0], position[1] - 1] == ' ':
                        current_positions.append((position[0],
                                                  position[1] - 1))
                        movement[(position[0], position[1] - 1)] = 'R'
                    elif maze_dictionary[position[0], position[1] - 1] == 'E':
                        find_exit = (position[0], position[1] - 1)
                        current_positions.append((position[0],
                                                  position[1] - 1))
                        movement[(position[0], position[1] - 1)] = 'R'
                        distance += 1
                        return find_exit, movement, distance

                # move to the up position
                if (position[0] + 1, position[1]) not in movement.keys():
                    if maze_dictionary[position[0] + 1, position[1]] == ' ':
                        current_positions.append((position[0] + 1,
                                                  position[1]))
                        movement[(position[0] + 1, position[1])] = 'U'
                    elif maze_dictionary[position[0] + 1, position[1]] == 'E':
                        find_exit = (position[0] + 1, position[1])
                        current_positions.append((position[0] + 1,
                                                  position[1]))
                        movement[(position[0] + 1, position[1])] = 'U'
                        distance += 1
                        return find_exit, movement, distance

                # move to the down position
                if (position[0] - 1, position[1]) not in movement.keys():
                    if maze_dictionary[position[0] - 1, position[1]] == ' ':
                        current_positions.append((position[0] - 1,
                                                  position[1]))
                        movement[(position[0] - 1, position[1])] = 'D'
                    elif maze_dictionary[position[0] - 1, position[1]] == 'E':
                        find_exit = (position[0] - 1, position[1])
                        current_positions.append((position[0] - 1,
                                                  position[1]))
                        movement[(position[0] - 1, position[1])] = 'D'
                        distance += 1
                        return find_exit, movement, distance
            distance += 1
            previous_positions = current_positions
            current_positions = []


def draw_shortest_path(find_exit, movement, beginning,
                       maze_dictionary, width, height):
    '''
    Function: 
        Draw the shortest from the nearest exit to the start position.
        Then print out the maze.
    Parameter:
        find_exit: a tuple of the location of the nearest exit
        movement: a dictionary stores the information of the positions
            that the program walks through to find the shortest path
        beginning: a tuple of the start position
        maze_dictionary: a dictionary stores the locations
            and the corresponding parts of the maze
        width: an integer of the width of the maze
        height: an integer of the height of the maze
    Return:
    '''

    path = find_exit

    while path != beginning:
        if movement[(path[0], path[1])] == 'L':
            path = (path[0], path[1] - 1)
            if path != beginning:
                maze_dictionary[(path[0], path[1])] = '*'
        elif movement[(path[0], path[1])] == 'R':
            path = (path[0], path[1] + 1)
            if path != beginning:
                maze_dictionary[(path[0], path[1])] = '*'
        elif movement[(path[0], path[1])] == 'U':
            path = (path[0] - 1, path[1])
            if path != beginning:
                maze_dictionary[(path[0], path[1])] = '*'
        elif movement[(path[0], path[1])] == 'D':
            path = (path[0] + 1, path[1])
            if path != beginning:
                maze_dictionary[(path[0], path[1])] = '*'
    maze_dictionary[path] = 'S'

    updated_maze = []
    for x in range(height):
        maze_line = ''
        for y in range(width):
            maze_line += maze_dictionary[(x, y)]
        updated_maze.append(maze_line)

    print("Do you want to print out solved maze?")
    print("Please enter the number\n1: print\n2: do not print")
    command = input()
    while not command.isdigit():
        print(TypeError, "Please enter an integer 1 or 2.")
        command = input("Try again:")
    if int(command) == 1:
        for line in updated_maze:
            print(line)
        return
    elif int(command) == 2:
        return


def main():
    # Ask user to make the desicion
    options = "1. Creat your own maze.\n2. Use a ready maze in file.\n" + \
              "3. Quit the game."

    print(options)
    command = input("Please select an option by input an integer:")
    while not command.isdigit():
        print(TypeError, "Please input a integer between 1 to 3.")
        print(options)
        command = input("Please select an option by input an integer:")
    while int(command) < 1 or int(command) > 3:
        print(ValueError, "Please choose a valid option.")
        print(options)
        command = input("Please select an option by input an integer:")

    while int(command) != 3:
        command = int(command)
        # User can draw the maze by hand typing
        if command == 1:
            print("Please determine the width(3-120) and the height(3-40)\n",
                  "of the maze(seperated by a whitespace):", sep='', end='')
            # a sting contains width and height
            input_size = input()
            # get the width and height from the string above
            width, height = input_maze_size(input_size)
            print("Let's build a maze with", width, "in width and", height,
                  "in height")
            # draw the maze by hand typing
            maze = diy_maze(width, height)
        # User can ask the program to read an existing maze file
        elif command == 2:
            # read an existing maze file
            read_maze, size_line = read_maze_file()
            # get the width and height from the string above
            width, height = input_maze_size(size_line)
            # store lines of maze into a list
            maze = input_maze(read_maze)
        # print the maze made by hand typing or existing file
        for line in maze:
            print(line)
        # store the locations of maze parts to a dictionary
        maze_dictionary = build_maze_map(maze)
        # ask user to choose a start position in the maze
        # update the maze_dictionary with start position
        beginning, maze_dictionary = start_point(maze_dictionary,
                                                 width, height)
        # find all of the exits from the start position
        maze_exit = exit_point(maze_dictionary)
        # find the nearest exit from the start position
        # store all of the steps that the function tries to find the way out
        # get the shortest distance
        find_exit, movement, distance = \
            find_path(maze_dictionary, beginning, maze_exit)
        print("The shortest distence between start and exit is:", distance)
        # draw the maze which shows the shortest path
        draw_shortest_path(find_exit, movement, beginning,
                           maze_dictionary, width, height)

        print(options)
        command = input("Please select an option by input an integer:")
        while not command.isdigit():
            print(TypeError, "Please input a integer between 1 to 3.")
            print(options)
            command = input("Please select an option by input an integer:")
        while int(command) < 1 or int(command) > 3:
            print(ValueError, "Please choose a valid option.")
            print(options)
            command = input("Please select an option by input an integer:")


if __name__ == "__main__":
    main()
